#should do all check ups with the master to avoid cheating, thus don't pass Hand from Game() to Play()
def Play(m,Master,Player_lst,Turn):
    from Message import Clear
    from CardMoves import Move_card
    Hand=Master[Player_lst[Turn]]
    if m==-1:
        m_card(Master,'Stack',0,Player_lst[Turn],0)
        print(Master)
        return True
    elif m not in range(len(Hand)):
        Clear()
        print('Please enter a valid Number\n')
        input('Press any button to continue')
        return False
    else:
        Move_card(Master,Player_lst[Turn],m,'Trash',0)
        print(Master)
        return True
