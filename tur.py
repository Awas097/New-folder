import turtle

tur = turtle.Turtle()
tur.speed(20)
tur.color("black", "orange")
tur.begin_fill()
 
for i in range(200):
    tur.forward(300)
    tur.left(170)
    for i in range(100):
        tur.fd(600)
        tur.lt(340)
 
tur.end_fill()
turtle.done()