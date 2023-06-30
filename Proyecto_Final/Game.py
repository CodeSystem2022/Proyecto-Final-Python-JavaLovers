 # initialize_db: Este método inicializa la base de datos SQLite. Crea una tabla llamada 'partida' si no existe y si no existe una fila con id=1 en la tabla 'partida', la crea e inicializa la vida en 100 y la arma en "puños".    
    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()


        # Crear la tabla 'partida' si no existe
        cursor.execute('CREATE TABLE IF NOT EXISTS partida (id INTEGER UNIQUE, vida INTEGER, arma TEXT)')


        # Comprobar si la fila con id=1 ya existe
        cursor.execute('SELECT id FROM partida WHERE id = 1')
        if cursor.fetchone() is None:
            # Si no existe, insertar la fila
            cursor.execute('INSERT INTO partida (id, vida, arma) VALUES (1, 100, "puños")')


        conn.commit()
        conn.close()
       
    # create_intro_screen: Este método crea la pantalla de inicio del juego mostrando una etiqueta con el texto "UTN WARS". Después de 5 segundos, limpia la ventana y crea los botones de inicio.    
    def create_intro_screen(self):
        self.label = tk.Label(self.window, text="UTN WARS", font=("Arial", 24))
        self.label.place(relx=0.5, rely=0.5, anchor='center')  # Coloca la etiqueta en el centro de la ventana
        self.window.after(5000, self.clear_window)
        self.window.after(5000, self.create_intro_buttons)


    # create_intro_buttons: Este método crea los botones de "Nueva partida" y "Cargar partida" en la pantalla de inicio.
    def create_intro_buttons(self):
        # Añade la imagen de fondo antes de añadir los botones
        image = Image.open("d:\\Descargas\\Carpetas\\UTN\\Tec. Prog\\Tercer Semestre\\Programacion III\\Proyecto-Python\\Proyecto-codigo\\imagen00.jpg")  # Cambia 'background_image.jpg' por la ruta de tu imagen
        image = image.resize((800, 600), Image.ANTIALIAS)  # Cambia los valores para que coincidan con el tamaño de tu ventana
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.intro_frame = tk.Frame(self.window)
        self.intro_frame.place(relx=0.5, rely=0.5, anchor='center')  # Coloca el frame en el centro de la ventana


        self.new_game_button = tk.Button(self.intro_frame, text="Nueva partida", command=self.start_new_game)
        self.new_game_button.pack(pady=10)


        self.load_game_button = tk.Button(self.intro_frame, text="Cargar partida", command=self.load_game)
        self.load_game_button.pack(pady=10)

        
    # start_new_game: Este método inicia una nueva partida. Limpia la ventana, crea la barra de estado del jugador,
    # muestra el campus y actualiza la barra de estado del jugador.
    def start_new_game(self):
        self.clear_window()
        self.create_player_status()  # Creación de la barra de estado
        self.show_campus()
        self.update_player_status()  # Se actualiza la barra de estado
     
   # load_game: Este método carga una partida guardada. Recupera los datos de la partida de la base de datos y los asigna al estado del jugador.
    # Luego, limpia la ventana, crea la barra de estado del jugador, muestra el campus y actualiza la barra de estado.
    def load_game(self):
        self.clear_window()
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT vida, arma FROM partida WHERE id = 1')
        vida, arma = cursor.fetchone()
        self.player_state['vida'] = vida
        self.player_state['arma'] = arma
        conn.close()
        self.create_player_status()  
        self.show_campus() 
        self.update_player_status() 
     # clear_window: Este método limpia todos los widgets de la ventana principal de tkinter, excepto el marco de estado.
    def clear_window(self):
        for widget in self.window.winfo_children():
            # Aquí se utiliza getattr para obtener el atributo "status_frame" del objeto self (que es una instancia de la clase Game). 
            # Si "status_frame" no existe (lo que sucede antes de que se haya llamado a start_new_game o load_game), getattr retorna None.
            # Luego, se verifica si el widget actual es diferente de "status_frame". Si es así, el widget se destruye.
            # De esta manera, "status_frame" no se destruirá incluso si clear_window se llama antes de que "status_frame" se haya definido.
            if widget != getattr(self, "status_frame", None):  
                widget.destroy()
     # create_player_status: Este método crea la barra de estado del jugador.
    def create_player_status(self):
        self.status_frame = tk.Frame(self.window, relief="sunken", borderwidth=1)
        self.status_frame.pack(anchor='ne', padx=10, pady=10)
        self.update_player_status()
     
     # update_player_status: Este método actualiza la barra de estado del jugador mostrando la vida y el arma actual del jugador.
    def update_player_status(self):
        for widget in self.status_frame.winfo_children():
            widget.destroy()
        vida_label = tk.Label(self.status_frame, text="Vida: {}".format(self.player_state['vida']))
        vida_label.pack(side="left")
        arma_label = tk.Label(self.status_frame, text="Arma: {}".format(self.player_state['arma']))
        arma_label.pack(side="left")
     
# return_to_campus: Este método lleva al jugador de vuelta al campus desde otra vista (por ejemplo, después de visitar la cafetería). Limpia la ventana para deshacerse de todos los widgets actuales (excepto el marco de estado, como se explicó anteriormente), muestra el campus y actualiza la barra de estado del jugador.
    def return_to_campus(self):
        self.clear_window()
        # Llama a show_campus para mostrar la vista del campus (que incluye varios botones para visitar diferentes lugares).
        self.show_campus()
        # Después de eso, verifica si se ha definido "status_frame" utilizando hasattr.
        # Si "status_frame" está definido (lo que significa que ya se ha iniciado o cargado un juego), se llama a update_player_status para actualizar la barra de estado del jugador.
        # Si "status_frame" no está definido, simplemente se omite esta actualización.
        # Por lo tanto, si se llama a return_to_campus antes de que se haya iniciado o cargado un juego, simplemente se mostrará la vista del campus sin una barra de estado del jugador.
        if hasattr(self, "status_frame"): 
            self.update_player_status()

