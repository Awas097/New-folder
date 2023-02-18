from turtle import*

speed('fastest')
pencolor('red')

side = 5
for i in range(6):
    pensize(5)
    fd(50)
    for i in range(6):
        pensize(3)
        fd(25)
        fillcolor('yellow')
        begin_fill()
        for i in range(side-1):
            pensize(1)
            fd(25)
        for i in range(side):
            fd(10)
            rt(360/side)
        lt(360/side)
    end_fill()
    rt(360/side)
    lt(360/side)

hideturtle()
mainloop()