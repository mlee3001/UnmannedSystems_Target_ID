from turtle import Screen, Turtle
import random
import copy
    
WIDTH = 500
HEIGHT = 400

# Initalize turtle and set speed
t = Turtle()
t.speed(0)

# Create a screen
screen = Screen()
screen.screensize(WIDTH, HEIGHT)

# List of colors
colors = ["white","black","red","blue","green","purple","brown","orange"]

# Draws a circle at x,y of radius r
def drawCircle(x,y,r):
    t.pu()
    t.goto(x,y-r) 
    t.pd()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# Draws a semi circle at x,y of radius r
def drawSemiCircle(x,y,r):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y-r) 
    t.pd()
    t.begin_fill()
    t.circle(r,180)
    t.left(90)
    t.forward(2*r)
    t.end_fill()

# Draws a quarter circle at x,y of radius r
def drawQuarterCircle(x,y,r):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y-r)
    t.pd()
    t.begin_fill()
    t.circle(r,90)
    t.left(90)
    t.forward(r)
    t.left(90)
    t.forward(r)
    t.end_fill()

# Draws a triangle at x,y with side length l
def drawTriangle(x,y,l):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.forward(l)
        t.left(120)
    t.end_fill()

# Draws a rectangle at x,y of side length l
def drawRectangle(x,y,l):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()

# Draws a pentagon at x,y of side length l
def drawPentagon(x,y,l):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    for i in range(5):
        t.forward(l)
        t.left(72)
    t.end_fill()

# Draws a star at x,y of side length l
def drawStar(x,y,l):
    angle = random.randint(0,359)
    t.left(angle)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    for i in range(5):
        t.forward(l/2)
        t.left(72)
        t.forward(l/2)
        t.right(180-36)
    t.end_fill()

# Draws a cross at x,y of side length l
def drawCross(x,y,l):
    pass


# Main Function
def main():
    # Creates 5 semi-circles of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        r = random.randint(30,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawSemiCircle(x,y,r)

    # Creates 5 circles of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        r = random.randint(30,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawCircle(x,y,r)

    # Creates 5 quarter-circles of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        r = random.randint(30,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawQuarterCircle(x,y,r)
    
    # Creates 5 triangles of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        l = random.randint(20,100)
        # picks random color
        c = copy.deepcopy(colors)
        col = random.choice(colors)
        t.fillcolor(col)
        drawTriangle(x,y,l)

    # Creates 5 rectangles of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        l = random.randint(20,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawRectangle(x,y,l)

    # Creates 5 pentagons of random color and size
    for i in range(5):
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        l = random.randint(20,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawPentagon(x,y,l)

    # Creates 5 stars of random color and size
    for i in range(5):
        
        x = random.randint(-250, 250)
        y = random.randint(-200,200)
        l = random.randint(20,100)
        # picks random color
        col = random.choice(colors)
        t.fillcolor(col)
        drawStar(x,y,l)
        

    t.ht()
    screen.exitonclick()

if __name__ == "__main__":
    main()