# Name: Clayton Vanfleet
# Course: CSE210-09
# Assignment: W02 Tick-Tac-Toe 

from turtle import *
import turtle as t
grid = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
turn = 'x'
t.pensize(5)
scrn = t.Screen()
scrn.setup(width=350, height=350)
t.speed(10)
t.pensize(5)
t.hideturtle()
t.Screen().bgcolor('lightgray')

def play():

    #create grid
    t.color('black')

    t.up()
    t.goto(-50,150)
    t.down()
    t.left(270)
    t.forward(300)

    t.up()
    t.goto(50,150)
    t.down()
    t.forward(300)

    t.up()
    t.goto(-150,50)
    t.left(90)
    t.down()
    t.forward(300)

    t.up()
    t.goto(-150,-50)
    t.down()
    t.forward(300)

    t.hideturtle()



    t.onscreenclick(getCoord)
    t.mainloop()


def calculateWin(turn):
    
    if (grid[1] == turn) and (grid[2] == turn) and (grid[3] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[1] == turn) and (grid[4] == turn) and (grid[7] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[1] == turn) and (grid[5] == turn) and (grid[9] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[2] == turn) and (grid[5] == turn) and (grid[8] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[3] == turn) and (grid[5] == turn) and (grid[7] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[4] == turn) and (grid[5] == turn) and (grid[6] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[7] == turn) and (grid[8] == turn) and (grid[9] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif (grid[3] == turn) and (grid[6] == turn) and (grid[9] == turn):
        again = t.textinput(f"The {turn}'s win!!",'Do you want to play again? (y/n) ')
        if again == 'y':
            t.clear()
            main()
        print('Thanks for playing! Bye!')
    elif None not in (grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8],grid[9]):
        again = t.textinput("Its a draw!", "Do you want to play again? (y,n) ")
        if again == 'y':
            t.clear()
            main()
    else:
        pass


def o(x,y):
    
    t.color('blue')
    t.goto(x,y-25)
    t.down()
    t.circle(25)
    t.update() 

def ex(x,y):
    t.color('red')
    t.goto(x-17.5,y-17.5)
    t.down()

    t.left(45)
    t.forward(50)
    t.up()
    t.right(45)
    t.backward(35)
    t.right(45)
    t.down()
    t.forward(50)

                                #reset turtles direction
    t.right(45)
    t.left(45)
    t.left(45)

def getCoord(x,y):
    
    t.up()

    global turn
    

    if (x < -50) and (y > 50):
        if grid[1] == None:
            if turn == 'x':
                grid[1] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[1] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
    elif (50 > x > -50) and (y > 50):
        if grid[2] == None:
            if turn == 'x':
                grid[2] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[2] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
    elif (x>50) and (y>50):
        if grid[3] == None:
            if turn == 'x':
                grid[3] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[3] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')

    elif (x < -50) and (50 > y > -50):
        if grid[4] == None:
            if turn == 'x':
                grid[4] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[4] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
    
    elif (-50 < x < 50) and (50 > y > -50):
        if grid[5] == None:
            if turn == 'x':
                grid[5] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[5] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else: 
            print('Please choose an empty slot.')
            
    elif (x > 50) and (50 > y > -50):
        if grid[6] == None:
            if turn == 'x':
                grid[6] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[6] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
    elif (x < -50) and (-50 > y):
        if grid[7] == None:
            if turn == 'x':
                grid[7] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[7] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
    elif (50 > x > -50) and (y < -50):
        if grid[8] == None:
            if turn == 'x':
                grid[8] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[8] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
    elif (x > 50) and (y < -50):
        if grid[9] == None:
            if turn == 'x':
                grid[9] = turn
                ex(x,y)
                calculateWin(turn)
                turn = 'o'
            elif turn == 'o':
                grid[9] = turn
                o(x,y)
                calculateWin(turn)
                turn = 'x'
        else:
            print('Please choose an empty slot.')
            
            
    


def main():

    t.clear()

    global grid

    grid = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}


    ready = t.textinput('Tic-tac-toe',"Welcome to tic-tac-toe, the x's will go first! Are you ready to play? (y/n) ")


    if ready == 'y':
        play()
    print('Okay, bye!')
       



if __name__ == '__main__':
    main()