'''Reads out config file'''
def Reader():
    Card_set=[]
    Rule_set=[]
    #Set a sensible default value
    Starting_Hand=1
    Players=5
    
    with open('MauMau.config') as A:
        lines=A.readlines()
        Config=Strip(lines)
    for i in range(len(Config)):
        if Config[i]=='//':
            if Config[i+1]=='General:':
                x=2
                while True:
                    if Config[x+i]!='\\\\':
                        if Config[x+i]=='Starting_Hand:':
                            Starting_Hand=int(Config[x+i+1])
                            x+=2
                        if Config[x+i]=='Players:':
                            Players=int(Config[x+i+1])
                            x+=2
                    else:
                        break
            elif Config[i+1]=='Card_set:':
                x=2
                while True:
                    if Config[x+i]!='\\\\':
                        Card_set.append(Config[x+i].split(','))
                        x+=1
                    else:
                        break
            elif Config[i+1]=='Rule_set:':
                x=2
                while True:
                    if Config[x+i]!='\\\\':
                        Rule_set.append(Config[x+i].split(':'))
                        x+=1
                    else:
                        break
    #finished
    return [Card_set,Players,Starting_Hand,Rule_set]

def StripLine(line):
    if line[0]==' ' or line[0]=='\t':          #ignore leading Whitespace characters
        return Strip(line[1:])
    elif line[0]=='*':                         #ignore Comments
        return ('')
    elif line[-1]=='\n':
        return (line[:-1])                 #kill the \n
    else:
        return (line)

def Strip(lines):
    res=[]
    for line in lines:
        res_line=StripLine(line)
        if res_line!='':
            res.append(res_line)
    return res
