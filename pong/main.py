import math
import pyglet

window = pyglet.window.Window(width=1000,height=800)

def tik(t):
    #had.x = had.x + t * 200
    had.x = had.x + t * 20
    had.y = had.y + 20 * math.sin(had.x / 5)
    #had.rotation = 270

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    had.x = 150

obrazok = pyglet.image.load('sprites/snake.jpg')
had = pyglet.sprite.Sprite(obrazok)

def vykreslit():
    window.clear()
    had.draw()

obrazok2 = pyglet.image.load('sprites/had.png')

def zmen(t):
    had.image = obrazok2
    pyglet.clock.schedule_once(zmen_nazad, 3)


def zmen_nazad(t):
    had.image = obrazok
    pyglet.clock.schedule_once(zmen, 3)

pyglet.clock.schedule_once(zmen, 3)

def klik(x,y, tlacitko, mod,):
    had.x = x
    had.y = y
    print(x)
    print(y)


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykreslit,
    on_mouse_press =klik
)

pyglet.app.run()