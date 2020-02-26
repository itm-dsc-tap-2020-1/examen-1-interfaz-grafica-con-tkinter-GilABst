import tkinter as tk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from tkinter import Menu
from tkinter import ttk

#Funcion click
def click():
    int contador
	ventana=tk.Tk()
	ventana.title("Calificacion")
	uno_click=uno.get()
    if uno_click == 14: contador=contador+20
    dos_click=dos.get()
    if dos_click == 6: contador=contador+20
    opcion_click=opcion.get()
    if opcion_click==1: contador=contador+20
    opcion1_click=opcion1.get()
    if opcion1_click==1: contador=contador+20



#Definir ventana
ventana=tk.Tk()
ventana.title("Examen matematicas")

#Pregunta 1
uno= tk.StringVar()
unoCapturado = ttk.Entry(ventana, width=12, textvariable=uno)
ttk.Label(ventana, text= "(3*3)+5").grid (column=0,row=0)
unoCapturado.grid(column=1,row=0)

#Pregunta 2
dos= tk.StringVar()
dosCapturado = ttk.Entry(ventana, width=12, textvariable=dos)
ttk.Label(ventana, text= "(3/3)+5").grid (column=0,row=1)
dosCapturado.grid(column=1,row=1)

#Pregunta 3
ttk.Label(ventana, text= "¿Cuanto es 30/2?").grid (column=1,row=2)

opcion=tk.IntVar()
radio1=tk.Radiobutton(ventana,text="15",variable=opcion,value=1)
radio1.grid(column=0,row=3,sticky=tk.W)

radio2=tk.Radiobutton(ventana,text="10",variable=opcion,value=2)
radio2.grid(column=1,row=3,sticky=tk.W)

radio3=tk.Radiobutton(ventana,text="6",variable=opcion,value=3)
radio3.grid(column=2,row=3,sticky=tk.W)

#Pregunta 4
ttk.Label(ventana, text= "¿Cuanto vale x si: x+2=0?").grid (column=1,row=4)

opcion1=tk.IntVar()
r1=tk.Radiobutton(ventana,text="x=-2",variable=opcion1,value=1)
r1.grid(column=0,row=5,sticky=tk.W)

r2=tk.Radiobutton(ventana,text="x=2",variable=opcion1,value=2)
r2.grid(column=1,row=5,sticky=tk.W)

r3=tk.Radiobutton(ventana,text="x=0",variable=opcion1,value=3)
r3.grid(column=2,row=5,sticky=tk.W)

#Pregunta 5
ttk.Label(ventana, text= "infinito/infinito=").grid (column=1,row=6)

opcion_1= tk.IntVar()
casilla_1 = tk.Checkbutton(ventana,text="0", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0,row=7,sticky=tk.W)

opcion_2= tk.IntVar()
casilla_2 = tk.Checkbutton(ventana,text="1",variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1,row=7,sticky=tk.W)

opcion_3= tk.IntVar()
casilla_3 = tk.Checkbutton(ventana,text="infinito", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2,row=7,sticky=tk.W)

opcion_4= tk.IntVar()
casilla_4 = tk.Checkbutton(ventana,text="-infinito", variable=opcion_3)
casilla_4.deselect()
casilla_4.grid(column=3,row=7,sticky=tk.W)

accion=ttk.Button(ventana, text="Entregar respuestas",command=click)
accion.grid(column=3,row=8)

ventana.mainloop()