# show_campus: Este método muestra los botones del campus que permiten al jugador visitar diferentes ubicaciones.
    def show_campus(self):
        # Creación de los botones del campus
     
        cafeteria_button = tk.Button(self.window, text="Visitar la cafetería", command=lambda: self.visit_cafeteria(initial=True))
        cafeteria_button.pack()

        multiuse_button = tk.Button(self.window, text="Visitar el salón de usos múltiples", command=self.visit_multiuse_room)
        multiuse_button.pack()
     
     

     
aca lo tuyo aldo









# visit_cafeteria: Este método representa la acción de visitar la cafetería. El jugador pierde vida al visitar la cafetería y se le presentan varias opciones de acción, en las cuales también puede perder vida. Por el momento no se agregaran más acciones, solo en futuras actualizaciones del código.    
    def visit_cafeteria(self, initial=False):
        if initial:
            self.player_state["vida"] -= 10  # El jugador pierde 10 de vida
            message1 = "¿Con que holgazaneando fuera del horario de estudio, eh?, *10 puntos menos para Gryffindor* digo,*muere holgazán*"
        else:
            self.player_state["vida"] -= 1  # El jugador pierde 1 de vida
            message1 = "*¿Todavía no aprendes?*"


        self.clear_window()


        label1 = tk.Label(self.window, text=message1, wraplength=400)
        label1.pack()
       
        if initial:
            message2 = "*Y que eso te sirva de lección, termina rapidamente aqui y continua con tus estudios*"
            label2 = tk.Label(self.window, text=message2, wraplength=400)
            label2.pack()


        vending_machine_button = tk.Button(self.window, text="Comprar de la máquina expendedora", command=self.visit_cafeteria)
        vending_machine_button.pack()


        steal_food_button = tk.Button(self.window, text="Manotear la comida de las mesas", command=self.visit_cafeteria)
        steal_food_button.pack()


        tip_button = tk.Button(self.window, text="Dejar propina al chico de la cafetería", command=self.visit_cafeteria)
        tip_button.pack()


        run_away_button = tk.Button(self.window, text="Huir despavorido", command=self.return_to_campus)
        run_away_button.pack()
       
    # visit_multiuse_room: Este método representa la acción de visitar la sala de usos múltiples. En este lugar, el jugador ve una "escena" y puede decidir volver al campus. Por el momento no se agregaran más acciones, solo en futuras actualizaciones del código.
    def visit_multiuse_room(self):
        self.clear_window()
        label1 = tk.Label(self.window, text="Al entrar ves equipos de mate tirados y gente durmiendo, mejor decides no preguntar y volver en otro momento", wraplength=400)
        label1.pack()
        button1 = tk.Button(self.window, text="Regresas sigilosamente", command=self.return_to_campus)
        button1.pack()

# visit_bathroom: Este método representa la acción de visitar el baño. El jugador puede investigar o decidir volver al campus. Por el momento no se agregaran más acciones, solo en futuras actualizaciones del código.
    def visit_bathroom(self, initial=True):
        if initial:
            self.clear_window()
            label1 = tk.Label(self.window, text="Sientes cierto olor, que no es a flores en el aire, pero ciertamente retrata la solemnidad del lugar, puedes regresar o investigar más", wraplength=400)
            label1.pack()
            button1 = tk.Button(self.window, text="Investigar el lugar del santo sepulcro", command=lambda: self.visit_bathroom(initial=False))
            button1.pack()
            button2 = tk.Button(self.window, text="Regresar a la civilización", command=self.return_to_campus)
            button2.pack()
        else:
            self.player_state["vida"] -= 1
            self.clear_window()
            label1 = tk.Label(self.window, text="*¿Qué demonios haces en un baño para hombres, cochino degenerado?*", wraplength=400)
            label1.pack()
            time.sleep(2)
            self.visit_bathroom(initial=True)


    # go_to_class: Este método representa la acción de ir a clases. Dependiendo de las acciones del jugador, se puede ganar o perder vida (+1 o -1 de vida). Por el momento no se agregaran más acciones, solo en futuras actualizaciones del código.
    def go_to_class(self, initial=True):
        if initial:
            self.player_state["vida"] += 1
            self.clear_window()
            label1 = tk.Label(self.window, text="Ya era hora de que llegaras, ten toma asiento mocoso", wraplength=400)
            label1.pack()
            button1 = tk.Button(self.window, text="Ruega por la iluminación", command=lambda: self.go_to_class(initial=False))
            button1.pack()
            button2 = tk.Button(self.window, text="Regresar a casa", command=self.return_to_campus)
            button2.pack()
        else:
            self.player_state["vida"] -= 1
            self.clear_window()
            label1 = tk.Label(self.window, text="*¿Así que quieres aprender?, bien por ti*\n*Golpe mortal*", wraplength=400)
            label1.pack()
            time.sleep(2)
            self.clear_window()
            label2 = tk.Label(self.window, text="*Para que aprendas a no ser un lamebotas*", wraplength=400)
            label2.pack()
            time.sleep(2)
            self.go_to_class(initial=True)
        pass
   
    # save_game: Este método guarda el estado actual del juego en la base de datos. Guarda la vida y el arma actual del jugador en la base de datos.
    def save_game(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('UPDATE partida SET vida = ?, arma = ? WHERE id = 1', (self.player_state['vida'], self.player_state['arma']))
        conn.commit()
        conn.close()


# Se crea una instancia del juego y se inicia la ejecución
game = Game()

