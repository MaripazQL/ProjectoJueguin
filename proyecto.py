"""Proyecto programable de Taller 
Maripaz Quesada Leitón 2023073101"""

#Juego "Dystopic Space Battle"
# Juego donde el usuario obtiene una nave espacial y la controla para eliminar enemigos e invasores

#Importaciones necesarias para el funcionamiento del programa
from tkinter import *
from PIL import Image, ImageTk

#c o l o r e s
whitish = "#C6BCDE"
brightpinky ="#FA1593"
barbiepink = "#EB649F"
darkpurple = "#22234A"
lightpurple = "#6069AE"
slay = "#B04FAD"
lightblue = "#95DEFF"
oceanblue = "#004B6B"
darky = "#071E26"

#Ventana principal con la temática del juego
def ventana1():
    ventanaPrin = Tk()
    ventanaPrin.title("Dystopic Space Battle")
    ventanaPrin.geometry("1300x700")
    ventanaPrin.resizable(False,False)
    ventanaPrin.config(bg="#22234A")
    imgI = ImageTk.PhotoImage (Image.open("Princi.jpg"))
    fondo = Label(ventanaPrin,image= imgI)
    fondo.pack(side="top", anchor="center")
    
    #Botón de cerrar
    byebye = Button(ventanaPrin, text="E X I T", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background="#6069AE", borderwidth=3, command=ventanaPrin.destroy)
    byebye.place(x=1200, y=665, anchor=SW)
    
    #Botón para abrir la ventana con mi información personal
    infopersonal = Button(ventanaPrin, text="I N F O", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background= "#6069AE", borderwidth=3)
    infopersonal.place(x=120, y=665, anchor=SE)
    
    #Botón para abrir ventana que explica cómo jugar el juego
    como = Button(ventanaPrin, text="HOW TO PLAY", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE")
    como.place(x=520, y=240, anchor=NE)
    
    #Botón para abrir ventana que muestra los mejores puntajes
    scores = Button(ventanaPrin, text="BEST SCORES", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE")
    scores.place(x=810, y=240, anchor=NW)
    
    #Botón para abrir ventana de juego primer nivel
    level1 = Button(ventanaPrin, text="LEVEL 1", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE")
    level1.place(x=350, y=495, anchor=SE)
    
    #Botón para abrir ventana de juego segundo nivel
    level2 = Button(ventanaPrin, text="LEVEL 2", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE")
    level2.place(x=667, y=495, anchor=S)
    
    
    ventanaPrin.mainloop()
ventana1()
    