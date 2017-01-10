'''Main Prog'''

#Load functions
from Reader import Reader
from Setup import Setup
from Game import Game
from Applier import Applier
from Win import Win
from End import End

Win=0
Rules=-1
Turn=0             #Whos Turn is it?

[Card_set,Players,Starting_Hand,Rule_set]=Reader()

while True:
    [Player_lst, Master]=Setup(Card_set,Players,Starting_Hand)
    while Win==0:
        [Master,Player_lst,Turn]=Game(Master,Player_lst,Turn,Rule_set)         #calls Applier
        Win()          #qick check of Master
    End()
