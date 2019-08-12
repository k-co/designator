'''
Created on 12 de ago de 2019

@author: k_co
'''

import gi, json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

'''
estas duas funções podem ser importantes no decorrer do desenvolvimento:
elas podem conter os widgets de seleção de arquivo.
'''
def salvar_dados_json(arquivo,dados):
    '''sarvar dados no formato json
    @arquivo caminho para o arquivo
    @dados dados a serem salvos
    '''
    try:
        with open(arquivo,'w') as doc:
            json.dump(dados,doc)
    except Exception as e:
        print('erro ao salvar arquivo: %s\n%s' %(arquivo,e))
        
def carregar_dados_json(arquivo):
    '''retorna dados do formato json
    @arquivo caminho para o arquivo
    '''
    with open(arquivo,'r') as doc:
        return json.load(doc)

class Janela_Editor_Lista():
    '''
    classdocs
    '''
    def __init__(self,DEBUGAR=None):
        '''
        Constructor
        '''
        try:
            self.inicia_interface()
        except Exception as e:
            print('Erro ao carregar o arquivo de layout\n%s' % e)
        
        self.debugar = DEBUGAR
        self.LISTA = {}       
        
    def inicia_interface(self):
        _construtor = Gtk.Builder()
        Gtk.Builder.add_from_file(_construtor,'layout2.glade')
        self.janela = _construtor.get_object('window1')
        self.janela.connect('destroy', self.on_quit)
        self.janela.set_title('Editor de Lista de Participantes')
        self.janela.show_all()
        
        self.manipulador = self.inicia_manipuladores()
        Gtk.Builder.connect_signals(_construtor, self.manipulador)
        
        self.entrada = _construtor.get_object('entry1')
        self.listagem = _construtor.get_object('listbox1')
        self.c_pub = _construtor.get_object('checkbutton1')
        self.c_lei = _construtor.get_object('checkbutton2')
        self.c_ora = _construtor.get_object('checkbutton3')
        self.c_ser = _construtor.get_object('checkbutton4')
        self.c_anc = _construtor.get_object('checkbutton5')
        self.c_int = _construtor.get_object('checkbutton6')
        
        self.c_pub.set_label('Publicador')
        self.c_lei.set_label('Leitor')
        self.c_ora.set_label('Oração')
        self.c_ser.set_label('Servo')
        self.c_anc.set_label('Ancião')
        self.c_int.set_label('Interpretação')
        self.janela.show_all()
        
    def inicia_manipuladores(self):
        return {
            "adicionar": self.adicionar,
            "excluir": self.excluir,
            "abrir": self.abrir,
            "salvar": self.salvar,
            "selecionar": self.selecionar            
            }
    
    def on_quit(self,wid,par=None):
        Gtk.main_quit()
        
    def atualizar_lista(self):
        if self.debugar: print('atualizar') 
        '''limpa a listagem'''
        filhos = self.listagem.get_children()
        if filhos is not None:
            for i in filhos:
                self.listagem.remove(i)
        '''adiciona os itens da lista'''
        lista = self.LISTA          # carrega dicionario
        if lista is not None:       # se não estiver vazio
            lista_org = []
            for i in lista:
                lista_org.append(i) # transforma em lista
            lista_org.sort()        # organiza
            for i in lista_org:     # adiciona itens a listagem 
                self.listagem.add(Gtk.Label(i))
                self.listagem.show_all()
        
    def adicionar(self,wid,par=None):
        nome = self.entrada.get_text()
        if nome == None or nome in self.LISTA:
            return
        partes = 0
        if self.c_pub.get_active(): partes += 1
        if self.c_lei.get_active(): partes += 2
        if self.c_ora.get_active(): partes += 4
        if self.c_ser.get_active(): partes += 8
        if self.c_anc.get_active(): partes += 16
        if self.c_int.get_active(): partes += 32       
        partes = str(partes)
        self.LISTA[nome]=partes
        self.atualizar_lista()
        if self.debugar: print('adicionar %s %s' % (nome,partes))
        
    def excluir(self,wid,par=None):
        if self.debugar: print('excluir')
        item = self.listagem.get_selected_row()
        if item == None:
            return
        nome = item.get_children()[0].get_text()
        self.LISTA.pop(nome)
        self.atualizar_lista()
        
    def abrir(self,wid,par=None):
        dados = carregar_dados_json('arquivo.json')
        if dados == None:
            return
        self.LISTA = dados
        self.atualizar_lista()
        if self.debugar: print('abrir')
        
    def salvar(self,wid,par=None):
        salvar_dados_json('arquivo.json', self.LISTA)
        if self.debugar: print('salvar')
        
    def selecionar(self,wid,par=None):
        item = wid.get_selected_row()
        if item == None:
            return
        nome = item.get_children()[0].get_text()
        valor = int(self.LISTA[nome])
        self.c_pub.set_active(valor & 1)
        self.c_lei.set_active(valor & 2)
        self.c_ora.set_active(valor & 4)
        self.c_ser.set_active(valor & 8)
        self.c_anc.set_active(valor & 16)
        self.c_int.set_active(valor & 32)
        if self.debugar: print('selecionar')          
        

if __name__ == '__main__':
    app = Janela_Editor_Lista(1)
    Gtk.main()
    
    