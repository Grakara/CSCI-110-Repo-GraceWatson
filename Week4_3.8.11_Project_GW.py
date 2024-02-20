import turtle
wn = turtle.Screen()                    #Window
wn.bgcolor("white")
wn.title("Five Pointed Star")

nein = turtle.Turtle()                  #Nein the turtle
nein.color("black")
nein.pensize(5)
nein.shape("blank")
nein.speed(15)

nein.penup()
nein.forward(-104.5)
nein.pendown()

for f in range(5):
    nein.forward(209)
    nein.right(144)
                                        #five lines to draw the star
wn.mainloop()
