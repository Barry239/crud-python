import tkinter as tk

from db import DBConnection
from models import User

class MainApp(tk.Frame):
    __current = -1

    def __init__(self, master, *args, **kargs):
        tk.Frame.__init__(self, master, *args, **kargs)
        self.master = master

        ## Configurar columnas
        self.grid_columnconfigure((0, 8), weight=1)

        ## Crear diseño
        self.title = tk.Label(self, text='CRUD', font=('Lucida Calligraphy', 16, 'bold'))
        self.title.grid(row=0, column=1, columnspan=5, pady=(18, 14))

        self.usernameLabel = tk.Label(self, text='Usuario:', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.usernameLabel.grid(row=2, column=1, padx=(2, 0), pady=(0, 5))
        self.usernameEntry = tk.Entry(self, font=('Lucida Sans Typewriter', 10))
        self.usernameEntry.grid(row=2, column=2, padx=(0, 2), pady=(0, 5))
        self.emailLabel = tk.Label(self, text='Correo:', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.emailLabel.grid(row=3, column=1, padx=(2, 0), pady=(0, 5))
        self.emailEntry = tk.Entry(self, font=('Lucida Sans Typewriter', 10))
        self.emailEntry.grid(row=3, column=2, padx=(0, 2), pady=(0, 5))
        
        self.idHeaderLabel = tk.Label(self, text='ID', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.idHeaderLabel.grid(row=2, column=3, padx=(84, 6), pady=(0, 5))
        self.usernameHeaderLabel = tk.Label(self, text='Usuario', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.usernameHeaderLabel.grid(row=2, column=4, padx=(6, 6), pady=(0, 5))
        self.emailHeaderLabel = tk.Label(self, text='Correo', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.emailHeaderLabel.grid(row=2, column=5, padx=(6, 6), pady=(0, 5))
        self.actionHeaderLabel = tk.Label(self, text='Acción', font=('Lucida Sans Typewriter', 10, 'italic'))
        self.actionHeaderLabel.grid(row=2, column=6, columnspan=2, padx=(6, 2), pady=(0, 5))

        self.submitButton = tk.Button(self, text='Submit', font=('Comic Sans MS', 10), fg='#fff', bg='#0d6efd', command=self.addUser)
        self.submitButton.grid(row=4, column=1, columnspan=2, pady=(16, 5), sticky='WE')

        ## Enfocar en la primera entrada
        self.usernameEntry.focus()

        ## Cargar usuarios
        self.getUsers()

    def addUser(self):
        ## Obtener datos ingresados
        username = self.usernameEntry.get()
        email = self.emailEntry.get()
        user = User(username=username, email=email)

        if (self.__current == -1):
            ## Crear usuario
            DBConnection().createUser(user)
        else:
            ## Editar usuario
            DBConnection().updateUser(self.__current, user)

            ## Cambiar bandera
            self.__current = -1

        ## Limpiar entradas
        self.usernameEntry.delete(0, tk.END)
        self.emailEntry.delete(0, tk.END)

        ## Cargar usuarios
        self.getUsers()

    def getUsers(self):
        ## Obtener usuarios
        users = DBConnection().getUsers()

        ## Limpiar datos de la tabla
        for widget in self.grid_slaves():
            if (widget.grid_info()['column'] >= 3 and widget.grid_info()['row'] >= 3):
                widget.grid_forget()

        ## Mostrar datos en la tabla
        for i, user in enumerate(users, 3):
            id = tk.Label(self, text=user.getId(), font=('Lucida Sans Typewriter', 10, 'italic'))
            id.grid(row=i, column=3, padx=(84, 6), pady=(0, 5))
            username = tk.Label(self, text=user.getUsername(), font=('Lucida Sans Typewriter', 10, 'italic'))
            username.grid(row=i, column=4, padx=(6, 6), pady=(0, 5))
            email = tk.Label(self, text=user.getEmail(), font=('Lucida Sans Typewriter', 10, 'italic'))
            email.grid(row=i, column=5, padx=(6, 6), pady=(0, 5))

            editButton = tk.Button(self, text='Editar', font=('Comic Sans MS', 10), fg='#fff', bg='#ffc107', command=lambda: self.editUser(user.getId()))
            editButton.grid(row=i, column=6, padx=(6, 6), pady=(0, 5), sticky='WE')
            deleteButton = tk.Button(self, text='Eliminar', font=('Comic Sans MS', 10), fg='#fff', bg='#dc3545', command=lambda: self.deleteUser(user.getId()))
            deleteButton.grid(row=i, column=7, padx=(6, 2), pady=(0, 5), sticky='WE')

    def editUser(self, id):
        ## Obtener usuario
        user = DBConnection().getUser(id)

        ## Limpiar entradas
        self.usernameEntry.delete(0, tk.END)
        self.emailEntry.delete(0, tk.END)

        ## Mostrar datos del usuario
        self.usernameEntry.insert(0, user.getUsername())
        self.emailEntry.insert(0, user.getEmail())

        ## Cambiar bandera
        self.__current = user.getId()
    
    def deleteUser(self, id):
        ## Eliminar usuario
        DBConnection().deleteUser(id)

        ## Cargar usuarios
        self.getUsers()
