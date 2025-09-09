import turtle

def turtle_move():
    turtle.forward(50)
    turtle.stamp()

def up_move():
    turtle.setheading(90)
    turtle_move()
def left_move():
    turtle.setheading(180)
    turtle_move()
def down_move():
    turtle.setheading(270)
    turtle_move()
def right_move():
    turtle.setheading(0)
    turtle_move()
def restart():
    turtle.reset()


turtle.shape('turtle')
turtle.stamp()
turtle.onkey(up_move,'w')
turtle.onkey(left_move,'a')
turtle.onkey(down_move,'s')
turtle.onkey(right_move,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
turtle.mainloop()