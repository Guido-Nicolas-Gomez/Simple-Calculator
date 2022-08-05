"""Interfaz grafica de una calculadora basica, la cual integra las operaciones del modulo operaciones.py"""
# Crear la interface grafica de una calculadora
from functools import partial
from tkinter import * 

#   ____ DEFINICIONES ____
# comandos
def agregar_caracter(caracter):
    """Comando utilizado para agregar un caracter al StringVar utilizado en el display de la calculadora"""
    
    # Limpiar la pantalla si se registro un error
    if formula.get() == 'E R R O R':
        formula.set('')

    # Agregar el caracter presionado    
    formula.set(formula.get() + caracter)

def igual():
    """Comando del boton "igual" la cual llama a la funcion evaluadora de la ecuacion ingresada"""
    try:
        formula.set(eval(formula.get().replace('x','*')))
    except:
        formula.set("E R R O R")


# Ventana
root = Tk()
root.title("Calculadora")
root.iconbitmap("calc_icon.ico")
root.resizable(0,0)
root.config(
    pady=5,
    padx=5
)


# Cabeza
display = Label(root)
formula = StringVar()
display.config(
    textvariable=formula,
    width=20,
    height=2,
    bg= "#192033",
    anchor="e",
    font=("Console",16),
    foreground="#FFFFFD",
)

# Cuerpo
keypads = Frame(root)
keypads.config(
    pady=5,
    width=300,
    height=300,
    bg = '#192033'
)


# Botones
botones_text =[
    {"C": lambda:formula.set(""),"(":"",")":"","/":""},
    {"7":"","8":"","9":"","x":""},
    {"4":"","5":"","6":"","-":""},
    {"1":"","2":"","3":"","+":""},
    {"+/-":lambda:formula.set('-' + formula.get()),"0":"",".":"","=":igual}
    ]

botones={}
for fila in botones_text: #Generando un diccionario con los objetos botones
    for boton in fila:
        if boton == "=":
            botones[boton] = Button(keypads, text=boton, command=fila[boton], bg = '#4CC2FF', fg = '#0E4D6E')

        elif boton == 'C':
            botones[boton] = Button(keypads, text=boton, command=fila[boton], bg = '#2C3145', fg = '#E9EEF1')

        elif boton == "+/-":
            botones["+/-"] = Button(keypads, text="+/-", command=fila["+/-"], bg = '#373A4D', fg = '#E9EEF1')
        
        elif boton in ['(', ')', '/', 'x', '-', '+']:
            formula_anterior = formula.get() + boton
            botones[boton] = Button(keypads, text=boton,activebackground="#ddffff", command=partial(agregar_caracter, boton), bg = '#2C3145', fg = '#E9EEF1')

        else:
            formula_anterior = formula.get() + boton
            botones[boton] = Button(keypads, text=boton,activebackground="#ddffff", command=partial(agregar_caracter, boton), bg = '#373A4D', fg = '#E9EEF1')

        botones[boton].config(
                width=5,
                font=1
            )

#   ____ INSTANCIAS ____

# Cabeza
display.pack()

# Cuerpo
keypads.pack()
for i,v in enumerate(botones_text): #Ubicacndo los botones en una cuadricula
    for j, u in enumerate(v):
        botones[u].grid(row=i,column=j, padx=5, pady=5)

# Ventana
root.config(bg = '#192033')

root.mainloop()
