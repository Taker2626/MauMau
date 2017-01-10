#Load functions
from Reader import Reader
from Setup import Setup
from Game import Game
from Applier import Applier
from Win import Win
from End import End

Win=0
Rules=-1

Reader()
while True:
    Setup(Card_set)             #finished
    while Win==0:
        Game()         #calls Applier
        Win()          #qick check of Master
    End()
