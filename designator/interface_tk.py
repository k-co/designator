'''
Created on 11 de ago de 2019

@author: k_co
'''
from tkinter import *


VERSAO = '0.0.1-tk'

class App(Tk):
    def __init__(self):
        super(App,self).__init__()
        #print('\n#Tk.'.join(dir(Tk)))
        #Tk._Misc__winfo_getint
        #Tk._Misc__winfo_parseitem
        #Tk.__class__
        #Tk.__delattr__
        #Tk.__dict__
        #Tk.__dir__
        #Tk.__doc__
        #Tk.__eq__
        #Tk.__format__
        #Tk.__ge__
        #Tk.__getattr__
        #Tk.__getattribute__
        #Tk.__getitem__
        #Tk.__gt__
        #Tk.__hash__
        #Tk.__init__
        #Tk.__le__
        #Tk.__lt__
        #Tk.__module__
        #Tk.__ne__
        #Tk.__new__
        #Tk.__reduce__
        #Tk.__reduce_ex__
        #Tk.__repr__
        #Tk.__setattr__
        #Tk.__setitem__
        #Tk.__sizeof__
        #Tk.__str__
        #Tk.__subclasshook__
        #Tk.__weakref__
        #Tk._bind
        #Tk._configure
        #Tk._displayof
        #Tk._getboolean
        #Tk._getconfigure
        #Tk._getconfigure1
        #Tk._getdoubles
        #Tk._getints
        #Tk._grid_configure
        #Tk._gridconvvalue
        #Tk._loadtk
        #Tk._nametowidget
        #Tk._noarg_
        #Tk._options
        #Tk._register
        #Tk._report_exception
        #Tk._root
        #Tk._subst_format
        #Tk._subst_format_str
        #Tk._substitute
        #Tk._tclCommands
        #Tk._w
        #Tk._windowingsystem
        #Tk.after
        #Tk.after_cancel
        #Tk.after_idle
        #Tk.anchor
        #Tk.aspect
        #Tk.attributes
        #Tk.bbox
        #Tk.bell
        #Tk.bind
        #Tk.bind_all
        #Tk.bind_class
        #Tk.bindtags
        #Tk.cget
        #Tk.client
        #Tk.clipboard_append
        #Tk.clipboard_clear
        #Tk.clipboard_get
        #Tk.colormapwindows
        #Tk.columnconfigure
        #Tk.command
        #Tk.config
        #Tk.configure
        #Tk.deiconify
        #Tk.deletecommand
        #Tk.destroy
        #Tk.event_add
        #Tk.event_delete
        #Tk.event_generate
        #Tk.event_info
        #Tk.focus
        #Tk.focus_displayof
        #Tk.focus_force
        #Tk.focus_get
        #Tk.focus_lastfor
        #Tk.focus_set
        #Tk.focusmodel
        #Tk.forget
        #Tk.frame
        Tk.geometry(self,'600x400')
        #Tk.getboolean
        #Tk.getdouble
        #Tk.getint
        #Tk.getvar
        #Tk.grab_current
        #Tk.grab_release
        #Tk.grab_set
        #Tk.grab_set_global
        #Tk.grab_status
        #Tk.grid
        #Tk.grid_anchor
        #Tk.grid_bbox
        #Tk.grid_columnconfigure
        #Tk.grid_location
        #Tk.grid_propagate
        #Tk.grid_rowconfigure
        #Tk.grid_size
        #Tk.grid_slaves
        #Tk.group
        #Tk.iconbitmap
        #Tk.iconify
        #Tk.iconmask
        #Tk.iconname
        #Tk.iconphoto
        #Tk.iconposition
        #Tk.iconwindow
        #Tk.image_names
        #Tk.image_types
        #Tk.keys
        #Tk.lift
        #Tk.loadtk
        #Tk.lower
        #Tk.mainloop
        #Tk.manage
        #Tk.maxsize
        #Tk.minsize
        #Tk.nametowidget
        #Tk.option_add
        #Tk.option_clear
        #Tk.option_get
        #Tk.option_readfile
        #Tk.overrideredirect
        #Tk.pack_propagate
        #Tk.pack_slaves
        #Tk.place_slaves
        #Tk.positionfrom(self, who)
        #Tk.propagate
        #Tk.protocol
        #Tk.quit
        #Tk.readprofile
        #Tk.register
        #Tk.report_callback_exception
        #Tk.resizable
        #Tk.rowconfigure
        #Tk.selection_clear
        #Tk.selection_get
        #Tk.selection_handle
        #Tk.selection_own
        #Tk.selection_own_get
        #Tk.send
        #Tk.setvar
        #Tk.size
        #Tk.sizefrom
        #Tk.slaves
        #Tk.state
        Tk.title(self,'Designator v.%s' % VERSAO)
        #Tk.tk_bisque
        #Tk.tk_focusFollowsMouse
        #Tk.tk_focusNext
        #Tk.tk_focusPrev
        #Tk.tk_menuBar
        #Tk.tk_setPalette
        #Tk.tk_strictMotif
        #Tk.tkraise
        #Tk.transient
        #Tk.unbind
        #Tk.unbind_all
        #Tk.unbind_class
        #Tk.update
        #Tk.update_idletasks
        #Tk.wait_variable
        #Tk.wait_visibility
        #Tk.wait_window
        #Tk.waitvar
        #Tk.winfo_atom
        #Tk.winfo_atomname
        #Tk.winfo_cells
        #Tk.winfo_children
        #Tk.winfo_class
        #Tk.winfo_colormapfull
        #Tk.winfo_containing
        #Tk.winfo_depth
        #Tk.winfo_exists
        #Tk.winfo_fpixels
        #Tk.winfo_geometry
        #Tk.winfo_height
        #Tk.winfo_id
        #Tk.winfo_interps
        #Tk.winfo_ismapped
        #Tk.winfo_manager
        #Tk.winfo_name
        #Tk.winfo_parent
        #Tk.winfo_pathname
        #Tk.winfo_pixels
        #Tk.winfo_pointerx
        #Tk.winfo_pointerxy
        #Tk.winfo_pointery
        #Tk.winfo_reqheight
        #Tk.winfo_reqwidth
        #Tk.winfo_rgb
        #Tk.winfo_rootx
        #Tk.winfo_rooty
        #Tk.winfo_screen
        #Tk.winfo_screencells
        #Tk.winfo_screendepth
        #Tk.winfo_screenheight
        #Tk.winfo_screenmmheight
        #Tk.winfo_screenmmwidth
        #Tk.winfo_screenvisual
        #Tk.winfo_screenwidth
        #Tk.winfo_server
        #Tk.winfo_toplevel
        #Tk.winfo_viewable
        #Tk.winfo_visual
        #Tk.winfo_visualid
        #Tk.winfo_visualsavailable
        #Tk.winfo_vrootheight
        #Tk.winfo_vrootwidth
        #Tk.winfo_vrootx
        #Tk.winfo_vrooty
        #Tk.winfo_width
        #Tk.winfo_x
        #Tk.winfo_y
        #Tk.withdraw
        #Tk.wm_aspect
        #Tk.wm_attributes
        #Tk.wm_client
        #Tk.wm_colormapwindows
        #Tk.wm_command
        #Tk.wm_deiconify
        #Tk.wm_focusmodel
        #Tk.wm_forget
        #Tk.wm_frame
        #Tk.wm_geometry
        #Tk.wm_grid
        #Tk.wm_group
        #Tk.wm_iconbitmap
        #Tk.wm_iconify
        #Tk.wm_iconmask
        #Tk.wm_iconname
        #Tk.wm_iconphoto
        #Tk.wm_iconposition
        #Tk.wm_iconwindow
        #Tk.wm_manage
        #Tk.wm_maxsize
        #Tk.wm_minsize
        #Tk.wm_overrideredirect
        #Tk.wm_positionfrom
        #Tk.wm_protocol
        #Tk.wm_resizable
        #Tk.wm_sizefrom
        #Tk.wm_state
        #Tk.wm_title(self,'Designator v.%s' % VERSAO)
        #Tk.wm_transient
        #Tk.wm_withdraw
        
        self.nome = Entry(self)
        self.nome.grid(column=0,row=0)
        
        self.bt = Button(self, text='ok',command=self.botao_ok)
        self.bt['textvariable']='123456'
        
        #print("\n#Tk.Button.".join(dir(bt)))
        
        self.bt.grid(column=1,row=0)        
        
        self.chave_0 = Checkbutton(self, text="Publicador")
        self.chave_0.grid(row=1,column=0)
        
        
        self.mainloop()
    
    def botao_ok(self):
        print('ok '+ self)
        
        
if __name__ == '__main__':
    app = App()