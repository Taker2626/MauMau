'''Sets up a new Game by shuffeling cards and creating the Hands'''
def Setup(Card_set,Players,Starting_Hand):
    from random import shuffle
    from copy import copy

    Player_lst=[]
    Master={}

    for i in range(1,Players+1):
        a='Master["P{}"]=[]'.format(i)
        exec(a)
        Player_lst.append('P{}'.format(i))
    shuffle(Card_set)
    Master['Stack']=copy(Card_set)
    Master['Trash']=[]
    #creating Player list (Player_lst) and the master dictionary keeping track of all cards Keys: P1-PN, Stack Trash

    for i in range(Starting_Hand):
        for x in range(1,1+len(Player_lst)):
            a='Master["P{}"]=Master["P{}"]+[Master["Stack"][0]]'.format(x,x)
            exec(a)
            Master['Stack'].pop(0)

    return [Player_lst, Master]
#to change the order of players chagnge Player_lst
