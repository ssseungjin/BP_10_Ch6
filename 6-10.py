import turtle
t = turtle.Turtle()
t.shape("turtle")

count = 0

while True:
    t.fd(100); t.rt(90); t.fd(20); t.rt(90); t.fd(100); t.lt(90); t.fd(20);
    t.lt(90);

    count += 1

    if(count == 7):
        break;