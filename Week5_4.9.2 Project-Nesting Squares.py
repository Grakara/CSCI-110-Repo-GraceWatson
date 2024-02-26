import turtle

def make_window(colr, ttle):        #make window funct
    """Set up the window with the given background color and title.
      Returns the new window.
    """
    w=turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):      #make turtles funct
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_square(t, sz):     #draw square funct
    for i in range(4):
        t.forward(sz)
        t.left(90)

def nest_square(t, sz, r):     #nest square funct
    for i in range(r):
        draw_square(t, sz + 20*i)
        t.penup()
        t.forward(-10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
      

wn= make_window("lightgreen", "4.9.2 Project: Nesting Squares") #window creation

torrah = make_turtle("hotpink", 5)          #turtle creation
torrah.shape("blank")
nest_square(torrah, 20, 5)


wn.mainloop()       #end program when window is closed
