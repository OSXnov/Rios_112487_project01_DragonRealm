import random
import time
from graphics import *
from button import Button


class DragonRealm():
    
    def __init__(self):
        self.win = GraphWin("Dragon Realm", 1000, 800)
        self.win.setBackground('light blue')

        self.txt = Text(Point(500, 210),'''Your are in a land full of dragons.
        In Front of you,
        you see two caves.In one cave,
        the dragon is friendly
        and will share his treasure with you.The other
        dragon
        is greedy and hungry,
        and will eat you on sight...''' )

        self.img = Image(Point(500, 220), "dialoguebox.gif")
        self.img.draw(self.win)

        self.txt.setSize(10)
        self.txt.setFace('helvetica')
        self.txt.draw(self.win)


        self.Continue = Button(self.win, Point(500, 400), 120, 50, "Continue")
        self.Continue.activate()
        
        while True:
            p = self.win.getMouse()
            if self.Continue.clicked(p):
                self.win.close()
                self.chooseCave()
                #self.checkCave()

        

    def chooseCave(self):
        self.win = GraphWin('Dragon Realm', 1000, 800)
        self.win.setBackground(color_rgb(62,32,17))
        
        #self.textEntry = Entry(Point(500, 650), 10)
        #self.textEntry.draw(self.win)
        #self.textEntry.getText()
        
        self.cave1 = Button(self.win, Point(200,400), 100,50, "cave 1")
        self.cave1.activate()

        self.cave2 = Button(self.win, Point(800,400), 100, 50, "cave 2")
        self.cave2.activate()

        

        self.img_cave1 = Image(Point(200, 220), "cave_entrance1.gif")
        self.img_cave1.draw(self.win)

        self.img_cave2 = Image(Point(800, 220), "cave_entrance1.gif")
        self.img_cave2.draw(self.win)

        self.img_dialogue = Image(Point(500, 600), "dialoguebox.gif")
        self.img_dialogue.draw(self.win)

        self.text = Text(Point(500, 600), '''Which cave will you go into? (1 or 2) 
        click the box''')
        self.text.draw(self.win)
        
        
        while True:
            p  = self.win.getMouse()
            if self.cave1.clicked(p):
                self.win.getMouse()
                self.win.close()
                self.checkCave()
                
               
            elif self.cave2.clicked(p):
                self.win.getMouse()
                self.win.close()
                self.checkCave()
                
                
    def checkCave(self):
        self.win = GraphWin('Dragon Realm', 1000, 800)
        self.win.setBackground(color_rgb(62,32,17))
        self.img = Image(Point(500, 100), "cave_entrance1.gif")
        self.img.draw(self.win)
        self.txt = Text(Point(500,300), 'You approach the cave...')
        self.txt.draw(self.win)
        time.sleep(2)

        self.txt1 = Text(Point(500,400), 'It is dark and spooky...')
        self.txt1.draw(self.win)
        time.sleep(2)

        self.txt2 = Text(Point(500,500), 'A large dragon jumps out in front of you! He opens his jaws and...')
        self.txt2.draw(self.win)
        time.sleep(2)

        self.p = [1,2]
        self.chosenCave = random.choice(self.p)
        

        if self.chosenCave == 1:
            self.txt3 = Text(Point(500,550), 'Give you his treasure!')
            self.txt3.setTextColor("yellow")
            self.cuteDragon = Image(Point(500, 650), "cute_dragon.gif")
            self.cuteDragon.draw(self.win)
            self.win.setBackground('light blue')
            self.txt3.draw(self.win)
        elif self.chosenCave == 2:
            self.txt4 = Text(Point(500,550), 'Goobles you down in one bite!!!!')
            self.BadDragon = Image(Point(500,650), "bad_dragon.gif")
            self.BadDragon.draw(self.win)
            self.win.setBackground('red')
            self.txt4.draw(self.win)

        self.Continue= Button(self.win,Point(500,700), 120,50, "Continue")
        self.Continue.activate()
        p = self.win.getMouse()
        while True:
            if self.Continue.clicked(p):
                self.win.getMouse()
                self.win.close()
                self.PlayAgain()

        
    def PlayAgain(self):
        self.win = GraphWin ('Dragon Realm', 500, 300)
        self.win.setBackground("light blue")
       
        self.playAgain = Button(self.win, Point(150,150), 120,50, "Play Again")
        self.playAgain.activate()

        self.Quit = Button(self.win, Point(350,150), 120, 50, "Quit")
        self.Quit.activate()


        p = self.win.getMouse()
        while True:
            if self.playAgain.clicked(p):
                self.win.close()
                self.__init__()
            elif self.Quit.clicked(p):
                self.win.close()
        
        





inter = DragonRealm()

        