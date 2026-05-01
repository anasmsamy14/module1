import turtle


screen = turtle.Screen()
screen.setup(width=800, height=600)  
screen.bgcolor("lightblue")                

pen = turtle.Turtle()


for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()
