import pyglet

#nastavenie okna
import pyglet.gl
from pyglet import gl

sirka = 1000
vyska = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST = 200 #pixely za s

#palky
dlzka_plaky = 10
VYSKA_PALKY = 100
RYCHLOST_PALKY = RYCHLOST * 1.5

#hrubka prostrednej ciary
CIARA_HRUBKA = 20

#font
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#STAVOVE PREMMENNE
pozicia_palok = [vyska // 2, vyska//2]
pozicia_lopty = [0,0]
rychlost_lopty = [0,0]
stisktnute_klavesy = set()
skore = [0,0]

def vykresli_obdlznik(x1 ,y1 ,x2 ,y2):
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuholniku

def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT) # nastavi okno na cierno
    gl.glColor3f(1, 1, 1) # nastavenie farby biela

    vykresli_obdlznik(
        pozicia_lopty[0],
        pozicia_lopty[1],
        pozicia_lopty[0] + VELKOST_LOPTY,
        pozicia_lopty[1] + VELKOST_LOPTY,
    )


window = pyglet.window.Window(width=sirka,height=vyska)
window.push_handlers(
    on_draw=vykresli,
)

pyglet.app.run()





