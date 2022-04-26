# Name: Clayton Vanfleet
# Course: CSE210-09
# Assignment: W02 Tick-Tac-Toe 

from turtle import *
import turtle

def main():

    tur = turtle.Turtle()
    scrn = turtle.Screen()
    scrn.setup(width=350, height=350)
    tur.speed(10)
    


    while True:

        size = input()

        if size == '3':
            threebythree(tur,scrn)
        elif size == '4x4':
            fourbyfour(tur,scrn)
        elif size == '5x5':
            fivebyfive(tur,scrn)
        elif size == '6x6':
            sixbysix(tur,scrn)
        print('Please input 3x3, 4x4, 5x5, or 6x6')
        pass

def threebythree(tur,scrn):

    #create grid
    tur.up()
    tur.goto(-50,150)
    tur.down()
    tur.left(270)
    tur.forward(300)

    tur.up()
    tur.goto(50,150)
    tur.down()
    tur.forward(300)

    tur.up()
    tur.goto(-150,50)
    tur.left(90)
    tur.down()
    tur.forward(300)

    tur.up()
    tur.goto(-150,-50)
    tur.down()
    tur.forward(300)

    tur.hideturtle()


    turtle.onscreenclick(getCoord)



def fourbyfour(tur,scrn):
    print('This is four by four')
def fivebyfive(tur,scrn):
    print('This is five by five')
def sixbysix(tur,scrn):
    print('This is six by six')

def o(x,y):
    turtle.goto(x,y-25)
    turtle.down()
    turtle.circle(25)

def ex(x,y):
    turtle.goto(x-17.5,y-17.5)
    turtle.down()

    turtle.left(45)
    turtle.forward(50)
    turtle.up()
    turtle.right(45)
    turtle.backward(35)
    turtle.right(45)
    turtle.down()
    turtle.forward(50)


def getCoord(x,y):

    grid = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

    turtle.up()
    turtle.hideturtle()
    print(x, y)

    if (x < -50) and (y > 50):
        grid[1] = 'o'
        o(x,y)
        print(grid)
    elif (50 > x > -50) and (y > 50):
        grid[2] = 'x'
        ex(x,y)
        print(grid)

    




if __name__ == '__main__':
    main()