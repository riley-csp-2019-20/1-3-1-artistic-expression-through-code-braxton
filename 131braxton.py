import turtle as trtl

#turtles used
Tic = trtl.Turtle()
Tac = trtl.Turtle()
Cross = trtl.Turtle()
circle = trtl.Turtle()

#modifications
Tic.speed(0.5)
Tac.speed(0.5)
Tic.pensize(10)
Tac.pensize(10)
Cross.shape = ("circle")

#drawing the VERTICLE LINES
Tic.penup()
Tic.goto(-200,150)
Tic.pendown()
Tic.left(90)
Tic.backward(500)
Tic.forward(800)
Tic.penup()
Tac.penup()
Tac.goto(200,150)
Tac.pendown()
Tac.left(90)
Tac.backward(500)
Tac.forward(800)
Tac.penup()


#DRAWING THE HORIZONTAL LINES
Tic.goto(200,150)
Tic.pendown()
Tic.right(90)
Tic.forward(200)
Tic.backward(800)
Tac.goto(200,-125)
Tac.pendown()
Tac.right(90)
Tac.forward(200)
Tac.backward(800)

Cross.shape
Cross.goto(0,0)
Cross.ht()







def W():
    Cross.ht()













wn = trtl.Screen()


#player 2 controll
wn.onkeypress(W,"W")
wn.onkeypress(8,"8")
wn.onkeypress(9,"9")
wn.onkeypress(4,"4")
wn.onkeypress(5,"5")
wn.onkeypress(6,"6")
wn.onkeypress(3,"3")
wn.onkeypress(2,"2")
wn.onkeypress(1,"1")









wn.mainloop()
