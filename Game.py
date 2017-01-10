'''Executes one move'''
def Game(Master,Player_lst,Turn,Rule_set):
    from Move import Move
    from Play import Play
    while True:
        m=Move(Master,Player_lst,Turn)                     #Client
        if Play(m,Master,Player_lst,Turn)==True:           #Checks wether move is valid
            break
    while True:
        Check()
        if Rules!=-1:
            if Rules=='+':          #can send back to Move()
                Applier('+')
            elif Rules=='0':
                Applier('0')
            elif Rules=='*':
                Applier('*')
            elif Rules=='1':         #Can't Play draws a card
                Applier('1')
