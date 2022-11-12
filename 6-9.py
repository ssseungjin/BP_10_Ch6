import random
import turtle
t = turtle.Turtle()
t.shape("turtle")


for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(-180, 180)

    t.up()
    t.goto(x, y)
    t.down()
    t.circle(z);