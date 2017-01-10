'''Lets a player make a move'''
def Move(Master,Player_lst,Turn):
    from copy import copy
    from Message import Clear,Card_display

    Hand=Master[Player_lst[Turn]]

    Clear()

    print('Your current hand:\n')
    Card_display(Hand)

    if len(Master['Trash'])!=0:
        Top=Master['Trash'][-1]
        print('Current Top card:\n')
        print(Top)
    else:
        Top=0
        print('Play any card, you go ahead and start <3')
    Playable=[]
    for i in Hand:
        if Top==0:
            Playable=copy(Hand)
        elif i[0] == Top[0] or i[1] == Top[1] or i[3]=='*':
            Playable.append(i)

    if len(Playable)>0:
        print('You can play the following cards:\n')
        Card_display(Playable)
        return (int(input('Which card would you like to play?: '))-1)

        #checked and working
    else:
        print('Oh dear you will have to draw a card.')
        return -1
        #checked and working
