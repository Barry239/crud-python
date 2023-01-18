from tkinter import Tk

from app import MainApp

def main() -> None:
    ## Inicializar ventana
    root = Tk()
    root.title('CRUD')
    root.geometry('900x350')

    ## Crear app
    MainApp(root).pack(side='top', fill='both', expand=True)

    ## Mostrar ventana
    root.mainloop()

if __name__ == '__main__':
    main()
