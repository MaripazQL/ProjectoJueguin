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
    
    #VENTANA DONDE ESTÁ LA INFORMACIÓN PERSONAL
    def ventana2():
        ventanaInfo = Toplevel()
        ventanaInfo.title("PERSONAL INFORMATION")
        ventanaInfo.geometry("540x690")
        ventanaInfo.resizable(False,False)
        imginfo = ImageTk.PhotoImage(Image.open("INFO.jpg"))
        fondo2 = Label(ventanaInfo, image= imginfo)
        fondo2.pack(side="top", anchor="center")
        
        #Botón que devuelve a la ventana principal
        backy = Button(ventanaInfo, text="Back", fg="#C6BCDE", font=("Open Sans Extrabold", 8), background="#071E26", borderwidth=3, command=ventanaInfo.destroy)
        backy.place(x=500, y=680, anchor=SW)
        ventanaInfo.mainloop()
     
     #VENTANA DONDE  ESTÁN LAS INDICACIONES DE CÓMO JUGAR    
    def ventana3():
        ventanaComo = Toplevel()
        ventanaComo.title("HOW TO PLAY")
        ventanaComo.geometry("960x540")
        ventanaComo.resizable(False,False)
        imgComo = ImageTk.PhotoImage(Image.open("Como.jpg"))
        fondo3 = Label(ventanaComo, image= imgComo)
        fondo3.pack(side="top", anchor="center")
        
        #BOTÓN QUE REGRESA A LA PANTALLA PRINCIPAL
        regreso = Button(ventanaComo, text="Back", fg="#071E26", font=("Open Sans Extrabold", 8), background="#B04FAD", borderwidth=3, command=ventanaComo.destroy)
        regreso.place(x=900, y=510, anchor=SW)
        
        
        ventanaComo.mainloop()
        
    # VENTANA DONDE ESTÁ EL HISTORIAL DE LOS MEJORES PUNTAJES
    def ventana4 ():
        ventanaScores = Toplevel()
        ventanaScores.title("BEST SCORES")
        
        ventanaScores.mainloop()
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 1
    def ventana5 ():
        ventanaN1 = Toplevel()
        ventanaN1.title("BEST SCORES")
    
        ventanaN1.mainloop()
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 2
    def ventana6 ():
        ventanaN2 = Toplevel()
        ventanaN2.title("BEST SCORES")
    
        ventanaN2.mainloop()
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 3
    def ventana7 ():
        ventanaN3 = Toplevel()
        ventanaN3.title("BEST SCORES")
    
        ventanaN3.mainloop()
        
    """B O T O N E S  D E  L A  V E N T A N A  P R I N C I P A L"""
    #Botón de cerrar
    byebye = Button(ventanaPrin, text="E X I T", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background="#6069AE", borderwidth=3, command=ventanaPrin.destroy)
    byebye.place(x=1200, y=665, anchor=SW)
    
    #Botón para abrir la ventana con mi información personal
    infopersonal = Button(ventanaPrin, text="I N F O", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background= "#6069AE", borderwidth=3, command=ventana2)
    infopersonal.place(x=120, y=665, anchor=SE)
    
    #Botón para abrir ventana que explica cómo jugar el juego
    como = Button(ventanaPrin, text="HOW TO PLAY", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana3)
    como.place(x=520, y=240, anchor=NE)
    
    #Botón para abrir ventana que muestra los mejores puntajes
    scores = Button(ventanaPrin, text="BEST SCORES", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana4)
    scores.place(x=810, y=240, anchor=NW)
    
    #Botón para abrir ventana de juego primer nivel
    level1 = Button(ventanaPrin, text="LEVEL 1", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana5)
    level1.place(x=350, y=495, anchor=SE)
    
    #Botón para abrir ventana de juego segundo nivel
    level2 = Button(ventanaPrin, text="LEVEL 2", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana6)
    level2.place(x=667, y=495, anchor=S)
    
    #Botón para abrir ventana de juego tercer nivel
    level2 = Button(ventanaPrin, text="LEVEL 3", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana7)
    level2.place(x=1059, y=495, anchor=S)
    
    
    ventanaPrin.mainloop()
ventana1()
    