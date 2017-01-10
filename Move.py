'''Lets a player make a move'''
def Move(Master,Player_lst,Turn):
    from Message import Clear

    Hand=Master[Player_lst[Turn]]

    Clear()
    print('Your current hand:\n')
    print(Hand)

    if len(Master['Trash'])!=0:
        Top=Master['Trash'][-1]
    else:
        print('Play any card, you go ahead and start <3')
        Top=0

    
