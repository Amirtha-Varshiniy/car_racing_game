import turtle
track=turtle.Screen()
redc=turtle.Turtle()
bluec=turtle.Turtle()
track.bgpic("track.gif")
track.addshape("blue_car.gif")
track.addshape("red_car.gif")
redc.shape("red_car.gif")
bluec.shape("blue_car.gif")
redc.setheading(90)
redc.penup()
redc.goto(-100,-240)
bluec.setheading(90)
bluec.penup()
bluec.goto(100,-240)
redc.speed(2000)
bluec.speed(2000)

def Bplayer():
    bluec.forward(5)
def Rplayer():
    redc.forward(5)
turtle.onkeypress(Bplayer,"Up")
turtle.onkeypress(Rplayer,"z")
turtle.listen()

while True:
    track.update()
    if bluec.pos()>(100,200):
        track.bgpic("Bwin.gif")
        break
    elif redc.pos()>(-100,200):
        track.bgpic("Rwin.gif")
        break
turtle.done()