import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
TITLE = "Increasing rects"

def draw ():
    screen.clear()
    

    width = WIDTH
    height = HEIGHT-200

    for i in range(11):
        r = randint(1,255)
        g = randint(1,255)
        b = randint(1,255)

        box = Rect((0,0),(width,height))
        box.center = 200,200
        screen.draw.rect(box,(r,g,b))
        width = width - 10
        height = height + 10

pgzrun.go()