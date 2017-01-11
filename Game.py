'''Executes one move'''
def Game(Master,Player_lst,Turn,Rule_set):
    from Check import Check
    from Move import Move
    from Play import Play
    while True:
        m=Move(Master,Player_lst,Turn)                     #Client
        if Play(m,Master,Player_lst,Turn)==True:           #Checks wether move is valid
            break
    while True:
        Rules=Check(Master,Rule_set)
            if Rules!=-1:
                if '+'in Rules:          #can send back to Move()
                    Applier('+')
                elif '0' in Rules:
                    Applier('0')
                elif '*' in Rules:
                    Applier('*')
                elif '1' in Rules:         #Can't Play draws a card
                    Applier('1')
            elif Rules==-1:
                return
