
from tkinter import*
from tkinter import messagebox
from ventanas import Login,Registro,Contenedor
from data import Datos


class Manager(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("JAVALOVERS")
        self.geometry("600x600")
        self.menu()
        contenedor=Frame(self)
        contenedor.pack(side=TOP,fill=BOTH,expand=True)
        contenedor.configure(bg="green")

        self.frame={}
        for i in (Login,Registro,Contenedor):
            frame=i(contenedor,self)
            self.frame[i]=frame
        self.show_frame(Login)

    def crearDB(self):
        db=Datos()
        try:
            db.crear()
        except:
            messagebox.showinfo(title="Informacion",message="La base de datos ya esta creada")

    def menu(self):
        menubar=Menu()
        menudata=Menu(menubar,tearoff=0)
        menudata.add_command(label="Crear/conectar Base de datos",command=self.crearDB)
        menubar.add_cascade(label="Inicio",menu=menudata)
        self.config(menu=menubar)

    def show_frame(self,contenedor):
        frame=self.frame[contenedor]
        frame.tkraise()

