"""Proyecto programable de Taller Maripaz Quesada Leitón 2023073101"""
# Juego "Dystopic Space Battle"
# Juego donde el usuario obtiene una nave espacial y la controla para eliminar enemigos e invasores
# Importaciones necesarias para el funcionamiento del programa
from tkinter import *
from PIL import Image, ImageTk
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
aliens1 = 7
aliens2 = 9
aliens3 = 12
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
        #DETALLES DEL TITULO Y RESIZE
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
        imgbalaj.image = imgbalaj


        """TEXTOS NIVEL 1"""
        # TEXTO CON LAS VIDAS
        textovida = Label(canvasN1, text="LIVES", font=("Minecraft", 13), fg="white", bg="black")
        textovida.place(x=10, y=9)
        textovar = Label(canvasN1, text=vidas1, font=("Minecraft", 13), fg="white", bg="black")
        textovar.place(x=70, y=9)

        # TEXTO CON EL SCORE
        texto1 = Label(canvasN1, text="SCORE", font=("Minecraft", 13), fg="white", bg="black")
        texto1.place(x=180, y=9)
        textoscore = Label(canvasN1, text=score1, font=("Minecraft", 13), fg="white", bg="black")
        textoscore.place(x=260, y=9)

        # TEXTO CON CANTIDAD DE ENEMIGOS
        textoenes = Label(canvasN1, text="ENEMIES", font=("Minecraft", 13), fg="white", bg="black")
        textoenes.place(x=300, y=9)
        textosalien = Label(canvasN1, text=aliens1, font=("Minecraft", 13), fg="white", bg="black")
        textosalien.place(x=390, y=9)



        """-------------------------------------------------"""

        # IMAGEN DEL ENEMIG0
        imgalien = ImageTk.PhotoImage(Image.open("alien1.png"))

        #FUNCIÓN QUE MUEVE EL ALIEN 1
        def moveali1():
            canvasN1.move(alien,-10,0)
            ventanaN1.after(900, moveali1)
            ebb = canvasN1.bbox(alien)
            if ebb[0] < 0:
                return canvasN1.delete(alien)
        alien = canvasN1.create_image(580, 60, image=imgalien)
        moveali1()

        #FUNCIÓN QUE MUEVE EL ALIEN 2
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali2():
            canvasN1.move(alien1,-10,0)
            ventanaN1.after(800, moveali2)
            ebb2 = canvasN1.bbox(alien1)
            if ebb2[0] < 0:
                return canvasN1.delete(alien1)
        alien1 = canvasN1.create_image(700, 130, image=imgalien)
        moveali2()

        #FUNCIÓN QUE MUEVE EL ALIEN 3
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali3():
            canvasN1.move(alien2,-10,0)
            ventanaN1.after(700, moveali3)
            ebb3 = canvasN1.bbox(alien2)
            if ebb3[0] < 0:
                return canvasN1.delete(alien2)
        alien2 = canvasN1.create_image(800, 190, image=imgalien)
        moveali3()

        #FUNCIÓN QUE MUEVE EL ALIEN 4
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali4():
            canvasN1.move(alien3,-10,0)
            ventanaN1.after(600, moveali4)
            ebb4 = canvasN1.bbox(alien3)
            if ebb4[0] < 0:
                return canvasN1.delete(alien3)
        alien3 = canvasN1.create_image(570, 250, image=imgalien)
        moveali4()

        #FUNCIÓN QUE MUEVE EL ALIEN 5
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali5():
            canvasN1.move(alien4,-10,0)
            ventanaN1.after(700, moveali5)
            ebb5 = canvasN1.bbox(alien4)
            if ebb5[0] < 0:
                return canvasN1.delete(alien4)
        alien4 = canvasN1.create_image(650, 310, image=imgalien)
        moveali5()

        #FUNCIÓN QUE MUEVE EL ALIEN 6
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali6():
            canvasN1.move(alien5,-10,0)
            ventanaN1.after(700, moveali6)
            ebb6 = canvasN1.bbox(alien5)
            if ebb6[0] < 0:
                return canvasN1.delete(alien5)
        alien5 = canvasN1.create_image(500, 370, image=imgalien)
        moveali6()

        #FUNCIÓN QUE MUEVE EL ALIEN 7
        """HACE QUE LA NAVE SE MUEVA, Y QUE SI TOCA EL EXTREMO IZQ DEL CANVAS SE DESAPAREZCA"""
        def moveali7():
            canvasN1.move(alien6,-10,0)
            ventanaN1.after(700, moveali7)
            ebb7 = canvasN1.bbox(alien6)
            if ebb7[0] < 0:
                return canvasN1.delete(alien6)
        alien6 = canvasN1.create_image(600, 430, image=imgalien)
        moveali7()


        """--------------------------C Ó D I G O   Q U E   M U E V E   B A L A------------------------------------"""


        #FUNCIÓN QUE DISPARA LAS BALAS DE LA NAVE
        """Verifica que la bala esté dentro del canvas, y cuando se salga que la función se deje de ejecutar"""
        def moverlabala():
            global balame
            ubi = canvasN1.bbox(balame)
            if ubi[3] < 564:
                canvasN1.move(balame, 10, 0)
            else:
                canvasN1.delete(balame)
            ventanaN1.after(60, moverlabala)

        #FUNCIÓN QUE CREA LA BALA EN EL CENTRO DE LA NAVE Y LLAMA A LA FUNCIÓN MOVERLABALA()
        def shoot(event):
            global balame
            naveBoundd = canvasN1.bbox(nave)
            centrolado = (naveBoundd[0] + naveBoundd[2])/2
            centroancho = (naveBoundd[1] + naveBoundd[3])/2
            balame = canvasN1.create_image(centrolado, centroancho, image=imgbalaj)
            moverlabala()
        """"-----------------------C Ó D I G O  M O V I M I E N T O   N A V E------------------------"""

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

        """----------------- P A R T E    C O L I S I O N E S------------------"""

        def collisionn1():
            sbb = canvasN1.bbox(nave)
            ebb = canvasN1.bbox(alien)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvasN1.delete(alien)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvasN1.delete(alien)
 
        def collisionn2():
            sbb2 = canvasN1.bbox(nave)
            ebb2 = canvasN1.bbox(alien1)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb2[0] < sbb2[2] < ebb2[2] and ebb2[1] < sbb2[1] < ebb2[3]:
                return canvasN1.delete(alien1)
            elif ebb2[0] < sbb2[2] < ebb2[2] and ebb2[1] < sbb2[3] < ebb2[3]:
                return canvasN1.delete(alien1)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb2[1] < sbb2[3] < ebb2[3] and ebb2[0] < sbb2[0] < ebb2[2]:
                return canvasN1.delete(alien1)
            elif ebb2[1] < sbb2[1] < ebb2[3] and ebb2[0] < sbb2[2] < ebb2[3]:
                return canvasN1.delete(alien1)


        def collisionn3():
            sbb = canvasN1.bbox(nave)
            ebb3 = canvasN1.bbox(alien2)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb3[0] < sbb[2] < ebb3[2] and ebb3[1] < sbb[1] < ebb3[3] or ebb3[0] < sbb[2] < ebb3[2] and ebb3[1] < sbb[3] < ebb3[3]:
                return canvasN1.delete(alien2)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb3[1] < sbb[3] < ebb3[3] and ebb3[0] < sbb[0] < ebb3[2] or ebb3[1] < sbb[1] < ebb3[3] and ebb3[0] < sbb[2] < ebb3[3]:
                return canvasN1.delete(alien2)

        def collisionn4():
            sbb = canvasN1.bbox(nave)
            ebb3 = canvasN1.bbox(alien3)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb3[0] < sbb[2] < ebb3[2] and ebb3[1] < sbb[1] < ebb3[3] or ebb3[0] < sbb[2] < ebb3[2] and ebb3[1] < sbb[3] < ebb3[3]:
                return canvasN1.delete(alien3)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb3[1] < sbb[3] < ebb3[3] and ebb3[0] < sbb[0] < ebb3[2] or ebb3[1] < sbb[1] < ebb3[3] and ebb3[0] < sbb[2] < ebb3[3]:
                return canvasN1.delete(alien3)

        def collisionn5():
            sbb = canvasN1.bbox(nave)
            ebb = canvasN1.bbox(alien4)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvasN1.delete(alien4)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvasN1.delete(alien4)

        def collisionn6():
            sbb = canvasN1.bbox(nave)
            ebb = canvasN1.bbox(alien5)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvasN1.delete(alien5)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvasN1.delete(alien5)

        def collisionn7():
            sbb = canvasN1.bbox(nave)
            ebb = canvasN1.bbox(alien6)
            # Si la nave toca el extremo izquierdo abajo del alien, que el alien se mueva
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvasN1.delete(alien6)
           #Si la nave toca el extremo derecho abajo de la nave, que el alien se mueva
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvasN1.delete(alien6)


        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE PARA VERIFICAR QUE NO SE HA SALIDO
        def moveRight(event):
            canvasN1.move(nave, 10, 0)
            naveBorde(), collisionn1(), collisionn2(), collisionn3(), collisionn4(), collisionn5(), collisionn6(), collisionn7()
        def moveLeft(event):
            canvasN1.move(nave, -10, 0)
            naveBorde(), collisionn1(), collisionn2(), collisionn3(), collisionn4(), collisionn5(), collisionn6(), collisionn7()
        def moveUp(event):
            canvasN1.move(nave, 0, -10)
            naveBorde(), collisionn1(), collisionn2(), collisionn3(), collisionn4(), collisionn5(), collisionn6(), collisionn7()
        def moveDown(event):
            canvasN1.move(nave, 0, 10)
            naveBorde(), collisionn1(), collisionn2(), collisionn3(), collisionn4(),collisionn5(), collisionn6(), collisionn7()

        # Conexión de teclas con la nave
        canvasN1.bind_all("<w>", moveUp)
        canvasN1.bind_all("<s>", moveDown)
        canvasN1.bind_all("<a>", moveLeft)
        canvasN1.bind_all("<d>", moveRight)
        canvasN1.bind_all("<space>", shoot)
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
        textosalien2 = Label(canvas2, text=aliens2, font=("Minecraft", 13), fg="white", bg="#22234A")
        textosalien2.place(x=340, y=9)


        """----------------------------------------------------------------------------------"""


        # IMAGEN DE ENEMIGOS
        """FUNCIÓN QUE VE SI EL ENEMIGO ESTÁ EN EL CANVAS, Y SI TOCA EL BORDE IZQUIERDO, SE ELIMINE"""
        imgENE2 = ImageTk.PhotoImage(Image.open("enemigon3.png"))
        def moveni1():
            canvas2.move(enemi1,-10,0)
            ventanaN2.after(600, moveni1)
            ebb1 = canvas2.bbox(enemi1)
            if ebb1[0] < 0:
                return canvas2.delete(enemi1)
        enemi1 = canvas2.create_image(900, 4, image=imgENE2)
        moveni1()

        def moveni2():
            canvas2.move(enemi2,-10,0)
            ventanaN2.after(600, moveni2)
            ebb2 = canvas2.bbox(enemi2)
            if ebb2[0] < 0:
                return canvas2.delete(enemi2)
        enemi2 = canvas2.create_image(700, 120, image=imgENE2)
        moveni2()

        def moveni3():
            canvas2.move(enemi3,-10,0)
            ventanaN2.after(600, moveni3)
            ebb3 = canvas2.bbox(enemi3)
            if ebb3[0] < 0:
                return canvas2.delete(enemi3)
        enemi3 = canvas2.create_image(600, 250, image=imgENE2)
        moveni3()

        def moveni4():
            canvas2.move(enemi4,-10,0)
            ventanaN2.after(300, moveni4)
            ebb4 = canvas2.bbox(enemi4)
            if ebb4[0] < 0:
                return canvas2.delete(enemi4)
        enemi4 = canvas2.create_image(800, 370, image=imgENE2)
        moveni4()

        def moveni5():
            canvas2.move(enemi5,-10,0)
            ventanaN2.after(500, moveni5)
            ebb5 = canvas2.bbox(enemi5)
            if ebb5[0] < 0:
                return canvas2.delete(enemi5)
        enemi5 = canvas2.create_image(950, 420, image=imgENE2)
        moveni5()

        def moveni6():
            canvas2.move(enemi6,-10,0)
            ventanaN2.after(400, moveni6)
            ebb6 = canvas2.bbox(enemi6)
            if ebb6[0] < 0:
                return canvas2.delete(enemi6)
        enemi6 = canvas2.create_image(850, 370, image=imgENE2)

        def moveni7():
            canvas2.move(enemi7,-10,0)
            ventanaN2.after(600, moveni7)
            ebb7 = canvas2.bbox(enemi7)
            if ebb7[0] < 0:
                return canvas2.delete(enemi7)
        enemi7 = canvas2.create_image(600, 470,  image=imgENE2)
        moveni7()
        def moveni8():
            canvas2.move(enemi8,-10,0)
            ventanaN2.after(600, moveni8)
            ebb8 = canvas2.bbox(enemi8)
            if ebb8[0] < 0:
                return canvas2.delete(enemi8)
        enemi8 = canvas2.create_image(800, 120, image=imgENE2)
        moveni8()
        def moveni9():
            canvas2.move(enemi9,-10,0)
            ventanaN2.after(600, moveni9)
            ebb9 = canvas2.bbox(enemi9)
            if ebb9[0] < 0:
                return canvas2.delete(enemi9)
        enemi9 = canvas2.create_image(500, 370, anchor=NW, image=imgENE2)
        moveni9()



        """---------P A R T E   C O D I G O   D I S P A R A   Y   M U E V E   B A L A------"""
        def moverlabala2():
            global balame2
            ubi = canvas2.bbox(balame2)
            if ubi[3] < 700:
                canvas2.move(balame2, 10, 0)
            else:
                canvas2.delete(balame2)
            ventanaN2.after(60, moverlabala2)
        #FUNCIÓN QUE CREA LA BALA EN EL CENTRO DE LA NAVE Y LLAMA A LA FUNCIÓN MOVERLABALA()
        def shoot2(event):
            global balame2
            naveBoundd2 = canvas2.bbox(nave2)
            centrolado2 = (naveBoundd2[0] + naveBoundd2[2])/2
            centroancho2 = (naveBoundd2[1] + naveBoundd2[3])/2
            balame2 = canvas2.create_image(centrolado2, centroancho2, image=imgbalaj2)
            moverlabala2()
        #IMAGEN BALA JUGADOR
        imgbalaj2 = ImageTk.PhotoImage(Image.open("balame.png"))
        balame2 = canvas2.create_image(150,6, image= imgbalaj2)
        """----------------------------------------------------------------------------------"""
        #PARTE DONDE SE MUEVE LA IMAGEN DEL JUGADOR
        # IMAGEN NAVE NIVEL 2
        imgNave2 = ImageTk.PhotoImage(Image.open("nave3.png"))
        nave2 = canvas2.create_image(120, 2, anchor=NE, image=imgNave2)

        def nave2Borde(): #Establece los bordes de la nave
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
        """---0---0---W---W---W--W--W--W---C O L I S I O N E S   N I V E L 2---W---W---W----W---W---W----W---0---0"""
        def collisionnN21(): #ENEMIGO 1
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi1)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi1)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi1)

        def collisionnN22(): #ENEMIGO 2
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi2)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi2)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi2)

        def collisionnN23():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi3)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi3)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi3)

        def collisionnN24():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi4)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi4)
            # Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi4)

        def collisionnN25():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi5)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi5)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi5)

        def collisionnN26():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi6)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi6)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi6)

        def collisionnN27():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi7)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi7)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi7)

        def collisionnN28():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi8)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi8)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi8)

        def collisionnN29():
            sbb = canvas2.bbox(nave2)
            ebb = canvas2.bbox(enemi9)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas2.delete(enemi9)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas2.delete(enemi9)

        """-----------------------------C O D I G O   M U E V E   N A V E-------------------------"""
        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def move2Right(event):
            canvas2.move(nave2, 10, 0)
            nave2Borde(),collisionnN21(), collisionnN22(), collisionnN23(), collisionnN24(), collisionnN25()
            collisionnN26(), collisionnN27(), collisionnN28(), collisionnN29()


        def move2Left(event):
            canvas2.move(nave2, -10, 0)
            nave2Borde(),collisionnN21(), collisionnN22(), collisionnN23(), collisionnN24(), collisionnN25()
            collisionnN26(), collisionnN27(), collisionnN28(), collisionnN29()

        def move2Up(event):
            canvas2.move(nave2, 0, -10)
            nave2Borde(),collisionnN21(), collisionnN22(), collisionnN23(), collisionnN24(), collisionnN25()
            collisionnN26(), collisionnN27(), collisionnN28(), collisionnN29()

        def move2Down(event):
            canvas2.move(nave2, 0, 10)
            nave2Borde(),collisionnN21(), collisionnN22(), collisionnN23(), collisionnN24(), collisionnN25()
            collisionnN26(), collisionnN27(), collisionnN28(), collisionnN29()

        # Conexión de teclas con la nave
        canvas2.bind_all("<w>", move2Up)
        canvas2.bind_all("<s>", move2Down)
        canvas2.bind_all("<a>", move2Left)
        canvas2.bind_all("<d>", move2Right)
        canvas2.bind_all("<space>", shoot2)

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


        """-------------------------------------------------"""


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
        textosalien3 = Label(canvas3, text=aliens3, font=("Minecraft", 13), fg="white", bg="#270A4C")
        textosalien3.place(x=340, y=9)


        """--------------------------------------------------------"""


        #IMAGEN DE ENEMIGOS
        imagenemi3 = ImageTk.PhotoImage(Image.open("ALIEN3.png"))

        #VEFICIA QUE EL ENEMIGO ESTÉ DENTRO DEL CANVAS Y QUE SI TOCA EL EXTREMO IZQUIERDO, DESAPAREZCA
        def movef1():
            canvas3.move(enemy1, -10, 0)
            ventanaN3.after(600, movef1)
            ebb1 = canvas3.bbox(enemy1)
            if ebb1[0] < 0:
                return canvas3.delete(enemy1)
        enemy1 = canvas3.create_image(700,100, image=imagenemi3)
        movef1()

        #N A V E 2
        def movef2():
            canvas3.move(enemy2, -10, 0)
            ventanaN3.after(600, movef2)
            ebb2 = canvas3.bbox(enemy2)
            if ebb2[0] < 0:
                return canvas3.delete(enemy2)
        enemy2 = canvas3.create_image(900,170, image=imagenemi3)
        movef2()

        # N A V E 3
        def movef3():
            canvas3.move(enemy3, -10, 0)
            ventanaN3.after(600, movef3)
            ebb3 = canvas3.bbox(enemy3)
            if ebb3[0] < 0:
                return canvas3.delete(enemy3)
        enemy3 = canvas3.create_image(1200,190, image=imagenemi3)
        movef3()

        # N A V E 4
        def movef4():
            canvas3.move(enemy4, -10, 0)
            ventanaN3.after(600, movef4)
            ebb4 = canvas3.bbox(enemy4)
            if ebb4[0] < 0:
                return canvas3.delete(enemy4)
        enemy4 = canvas3.create_image(1500,250, image=imagenemi3)
        movef4()

        # N A V E 5
        def movef5():
            canvas3.move(enemy5, -10, 0)
            ventanaN3.after(600, movef5)
            ebb5 = canvas3.bbox(enemy5)
            if ebb5[0] < 0:
                return canvas3.delete(enemy5)
        enemy5 = canvas3.create_image(720,280, image=imagenemi3)
        movef5()

        # N A V E 6
        def movef6():
            canvas3.move(enemy6, -10, 0)
            ventanaN3.after(600, movef6)
            ebb6 = canvas3.bbox(enemy6)
            if ebb6[0] < 0:
                return canvas3.delete(enemy6)
        enemy6 = canvas3.create_image(640,200, image=imagenemi3)
        movef6()

        # N A V E 7
        def movef7():
            canvas3.move(enemy7, -10, 0)
            ventanaN3.after(600, movef7)
            ebb7 = canvas3.bbox(enemy7)
            if ebb7[0] < 0:
                return canvas3.delete(enemy7)
        enemy7 = canvas3.create_image(1200,350, image=imagenemi3)
        movef7()

        # N A V E 8
        def movef8():
            canvas3.move(enemy8, -10, 0)
            ventanaN3.after(600, movef8)
            ebb8 = canvas3.bbox(enemy8)
            if ebb8[0] < 0:
                return canvas3.delete(enemy8)
        enemy8 = canvas3.create_image(500,300, image=imagenemi3)
        movef8()

        # N A V E 9
        def movef9():
            canvas3.move(enemy9, -10, 0)
            ventanaN3.after(600, movef9)
            ebb9 = canvas3.bbox(enemy9)
            if ebb9[0] < 0:
                return canvas3.delete(enemy9)
        enemy9 = canvas3.create_image(1000,370, image=imagenemi3)
        movef9()

        # N A V E 10
        def movef10():
            canvas3.move(enemy10, -10, 0)
            ventanaN3.after(600, movef10)
            ebb10 = canvas3.bbox(enemy10)
            if ebb10[0] < 0:
                return canvas3.delete(enemy10)
        enemy10 = canvas3.create_image(1100,480, image=imagenemi3)
        movef10()

        # N A V E 11
        def movef11():
            canvas3.move(enemy11, -10, 0)
            ventanaN3.after(600, movef11)
            ebb11 = canvas3.bbox(enemy11)
            if ebb11[0] < 0:
                return canvas3.delete(enemy11)
        enemy11 = canvas3.create_image(420,500, image=imagenemi3)
        movef11()


        """------------------------------M O V I M I E N T O   D E   B A L A----------------------"""
        def moverlabala3():
            global balame3
            ubi = canvas3.bbox(balame3)
            if ubi[3] < 700:
                canvas3.move(balame3, 10, 0)
            else:
                canvas3.delete(balame3)
            ventanaN3.after(60, moverlabala3)
        #FUNCIÓN QUE CREA LA BALA EN EL CENTRO DE LA NAVE Y LLAMA A LA FUNCIÓN MOVERLABALA()
        def shoot3(event):
            global balame3
            naveBoundd3 = canvas3.bbox(nave3)
            centrolado3 = (naveBoundd3[0] + naveBoundd3[2])/2
            centroancho3 = (naveBoundd3[1] + naveBoundd3[3])/2
            balame3 = canvas3.create_image(centrolado3, centroancho3, image=imgbalaj3)
            moverlabala3()
        imgbalaj3 = ImageTk.PhotoImage(Image.open("balame.png"))


        """------------------------INICIO DE FUNCIONES DE NAVE Y ENEMIGOS-------------------------------"""
        # IMAGEN NAVE NIVEL 3
        imgNave3 = ImageTk.PhotoImage(Image.open("nave2.png"))
        nave3 = canvas3.create_image(200, 2, anchor=NE, image=imgNave3)
        def nave3Borde(): #ESTABLECE LOS BORDES DE LA IMAGEN
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


        """---------0---------0-------0--------C O L I S I O N E S-------0-------------0--------0----------0"""
        def collisionnN31():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy1)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy1)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy1)

        def collisionnN32():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy2)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy2)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy2)

        def collisionnN33():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy3)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy3)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy3)

        def collisionnN34():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy4)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy4)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy4)

        def collisionnN35():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy5)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy5)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy5)

        def collisionnN36():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy6)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy6)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy6)

        def collisionnN37():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy7)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy7)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy7)

        def collisionnN38():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy8)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy8)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy8)

        def collisionnN39():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy9)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy9)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy9)

        def collisionnN310():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy10)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy10)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy10)

        def collisionnN311():
            sbb = canvas3.bbox(nave3)
            ebb = canvas3.bbox(enemy11)
            # Si la nave toca el extremo izquierdo abajo o arriba del alien, que el alien se elimine
            if ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[1] < ebb[3] or ebb[0] < sbb[2] < ebb[2] and ebb[1] < sbb[3] < ebb[3]:
                return canvas3.delete(enemy11)
           #Si la nave toca el extremo derecho abajo o arriba de la nave, que el alien se elimine
            elif ebb[1] < sbb[3] < ebb[3] and ebb[0] < sbb[0] < ebb[2] or ebb[1] < sbb[1] < ebb[3] and ebb[0] < sbb[2] < ebb[3]:
                return canvas3.delete(enemy11)

        # CÓDIGO QUE MUEVE LA NAVE Y LLAMA NAVEBORDE() CADA QUE SE MUEVE
        def move3Right(event):
            canvas3.move(nave3, 10, 0)
            nave3Borde(), collisionnN31(), collisionnN32(), collisionnN33(), collisionnN34(), collisionnN35()
            collisionnN36(), collisionnN37(), collisionnN38(), collisionnN39(), collisionnN310(), collisionnN311()

        def move3Left(event):
            canvas3.move(nave3, -10, 0)
            nave3Borde(), collisionnN31(), collisionnN32(), collisionnN33(), collisionnN34(), collisionnN35()
            collisionnN36(), collisionnN37(), collisionnN38(), collisionnN39(), collisionnN310(), collisionnN311()
        def move3Up(event):
            canvas3.move(nave3, 0, -10)
            nave3Borde(), collisionnN31(), collisionnN32(), collisionnN33(), collisionnN34(), collisionnN35()
            collisionnN36(), collisionnN37(), collisionnN38(), collisionnN39(), collisionnN310(), collisionnN311()
        def move3Down(event):
            canvas3.move(nave3, 0, 10)
            nave3Borde(), collisionnN31(), collisionnN32(), collisionnN33(), collisionnN34(), collisionnN35()
            collisionnN36(), collisionnN37(), collisionnN38(), collisionnN39(), collisionnN310(), collisionnN311()
        # Conexión de teclas con la nave
        canvas3.bind_all("<w>", move3Up)
        canvas3.bind_all("<s>", move3Down)
        canvas3.bind_all("<a>", move3Left)
        canvas3.bind_all("<d>", move3Right)
        canvas3.bind_all("<space>", shoot3)
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