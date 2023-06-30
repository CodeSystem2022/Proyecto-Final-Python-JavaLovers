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
