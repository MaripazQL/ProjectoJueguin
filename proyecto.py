"""Proyecto programable de Taller 
Maripaz Quesada Leitón 2023073101"""

#Juego "Dystopic Space Battle"
# Juego donde el usuario obtiene una nave espacial y la controla para eliminar enemigos e invasores

#Importaciones necesarias para el funcionamiento del programa
from tkinter import *
from PIL import Image, ImageTk
import random
import threading
import subprocess
from pygame import mixer

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
    #Fondo de la ventana principal
    imgI = ImageTk.PhotoImage (Image.open("Princi.jpg"))
    fondo = Label(ventanaPrin,image= imgI)
    fondo.pack(side="top", anchor="center")      
    
    #FUNCIÓN QUE REPRODUCE MÚSICA EN VENTANA ´PRINCIPAL
    mixer.init()
    mixer.music.load("bombatronic.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)
    
    
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
    #VENTANA DONDE ESTÁ LA INFORMACIÓN PERSONAL
    def ventana2():
        ventanaPrin.withdraw()
        ventanaInfo = Toplevel()
        ventanaInfo.title("PERSONAL INFORMATION")
        ventanaInfo.geometry("540x690")
        ventanaInfo.resizable(False,False)
        imginfo = ImageTk.PhotoImage(Image.open("INFO.jpg"))
        fondo2 = Label(ventanaInfo, image= imginfo)
        fondo2.pack(side="top", anchor="center")
        
        #FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def endINFO():
            ventanaPrin.deiconify()
            ventanaInfo.destroy()
        #Botón que devuelve a la ventana principal
        backy = Button(ventanaInfo, text="Back", fg="#C6BCDE", font=("Open Sans Extrabold", 8), background="#071E26", borderwidth=3, command=(endINFO))
        backy.place(x=500, y=680, anchor=SW)
        ventanaInfo.mainloop()
        
        
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""    
    #VENTANA DONDE  ESTÁN LAS INDICACIONES DE CÓMO JUGAR    
    def ventana3():
        ventanaPrin.withdraw()
        ventanaComo = Toplevel()
        ventanaComo.title("HOW TO PLAY")
        ventanaComo.geometry("960x540")
        ventanaComo.resizable(False,False)
        imgComo = ImageTk.PhotoImage(Image.open("Como.jpg"))
        fondo3 = Label(ventanaComo, image= imgComo)
        fondo3.pack(side="top", anchor="center")
        
        #FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def endINDI():
            ventanaPrin.deiconify()
            ventanaComo.destroy()
        #BOTÓN QUE REGRESA A LA PANTALLA PRINCIPAL
        regreso = Button(ventanaComo, text="Back", fg="#071E26", font=("Open Sans Extrabold", 8), background="#B04FAD", borderwidth=3, command=endINDI)
        regreso.place(x=900, y=510, anchor=SW)
        ventanaComo.mainloop() #Importante 
        
        
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
    # VENTANA DONDE ESTÁ EL HISTORIAL DE LOS MEJORES PUNTAJES
    def ventana4 ():
        ventanaScores = Toplevel()
        ventanaScores.title("BEST SCORES")
        ventanaScores.geometry("500x500")
        
        
        ventanaScores.mainloop()
        
        
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
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
        nave = canvasN1.create_image(100,35, image= imgNAVE)
        
        #CÓDIGO QUE GENERA LOS BORDES PARA QUE LA NAVE NO SE SALGA
        def naveBorde():
            naveBordee = canvasN1.bbox(nave)
            naveleft = naveBordee[0]
            naveRight = naveBordee[2]
            naveTop = naveBordee[1]
            naveBottom = naveBordee[3]
            
            if naveleft < 0: #si el borde de la nave es menor que 0 (borde de la pantalla), que no avance
                canvasN1.move(nave, 10, 0)
            
            elif naveTop < 0:
                canvasN1.move(nave, 0, 10)
                
            elif naveRight > 564:
                canvasN1.move(nave, -10, 0)
                
            elif naveBottom > 564:
                canvasN1.move(nave, 0, -10)
                
        
        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def moveRight(event):
            canvasN1.move(nave,10,0)
            naveBorde()
        def moveLeft(event):
            canvasN1.move(nave,-10,0)
            naveBorde()
        def moveUp(event):
            canvasN1.move(nave,0,-10)
            naveBorde()
        def moveDown(event):
            canvasN1.move(nave,0,10)
            naveBorde()
            
        #Conexión de teclas con la nave
        canvasN1.bind_all("<w>", moveUp)
        canvasN1.bind_all("<s>", moveDown)
        canvasN1.bind_all("<a>", moveLeft)
        canvasN1.bind_all("<d>", moveRight)
        
        
        
        #IMAGEN CORAZONES DE VIDA1
        imgCORA1 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(40,2,anchor=NE, image=imgCORA1)
        
        #IMAGEN CORAZONES DE VIDA2
        imgCORA2 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(80,2,anchor=NE, image=imgCORA2)
        
        #IMAGEN CORAZONES DE VIDA3
        imgCORA3 = ImageTk.PhotoImage(Image.open("Heart.png"))
        canvasN1.create_image(120,2,anchor=NE, image=imgCORA3)
        
        #FUNCIÓN QUE DEVUELVE A LA PANTAÑA PRINCIPAL Y ELIMINA LA ACTUAL
        def chao():
            ventanaPrin.deiconify()
            ventanaN1.destroy()
        #BOTÓN QUE EJECUTA LA FUNCIÓN CHAO
        comeback = Button(canvasN1, text="End", fg="black", font=("Open Sans Extrabold", 8), background="#C6BCDE", borderwidth=3, command=chao)
        comeback.place(x=530, y=560, anchor=SW)
        ventanaN1.mainloop()
        
        
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
    #VENTANA DONDE SE MUESTRA EL NIVEL 2
    def ventana6 ():
        ventanaN2 = Toplevel()
        ventanaN2.title("Nivel 2")
        ventanaN2.resizable(False,False)
        #IMAGEN DE FONDO DEL NIVEL 2
        canvas2 = Canvas(ventanaN2, height=505, width=700)
        canvas2.pack(side="top", anchor="center")
        imgFN2 = ImageTk.PhotoImage(Image.open("FONDO2.jpg"))
        canvas2.create_image(698,2,anchor=NE, image=imgFN2)

        #IMAGEN NAVE NIVEL 2
        imgNave2 = ImageTk.PhotoImage(Image.open("nave2.png"))
        canvas2.create_image(101, 2, anchor= NE, image=imgNave2)
        
        def nave2Borde():
            nave2Bordee = canvas2.bbox(imgNave2)
            nave2left = nave2Bordee[0]
            nave2Right = nave2Bordee[2]
            nave2Top = nave2Bordee[1]
            nave2Bottom = nave2Bordee[3]
            
            if nave2left < 0: #si el borde de la nave es menor que 0 (borde de la pantalla), que no avance
                canvas2.move(imgNave2, 10, 0)
            
            elif nave2Top < 0:
                canvas2.move(imgNave2, 0, 10)
                
            elif nave2Right > 505:
                canvas2.move(imgNave2, -10, 0)
                
            elif nave2Bottom > 700:
                canvas2.move(imgNave2, 0, -10)
                
        
        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def move2Right(event):
            canvas2.move(imgNave2,10,0)
            nave2Borde()
        def move2Left(event):
            canvas2.move(imgNave2,-10,0)
            nave2Borde()
        def move2Up(event):
            canvas2.move(imgNave2,0,-10)
            nave2Borde()
        def move2Down(event):
            canvas2.move(imgNave2,0,10)
            nave2Borde()
            
        #Conexión de teclas con la nave
        canvas2.bind_all("<w>", move2Up)
        canvas2.bind_all("<s>", move2Down)
        canvas2.bind_all("<a>", move2Left)
        canvas2.bind_all("<d>", move2Right)
        

        
        #FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def ending():
            ventanaPrin.deiconify()
            ventanaN2.destroy()
        #BOTÓN QUE EJECUTA LA FUNCIÓN ENDING
        regreso = Button(ventanaN2, text="Back", fg="#C6BCDE", font=("Open Sans Extrabold", 8), background="#071E26", borderwidth=3, command=ending)
        regreso.place(x=565, y=420, anchor=SW)
        ventanaN2.mainloop()
        
        
    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""
    #VENTANA DONDE SE MUESTRA EL NIVEL 3
    def ventana7 ():
        ventanaN3 = Toplevel()
        ventanaN3.title("Nivel 3")
        ventanaN3.geometry("730x626")
        ventanaN3.resizable(False,False)
        
        #CANVAS DEL NIVEL 3
        CanvasN3 = Canvas(ventanaN3, height=625, width=729)
        CanvasN3.pack(side="top", anchor="center")
        #IMAGEN DE FONDO NIVEL 3
        imgN3 = ImageTk.PhotoImage(Image.open("nivel3.jpg"))
        CanvasN3.create_image(729,2, anchor=NE, image= imgN3)
        
        #IMAGEN NAVE NIVEL 3
        imgNave = ImageTk.PhotoImage(Image.open("nave3.png"))
        CanvasN3.create_image(120,2, anchor=NE, image= imgNave)
        
        #IMAGEN DE ENEMIGOS
        imgENE2 = ImageTk.PhotoImage(Image.open("enemigon3.png"))
        CanvasN3.create_image(200,4, anchor=NW, image=imgENE2)
        
        #FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def FINISH():
            ventanaPrin.deiconify()
            ventana7.destroy()
        #BOTÓN QUE EJECUTA LA FUNCIÓN FINISH
        beback = Button(ventanaN3, text="Back", fg="#004B6B", font=("Open Sans Extrabold", 8), background="#B04FAD", borderwidth=3, command= FINISH)
        beback.place(x=800, y=690, anchor=SW)
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