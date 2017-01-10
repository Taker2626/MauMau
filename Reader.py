'''Reads out config file'''
def Reader():
    Card_set=[]
    Rule_set=[]

    with open('MauMau.config') as A:
        Config=A.readlines()
    for i in range(len(Config)):
        if Config[i]=='//\n':
            if Config[i+1]=='General:\n':
                x=2
                while True:
                    if Config[x+i]!='\\\\\n':
                        if Config[x+i]=='Starting_Hand:\n':
                            Starting_Hand=int(Config[x+i+1].rstrip('\n'))
                            x+=2
                        if Config[x+i]=='Players:\n':
                            Players=int(Config[x+i+1].rstrip('\n'))
                            x+=2
                    else:
                        break
            elif Config[i+1]=='Card_set:\n':
                x=2
                while True:
                    if Config[x+i]!='\\\\\n':
                        Card_set.append(Config[x+i].rstrip('\n').split(','))
                        x+=1
                    else:
                        break
            elif Config[i+1]=='Rule_set:\n':
                x=2
                while True:
                    if Config[x+i]!='\\\\\n':
                        Rule_set.append(Config[x+i].rstrip('\n').split(':'))
                        x+=1
                    else:
                        break
    #finished
    return [Card_set,Players,Starting_Hand,Rule_set]
