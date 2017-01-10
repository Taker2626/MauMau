def Game():
    global Rules
    while True:
        Move()                     #Client
        if Play()==True:           #Checks wether move is valid
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
