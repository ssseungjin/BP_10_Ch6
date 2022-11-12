import turtle
t = turtle.Turtle()
t.shape("turtle")

count = 0
t.lt(30)
for i in range(7):
    t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30);
    t.rt(120); t.fd(30); t.fd(-30); t.lt(60); t.fd(-70); t.lt(60); 