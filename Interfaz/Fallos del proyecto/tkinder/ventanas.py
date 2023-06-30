from tkinter import* 
from tkinter import ttk,messagebox
from data import Datos
import sqlite3
from tkinter import*
from PIL import Image, ImageTk
import cv2
import imutils

class Login(Frame):
    image=None
    def __init__(self,padre,controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=600,height=600)
        self.controlador=controlador
        self.widgets()
        self.imagen()

    def imagen(self):
        global image
        image=cv2.imread("gigachad_man.jpeg")
        image_show=imutils.resize(image,width=240,height=240)
        image_show=cv2.cvtColor(image_show,cv2.COLOR_BGR2RGB)
        im=Image.fromarray(image_show)
        img=ImageTk.PhotoImage(image=im)
        self.perfil.configure(image=img)
        self.perfil.image=img

    def validacion(self,user,pas):
        return len(user)>0 and len(pas)>0
    def login(self):
        with sqlite3.connect("database.db") as conn:
            cursor=conn.cursor()
            user=self.username.get()
            pas=self.password.get()
            if self.validacion(user,pas):
                consulta="SELECT*FROM usuarios WHERE name=? AND password=?"
                parametros=(user,pas)
                try:
                    cursor.execute(consulta,parametros)
                    if cursor.fetchall():
                        self.control1()
                    else:
                        self.username.delete(0,END)
                        self.password.delete(0,END)
                        messagebox.showerror(title="Error",message="Usuario y/o clase incorrecta")
                except:
                    messagebox.showerror(title="Error",message="No se conecto a la base")
            else:
                messagebox.showerror(title="Error",message="Pasa la info loco")
            cursor.close()
        

    def control1(self):
        self.controlador.show_frame(Contenedor)

    def control2(self):
        self.controlador.show_frame(Registro)

    def widgets(self):
        fondo=Frame(self,bg="black")
        fondo.pack()
        fondo.place(x=0,y=0,width=600,height=600)
        self.perfil=Label(fondo)
        self.perfil.place(x=200,y=50)
        user = Label(fondo, text="Inicio de Sesion")
        user.place(x=250, y=300)
        self.username=Entry(fondo)
        self.username.place(x=250,y=340,width=140,height=20)
        self.password=Entry(fondo,show="*")
        self.password.place(x=250,y=390,width=140,height=20)
        btn1=Button(fondo,bg="blue",fg="white",text="Iniciar",command=self.login)
        btn1.place(x=250,y=420)
        btn2=Button(fondo,bg="blue",fg="white",text="Registrar",command=self.control2)
        btn2.place(x=300,y=420)

    
class Registro(Frame):
    def __init__(self,padre,controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=600,height=600)
        self.controlador=controlador
        self.widgest()

    def validacion(self,user,pas):
        return len(user)>0 and len(pas)>0
    def eje_consulta(self,consulta,parametros=()):
        db=Datos()
        db.consultas(consulta,parametros)

    def registro(self):
        user=self.username.get()
        pas=self.password.get()
        if self.validacion(user, pas):
            if len(pas)<6:
                messagebox.showinfo(title="Error",message="Clase FACIL")
                self.username.delete(0,END)
                self.password.delete(0,END)
            else:
                consulta="INSERT INTO usuarios VALUES(?,?,?)"
                parametros=(None,user,pas)
                self.eje_consulta(consulta,parametros)
                self.control1()
        else:
            messagebox.showerror(title="Error", message="Llena los datos")
    def control1(self):
        self.controlador.show_frame(Contenedor)

    def control2(self):
        self.controlador.show_frame(Login)

    def widgest(self):
        fondo=Frame(self,bg="cyan")
        fondo.pack()
        fondo.place(x=0,y=0,width=600,height=600)
        user=Label(fondo,text="Nombre de usuario")
        user.place(x=250,y=240)
        self.username=Entry(fondo,font="Arial 16")
        self.username.place(x=250,y=280,width=140,height=20)
        pas=Label(fondo,text="Clave de Seguridad")
        pas.place(x=250,y=340)
        self.password=Entry(fondo,show="*",font=16)
        self.password.place(x=250,y=380,width=140,height=20)
        btn1=Button(fondo,bg="blue",fg="white",text="Atras",command=self.control2)
        btn1.place(x=320, y=460)
        btn2=Button(fondo,bg="blue",fg="white",text="Registrar",command=self.registro)
        btn2.place(x=250,y=460)

class Contenedor(Frame):
    def __init__(self,padre,controlador):
        super().__init__(padre)
        self.controlador=controlador
        self.pack()
        self.place(x=0,y=0,width=600,height=600)
        self.widgets()
        self.frame={}

        for i in (Game_1,Game_2):
            frame=i(self)
            self.frame[i]=frame
            frame.pack()
            frame.config(bg="blue")
            frame.place(x=0,y=40,width=600,height=600)
        self.show_frames(Game_1)
    def show_frames(self,contenedor):
        frame=self.frame[contenedor]
        frame.tkraise()

    def game_1(self):
        self.show_frames(Game_1)

    def game_2(self):
        self.show_frames(Game_2)

    def widgets(self):
        game1=Button(self,text="juego 1",command=self.game_1)
        game1.pack()
        game1.place(x=0,y=0,width=300,height=40)
        game2=Button(self,text="juego 2",command=self.game_2)
        game2.pack()
        game2.place(x=300,y=0,width=300,height=40)

class Game_1(Frame):
    def __init__(self,padre):
        super().__init__(padre)
        self.widgets()
    def widgets(self):
        game1=Label(self,text="juego 1")
        game1.pack()
        game1.place(x=258,y=450)

class Game_2(Frame):
    def __init__(self,padre):
        super().__init__(padre)
        self.widgets()
    def widgets(self):
        game2=Label(self,text="juego 2")
        game2.pack()
        game2.place(x=248,y=450)




