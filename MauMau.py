#reading the config file:
from random import shuffle
from copy import copy

#Load functions
from Setup import Setup
from Game import Game
from Applier import Applier
from Win? import Win?
from End import End
from Reader import Reader


Reader()
while True:
    Setup()
    while Win==0:
        Game()
        Applier()       #Applies Rules just to Stack
        Win?()          #qick check of Master
    End()
