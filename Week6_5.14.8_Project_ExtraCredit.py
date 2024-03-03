import turtle

def color_bar(t, height):
    if (height >= 200):
        t.color("blue", "red")
    elif (height < 200) and (height >= 100):
        t.color("blue", "yellow")
    elif (height < 100):
        t.color("blue", "green")

    
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    color_bar(t, height)
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
