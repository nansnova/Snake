#Trabajo de Semana TEC

#Código modificado por:

#Autor: Ricardo Rmz. Condado
#Autor: Nancy L. Garcia Jimenez

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""


from turtle import *
from random import randrange
from freegames import square, vector
import random


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colores = ['yellow','black','blue','magneta','orange']
serpienteCuerpo = random.choice(colores)
comidaSerpiente = random.choice(colores)

#Cambia los valores del vector
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#determina si se queda dentro del límite
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#funcion principal de movimiento
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, serpienteCuerpo)

    square(food.x, food.y, 9, 'comidaSerpiente')
    update()
    ontimer(move, 100)

def movesquare():
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    ontimer(movesquare, 4500)

#anima snake
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movesquare()
done()
