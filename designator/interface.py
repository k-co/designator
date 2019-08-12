'''
Created on 11 de ago de 2019

@author: k_co
https://python-gtk-3-tutorial.readthedocs.io/en/latest/application.html
'''
import gi
from AptUrl import gtk
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gio

LISTA = {}
DATAS = {}
    
class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="org.kinfoseg.designator")
        
        self.manipulador = {
            "localizar": self.localizar,
            "adicionar": self.adicionar,
            "excluir": self.excluir,
            "abrir": self.abrir,
            "salvar": self.salvar
            }
        
        self.janela = None
        
    def do_startup(self):
        Gtk.Application.do_startup(self)
        
        action = Gio.SimpleAction.new("Sair",None)
        action .connect("activate", self.on_quit)
        self.add_action(action)
               
    def do_activate(self):
        if self.janela == None:
            _construtor = Gtk.Builder().new_from_file('layout.glade')
            self.janela = _construtor.get_object('janela_editar_participantes')
            self.listagem = _construtor.get_object('caixa_listagem') 
            self.entrada = _construtor.get_object('entrada_nome')
            

            self.c_pub = _construtor.get_object('check_publicador')
            self.c_lei = _construtor.get_object('check_leitor')
            self.c_ora = _construtor.get_object('check_oracao')
            self.c_ser = _construtor.get_object('check_servo')
            self.c_anc = _construtor.get_object('check_anciao')
            self.c_int = _construtor.get_object('check_interpretacao')
            
            Gtk.ApplicationWindow.set_application(self.janela,self)
            Gtk.Builder.connect_signals(_construtor, self.manipulador)
            
            self.janela.present()
        
    def on_quit(self, action, param):
        self.quit()
        
    '''Agora é que o bixo vai pegar
    '''
        
    def localizar(self,action,param=None):
        #Gtk.ListBox.get_row_at_index()
        #nome = self.entrada.get_text()
        print('localizar')
        
    def adicionar(self,action,param=None):
        nome = self.entrada.get_text()
        partes = 0        
        if not nome=='' and nome not in LISTA:
            
            if self.c_pub.get_active(): partes += 1
            if self.c_lei.get_active(): partes += 2
            if self.c_ora.get_active(): partes += 4
            if self.c_ser.get_active(): partes += 8
            if self.c_anc.get_active(): partes += 16
            if self.c_int.get_active(): partes += 32
            
            Gtk.ListBox.add(self.listagem,Gtk.Label(nome))
            Gtk.ListBox.show_all(self.listagem)
            LISTA[nome]=str(partes)
            print('adicionar %s %s' % (nome,partes))
        else:
            print('Erro: Verifique o Nome')
    
    def excluir(self,action,param=None):
        item = Gtk.ListBox.get_selected_row(self.listagem)  #linha selecionada
        nome = item.get_children()[0].get_text()            #primeiro filho da linha selecionada
        LISTA.pop(nome)                                     #removido da lista principal
        Gtk.ListBox.remove(self.listagem,item)              #removido da ListBox
        Gtk.ListBox.show_all(self.listagem)                 #mostrar alterações
        print('excluir')
               
    def abrir(self,action,param=None):
        print('abrir')
             
    def salvar(self, action,param=None):
        print('salvar')

        
if __name__ == '__main__':
    app = App()
    app.run()