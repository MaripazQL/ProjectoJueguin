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
        ventanaComo.mainloop() #Importante 
        
        
        
    # VENTANA DONDE ESTÁ EL HISTORIAL DE LOS MEJORES PUNTAJES
    def ventana4 ():
        ventanaScores = Toplevel()
        ventanaScores.title("BEST SCORES")
        
        ventanaScores.mainloop()
        
        
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 1
    def ventana5 ():
        ventanaN1 = Toplevel()
        ventanaN1.title("Nivel 1")
        ventanaN1.resizable(False,False)

        #CANVAS DEL NIVEL 1 DEL JUEGO. 
        canvasN1 = Canvas(ventanaN1, height=564, width=564)
        canvasN1.pack(side="top", anchor="center")
        
        #IMAGEN DE FONDO DEL JUEGO
        imgFN1 = ImageTk.PhotoImage(Image.open("nivel1.jpg"))
        canvasN1.create_image(564,1, anchor= NE, image= imgFN1)
        
        #IMAGEN DE LA NAVE
        imgNAVE = ImageTk.PhotoImage(Image.open("nave.png"))
        canvasN1.create_image(100,35, image= imgNAVE)
        
        
        #IMAGEN CORAZONES DE VIDA1
        imgCORA1 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(40,2,anchor=NE, image=imgCORA1)
        
        #IMAGEN CORAZONES DE VIDA2
        imgCORA2 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(80,2,anchor=NE, image=imgCORA2)
        
        #IMAGEN CORAZONES DE VIDA3
        imgCORA3 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(120,2,anchor=NE, image=imgCORA3)
        
        #BOTÓN DE REGRESAR A LA VENTANA PRINCIPAL
        comeback = Button(canvasN1, text="End", fg="black", font=("Open Sans Extrabold", 8), background="#C6BCDE", borderwidth=3, command=ventanaN1.destroy)
        comeback.place(x=530, y=560, anchor=SW)
        ventanaN1.mainloop()
        
        
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 2
    def ventana6 ():
        ventanaN2 = Toplevel()
        ventanaN2.title("Nivel 2")
    
        ventanaN2.mainloop()
        
        
        
    #VENTANA DONDE SE MUESTRA EL NIVEL 3
    def ventana7 ():
        ventanaN3 = Toplevel()
        ventanaN3.title("Nivel 3")
    
        ventanaN3.mainloop()       
        
        
    """B O T O N E S  D E  L A  V E N T A N A  P R I N C I P A L"""
    #Botón de cerrar
    byebye =Button(ventanaPrin, text="E X I T", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background="#6069AE", borderwidth=3, command=ventanaPrin.destroy)
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
    level3 = Button(ventanaPrin, text="LEVEL 3", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD", borderwidth=4, activebackground="#6069AE", command=ventana7)
    level3.place(x=1059, y=495, anchor=S)
    
    
    ventanaPrin.mainloop()
ventana1()
    