import turtle 
turtle.Screen().bgcolor("green")
turtle.Screen().setup(700,800)
t=turtle.Turtle()
t.speed(2)
sides=6
lengh= 80
angle=360.0/sides
for i in range(sides):
    t.forward(lengh)
    t.right(angle)
turtle.done()