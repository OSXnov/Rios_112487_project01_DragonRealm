import random
import time
from graphics import *


def displayIntro():
    win = GraphWin('Dragon Realm',1000, 800)
    win.setBackground('light blue')

    txt = Text(Point(500, 210), '''Your are in a land full of dragons.
    In Front of you,
    you see two caves.In one cave,
    the dragon is friendly
    and will share his treasure with you. The other
    dragon
    is greedy and hungry,
    and will eat you on sight...''')


    img = Image(Point(500, 220), "dialoguebox.gif")
    img.draw(win)
    
    txt.setSize(10)
    txt.setFace('helvetica')
    txt.draw(win)

    win.getMouse()
    win.close()


def chooseCave():
    win = GraphWin('Dragon Realm', 1000, 1000)
    win.setBackground(color_rgb(62,32,17))
    textEntry = Entry(Point(500,650), 10)
    textEntry.draw(win)
    text = textEntry.getText()

    img_cave1 = Image(Point(200,220), "cave_entrance1.gif")
    img_cave1.draw(win)

    img_cave2 = Image(Point(800,220), "cave_entrance1.gif")
    img_cave2.draw(win)

    img_dialogue = Image(Point(500,600), "dialogue.gif")
    img_dialogue.draw(win)
    

   
    text = Text(Point(500,600), '''which cave will you go into? (1 or 2)
    click the mouse when done
    entering text''')
    text.draw(win)
    #click the mouse to signal done entering text
    win.getMouse()
    
    win.close()
    return text
    
def checkCave(chosenCave):
    win = GraphWin('DragonRealm', 1000, 1000)
    win.setBackground(color_rgb(62,32,17))
    img = Image(Point(500,100), "cave_entrance1.gif")
    img.draw(win)
    txt = Text(Point(500,500), 'You approach the cave...')
    txt.draw(win)
    time.sleep(2)

    txt1 = Text(Point(500,550), 'It is dark and spooky...')
    txt1.draw(win)
    time.sleep(2)

    txt2 = Text(Point(500,600), 'A large dragon jumps out in front of you! He opens his jaws and...')
    txt2.draw(win)
    time.sleep(2)

    friendlyCave= random.randint(1,2)

    if chosenCave == str(friendlyCave):
        txt3 = Text(Point(500, 800), ' Gives you his treasure!')
        txt3.setTextColor("yellow")
        cuteDragon = Image(Point(500,700), "cute_dragon.gif")
        cuteDragon.draw(win)
        win.setBackground('light blue')
        txt3.draw(win)
    else:
        txt4 = Text(Point(500,800), 'Goobles you down in one bite!!!!')
        BadDragon = Image(Point(500,700), "bad_dragon.gif")
        BadDragon.draw(win)
        win.setBackground('red')
        txt4.draw(win)

    win.getMouse()
    win.close()


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
