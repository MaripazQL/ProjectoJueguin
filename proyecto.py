"""Proyecto programable de Taller Maripaz Quesada Leitón 2023073101"""
# Juego "Dystopic Space Battle"
# Juego donde el usuario obtiene una nave espacial y la controla para eliminar enemigos e invasores
# Importaciones necesarias para el funcionamiento del programa
from tkinter import *
from PIL import Image, ImageTk
import random
import threading
import subprocess
from pygame import mixer

# c o l o r e s
whitish = "#C6BCDE"
brightpinky = "#FA1593"
barbiepink = "#EB649F"
darkpurple = "#22234A"
lightpurple = "#6069AE"
slay = "#B04FAD"
lightblue = "#95DEFF"
oceanblue = "#004B6B"
darky = "#071E26"

#GLOBAL VARIABLE DEL PUNTAJE DEL NIVEL 1-2-3
score1 = 0
score2 = 0
score3 = 0

#GLOBAL DE VIDAS DEL NIVEL 1-2-3
vidas1 = 3
vidas2 = 3
vidas3 = 3

#GLODAL DE ENEMIGOS DEL NIVEL 1-2-2
alien1 = 7
alien2 = 9
alien3 = 12
################################################################################################################

# Ventana principal con la temática del juego
def ventana1():
    ventanaPrin = Tk()
    ventanaPrin.title("Dystopic Space Battle")
    ventanaPrin.geometry("1300x700")
    ventanaPrin.resizable(False, False)
    ventanaPrin.config(bg="#22234A")
    # Fondo de la ventana principal
    imgI = ImageTk.PhotoImage(Image.open("Princi.jpg"))
    fondo = Label(ventanaPrin, image=imgI)
    fondo.pack(side="top", anchor="center")

    # FUNCIÓN QUE REPRODUCE MÚSICA EN VENTANA ´PRINCIPAL
    mixer.init()
    mixer.music.load("bombatronic.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.2)


    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

    # VENTANA DONDE ESTÁ LA INFORMACIÓN PERSONAL
    def ventana2():
        ventanaPrin.withdraw()
        ventanaInfo = Toplevel()
        ventanaInfo.title("PERSONAL INFORMATION")
        ventanaInfo.geometry("540x690")
        ventanaInfo.resizable(False, False)
        imginfo = ImageTk.PhotoImage(Image.open("INFO.jpg"))
        fondo2 = Label(ventanaInfo, image=imginfo)
        fondo2.pack(side="top", anchor="center")


        # FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def endINFO():
            ventanaPrin.deiconify()
            ventanaInfo.destroy()


        # Botón que devuelve a la ventana principal
        backy = Button(ventanaInfo, text="Back", fg="#C6BCDE", font=("Open Sans Extrabold", 8), background="#071E26",
                       borderwidth=3, command=endINFO)
        backy.place(x=500, y=680, anchor=SW)
        ventanaInfo.mainloop()


    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""



    # VENTANA DONDE  ESTÁN LAS INDICACIONES DE CÓMO JUGAR
    def ventana3():
        ventanaPrin.withdraw()
        ventanaComo = Toplevel()
        ventanaComo.title("HOW TO PLAY")
        ventanaComo.geometry("960x540")
        ventanaComo.resizable(False, False)
        imgComo = ImageTk.PhotoImage(Image.open("Como.jpg"))
        fondo3 = Label(ventanaComo, image=imgComo)
        fondo3.pack(side="top", anchor="center")


        # FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def endINDI():
            ventanaPrin.deiconify()
            ventanaComo.destroy()


        # BOTÓN QUE REGRESA A LA PANTALLA PRINCIPAL
        regreso = Button(ventanaComo, text="Back", fg="#071E26", font=("Open Sans Extrabold", 8), background="#B04FAD",
                         borderwidth=3, command=endINDI)
        regreso.place(x=900, y=510, anchor=SW)
        ventanaComo.mainloop()  # Importante




    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""



    # VENTANA DONDE ESTÁ EL HISTORIAL DE LOS MEJORES PUNTAJES
    def ventana4():
        ventanaScores = Toplevel()
        ventanaScores.title("BEST SCORES")
        ventanaScores.geometry("500x500")

        ventanaScores.mainloop()


    """wwwwwwwwwwwwwwwwwwwwwwwwwwwWWWW-- N I V E L 1 --WWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""



    # VENTANA DONDE SE MUESTRA EL NIVEL 1
    def ventana5():
        ventanaN1 = Toplevel()
        ventanaN1.title("Nivel 1")
        ventanaN1.resizable(False, False)

        """FONDO NIVEL 1"""
        # CANVAS DEL NIVEL 1 DEL JUEGO.
        canvasN1 = Canvas(ventanaN1, height=564, width=564)
        canvasN1.pack(side="top", anchor="center")
        # IMAGEN DE FONDO DEL JUEGO
        imgFN1 = ImageTk.PhotoImage(Image.open("nivel1.jpg"))
        canvasN1.create_image(564, 1, anchor=NE, image=imgFN1)

        """I M A G E N E S  D E L   N I V E L 1"""
        # IMAGEN BALA JUGADOR
        imgbalaj = ImageTk.PhotoImage(Image.open("balame.png"))
        balame = canvasN1.create_image(150, 100, image=imgbalaj)

        # IMAGEN DEL ENEMIG0
        imgalien = ImageTk.PhotoImage(Image.open("alien1.png"))
        alien = canvasN1.create_image(300, 60, image=imgalien)

        # IMAGEN BALA DEL ENEMIGO
        imgboom = ImageTk.PhotoImage(Image.open("balaenemigo.png"))
        boom = canvasN1.create_image(250, 170, image=imgboom)

        """TEXTOS NIVEL 1"""
        #TEXTO CON LAS VIDAS
        textovida = Label(canvasN1, text="LIVES", font=("Minecraft", 13), fg="white", bg="black")
        textovida.place(x=10, y=9)
        textovar = Label(canvasN1,text=vidas1, font=("Minecraft", 13), fg="white", bg="black")
        textovar.place(x=70, y=9)

        # TEXTO CON EL SCORE
        texto1 = Label(canvasN1, text="SCORE", font=("Minecraft", 13), fg="white", bg="black")
        texto1.place(x=180, y=9)
        textoscore = Label(canvasN1, text=score1, font=("Minecraft", 13), fg="white", bg="black")
        textoscore.place(x=260, y=9)

        #TEXTO CON CANTIDAD DE ENEMIGOS
        textoenes = Label(canvasN1, text="ENEMIES", font=("Minecraft", 13), fg="white", bg="black")
        textoenes.place(x=300, y=9)
        textosalien = Label(canvasN1, text=alien1, font=("Minecraft", 13), fg="white", bg="black")
        textosalien.place(x=270, y=9)
        """-----------------------------------------------------------------------"""

        #PARTE DEL CÓDIGO QUE MUEVE LA NAVE DEL NIVEL 1
        # IMAGEN DE LA NAVE
        imgNAVE = ImageTk.PhotoImage(Image.open("nave.png"))
        nave = canvasN1.create_image(180, 75, image=imgNAVE)

        # CÓDIGO QUE GENERA LOS BORDES PARA QUE LA NAVE NO SE SALGA
        def naveBorde(): # Esta parte establece los bordes de la imagen
            naveBordee = canvasN1.bbox(nave)
            naveleft = naveBordee[0]
            naveRight = naveBordee[2]
            naveTop = naveBordee[1]
            naveBottom = naveBordee[3]

            if naveleft < 0:  # si el borde de la nave es menor que 0 (borde de la pantalla), que no avance
                canvasN1.move(nave, 10, 0)

            elif naveTop < 0:
                canvasN1.move(nave, 0, 10)

            elif naveRight > 564:
                canvasN1.move(nave, -10, 0)

            elif naveBottom > 564:
                canvasN1.move(nave, 0, -10)


        def collisionn1():
            sbb = canvasN1.bbox(nave)
            ebb = canvasN1.bbox(alien)

            # Si la nave toca el extremo izquierdo abajo del alien, que el alien se mueva y que le reste una vida
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3]:
                canvasN1.move(alien,400,400)

            #Si la nave toca el extremo izquierdo arriba, que el alien se mueva y que le reste una vida
            elif ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                canvasN1.move(alien, 400,400)
            #Si la nave toca el extremo derecho abajo de la nave, que el alien se mueva y que le reste una vida
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2]:
                canvasN1.move(alien,400,400)
            #Si la nave toca el extremo derecho arriba de la nave, que el alien se mueva
            elif ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                canvasN1.move(alien,400,400)



        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE PARA VERIFICAR QUE NO SE HA SALIDO
        def moveRight(event):
            canvasN1.move(nave, 10, 0)
            naveBorde()
            collisionn1()
        def moveLeft(event):
            canvasN1.move(nave, -10, 0)
            naveBorde()
            collisionn1()
        def moveUp(event):
            canvasN1.move(nave, 0, -10)
            naveBorde()
            collisionn1()
        def moveDown(event):
            canvasN1.move(nave, 0, 10)
            naveBorde()
            collisionn1()

        # Conexión de teclas con la nave
        canvasN1.bind_all("<w>", moveUp)
        canvasN1.bind_all("<s>", moveDown)
        canvasN1.bind_all("<a>", moveLeft)
        canvasN1.bind_all("<d>", moveRight)
        """-----------------------------------------------------------------------"""


        #INICIO DE COLISIONES ENTRE ENEMIGOS Y JUGADOR


        #FUNCIÓN QUE DEVUELVE A LA PANTAÑA PRINCIPAL Y ELIMINA LA ACTUAL
        def chao():
            ventanaPrin.deiconify()
            ventanaN1.destroy()

        # BOTÓN QUE EJECUTA LA FUNCIÓN CHAO
        comeback = Button(canvasN1, text="End", fg="black", font=("Open Sans Extrabold", 8), background="#C6BCDE",
                          borderwidth=3, command=chao)
        comeback.place(x=530, y=560, anchor=SW)
        ventanaN1.mainloop()




    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwWWW--- N I V E L 2 ---WWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

    # VENTANA DONDE SE MUESTRA EL NIVEL 2
    def ventana6():
        ventanaN2 = Toplevel()
        ventanaN2.title("Nivel 2")
        ventanaN2.resizable(False, False)
        # IMAGEN DE FONDO DEL NIVEL 2
        canvas2 = Canvas(ventanaN2, height=505, width=700)
        canvas2.pack(side="top", anchor="center")
        imgFN2 = ImageTk.PhotoImage(Image.open("FONDO2.jpg"))
        canvas2.create_image(698, 2, anchor=NE, image=imgFN2)

        """TEXTOS NIVEL 2"""
        #TEXTO CON LAS VIDAS
        textovida2 = Label(canvas2, text="LIVES", font=("Minecraft", 13), fg="white", bg="#22234A")
        textovida2.place(x=10, y=9)
        textovar2 = Label(canvas2,text=vidas2, font=("Minecraft", 13), fg="white", bg="#22234A")
        textovar2.place(x=75, y=9)

        # TEXTO CON EL SCORE
        texto2 = Label(canvas2, text="SCORE", font=("Minecraft", 13), fg="white", bg="#22234A")
        texto2.place(x=120, y=9)
        texto2score = Label(canvas2, text=score2, font=("Minecraft", 13), fg= "white", bg="#22234A")
        texto2score.place(x=195, y=9)

        #TEXTO CON CANTIDAD DE ENEMIGOS
        textoenes2 = Label(canvas2, text="ENEMIES", font=("Minecraft", 13), fg="white", bg="#22234A")
        textoenes2.place(x=250, y=9)
        textosalien2 = Label(canvas2, text=alien2, font=("Minecraft", 13), fg="white", bg="#22234A")
        textosalien2.place(x=340, y=9)

        """----------------------------------------------------------------------------------"""
        #PARTE DONDE SE MUEVE LA IMAGEN DEL JUGADOR
        # IMAGEN NAVE NIVEL 2
        imgNave2 = ImageTk.PhotoImage(Image.open("nave3.png"))
        nave2 = canvas2.create_image(120, 2, anchor=NE, image=imgNave2)

        def nave2Borde():
            nave2Bordee = canvas2.bbox(nave2)
            nave2left = nave2Bordee[0]
            nave2Right = nave2Bordee[2]
            nave2Top = nave2Bordee[1]
            nave2Bottom = nave2Bordee[3]

            if nave2left < 0:  # si el borde de la nave es menor que 0 (borde de la pantalla), que no avance
                canvas2.move(nave2, 10, 0)

            elif nave2Top < 0:
                canvas2.move(nave2, 0, 10)

            elif nave2Right > 700:
                canvas2.move(nave2, -10, 0)

            elif nave2Bottom > 505:
                canvas2.move(nave2, 0, -10)

        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def move2Right(event):
            canvas2.move(nave2, 10, 0)
            nave2Borde()

        def move2Left(event):
            canvas2.move(nave2, -10, 0)
            nave2Borde()

        def move2Up(event):
            canvas2.move(nave2, 0, -10)
            nave2Borde()

        def move2Down(event):
            canvas2.move(nave2, 0, 10)
            nave2Borde()

        # Conexión de teclas con la nave
        canvas2.bind_all("<w>", move2Up)
        canvas2.bind_all("<s>", move2Down)
        canvas2.bind_all("<a>", move2Left)
        canvas2.bind_all("<d>", move2Right)

        #IMAGEN BALA JUGADOR
        imgbalaj2 = ImageTk.PhotoImage(Image.open("balame.png"))
        balame2 = canvas2.create_image(150,6, image= imgbalaj2)

        """-----------------------------------------------------------------------"""

        # FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def ending():
            ventanaPrin.deiconify()
            ventanaN2.destroy()

        # BOTÓN QUE EJECUTA LA FUNCIÓN ENDING
        regreso = Button(ventanaN2, text="Back", fg="#C6BCDE", font=("Open Sans Extrabold", 8), background="#071E26",
                         borderwidth=3, command=ending)
        regreso.place(x=645, y=500, anchor=SW)
        ventanaN2.mainloop()




    """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwWWW--- N I V E L 3---WWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

    # VENTANA DONDE SE MUESTRA EL NIVEL 3
    def ventana7():
        ventanaN3 = Toplevel()
        ventanaN3.title("Nivel 3")
        ventanaN3.geometry("730x626")
        ventanaN3.resizable(False, False)

        # CANVAS DEL NIVEL 3
        canvas3 = Canvas(ventanaN3, height=625, width=729)
        canvas3.pack(side="top", anchor="center")
        # IMAGEN DE FONDO NIVEL 3
        imgN3 = ImageTk.PhotoImage(Image.open("nivel3.jpg"))
        canvas3.create_image(729, 2, anchor=NE, image=imgN3)
        """T E X T O S   D E L   N I V E L  3"""
        #TEXTO CON LAS VIDAS
        textovida3 = Label(canvas3, text="LIVES", font=("Minecraft", 13), fg="white", bg="#270A4C")
        textovida3.place(x=10, y=9)
        textovar3 = Label(canvas3,text=vidas3, font=("Minecraft", 13), fg="white", bg="#270A4C")
        textovar3.place(x=75, y=9)

        # TEXTO CON EL SCORE
        texton3 = Label(canvas3, text="SCORE", font=("Minecraft", 13), fg="white", bg="#270A4C")
        texton3.place(x=120, y=9)
        texto3score = Label(canvas3, text=score3, font=("Minecraft", 13), fg= "white", bg="#270A4C")
        texto3score.place(x=195, y=9)

        #TEXTO CON CANTIDAD DE ENEMIGOS
        textoenes3 = Label(canvas3, text="ENEMIES", font=("Minecraft", 13), fg="white", bg="#270A4C")
        textoenes3.place(x=250, y=9)
        textosalien3 = Label(canvas3, text=alien3, font=("Minecraft", 13), fg="white", bg="#270A4C")
        textosalien3.place(x=340, y=9)

        # IMAGEN DE ENEMIGOS
        imgENE2 = ImageTk.PhotoImage(Image.open("enemigon3.png"))
        canvas3.create_image(200, 4, anchor=NW, image=imgENE2)

        """INICIO DE FUNCIONES DE NAVE Y ENEMIGOS"""
        # IMAGEN NAVE NIVEL 3
        imgNave3 = ImageTk.PhotoImage(Image.open("nave2.png"))
        nave3 = canvas3.create_image(120, 2, anchor=NE, image=imgNave3)
        def nave3Borde():
            nave3Bordee = canvas3.bbox(nave3)
            nave3left = nave3Bordee[0]
            nave3right = nave3Bordee[2]
            nave3top = nave3Bordee[1]
            nave3bottom = nave3Bordee[3]

            if nave3left < 0:  # si el borde de la nave es menor que 0 (borde de la pantalla), que no avance
                canvas3.move(nave3, 10, 0)

            elif nave3top < 0:
                canvas3.move(nave3, 0, 10)

            elif nave3right > 729:
                canvas3.move(nave3, -10, 0)

            elif nave3bottom > 625:
                canvas3.move(nave3, 0, -10)

        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def move3Right(event):
            canvas3.move(nave3, 10, 0)
            nave3Borde()

        def move3Left(event):
            canvas3.move(nave3, -10, 0)
            nave3Borde()

        def move3Up(event):
            canvas3.move(nave3, 0, -10)
            nave3Borde()

        def move3Down(event):
            canvas3.move(nave3, 0, 10)
            nave3Borde()

        # Conexión de teclas con la nave
        canvas3.bind_all("<w>", move3Up)
        canvas3.bind_all("<s>", move3Down)
        canvas3.bind_all("<a>", move3Left)
        canvas3.bind_all("<d>", move3Right)
        """----------------------------------------------------------------"""


        # FUNCIÓN QUE ELIMINA LA VENTANA ACTUAL Y DEVUELVE A LA VENTANA PRINCIPAL
        def FINISH():
            ventanaPrin.deiconify()
            canvas3.destroy()

        # BOTÓN QUE EJECUTA LA FUNCIÓN FINISH
        beback = Button(ventanaN3, text="Back", fg="#004B6B", font=("Open Sans Extrabold", 8), background="#B04FAD",
                        borderwidth=3, command=FINISH)
        beback.place(x=630, y=600, anchor=SW)
        ventanaN3.mainloop()





    """B O T O N E S  D E  L A  V E N T A N A  P R I N C I P A L"""
    # Botón de cerrar
    byebye = Button(ventanaPrin, text="E X I T", fg="#C6BCDE", font=("Open Sans Extrabold", 12), background="#6069AE",
                    borderwidth=3, command=ventanaPrin.destroy)
    byebye.place(x=1200, y=665, anchor=SW)

    # Botón para abrir la ventana con mi información personal
    infopersonal = Button(ventanaPrin, text="I N F O", fg="#C6BCDE", font=("Open Sans Extrabold", 12),
                          background="#6069AE", borderwidth=3, command=ventana2)
    infopersonal.place(x=120, y=665, anchor=SE)

    # Botón para abrir ventana que explica cómo jugar el juego
    como = Button(ventanaPrin, text="HOW TO PLAY", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD",
                  borderwidth=4, activebackground="#6069AE", command=ventana3)
    como.place(x=520, y=240, anchor=NE)

    # Botón para abrir ventana que muestra los mejores puntajes
    scores = Button(ventanaPrin, text="BEST SCORES", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD",
                    borderwidth=4, activebackground="#6069AE", command=ventana4)
    scores.place(x=810, y=240, anchor=NW)

    # Botón para abrir ventana de juego primer nivel
    level1 = Button(ventanaPrin, text="LEVEL 1", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD",
                    borderwidth=4, activebackground="#6069AE", command=ventana5)
    level1.place(x=350, y=495, anchor=SE)

    # Botón para abrir ventana de juego segundo nivel
    level2 = Button(ventanaPrin, text="LEVEL 2", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD",
                    borderwidth=4, activebackground="#6069AE", command=ventana6)
    level2.place(x=667, y=495, anchor=S)

    # Botón para abrir ventana de juego tercer nivel
    level3 = Button(ventanaPrin, text="LEVEL 3", fg="#C6BCDE", font=("SDGlitchDemo", 33), background="#B04FAD",
                    borderwidth=4, activebackground="#6069AE", command=ventana7)
    level3.place(x=1059, y=495, anchor=S)

    ventanaPrin.mainloop()


ventana1()