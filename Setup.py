def Setup():
    Player_lst=[]
    Master={}
    print(Starting_Hand)
    for i in range(1,Players+1):
        a='Master["P{}"]=[]'.format(i)
        exec(a)
        Player_lst.append('P{}'.format(i))
    shuffle(Card_set)
    Master['Stack']=copy(Card_set)
    Master['Trash']=[]
    #creating Player list (Player_lst) and the master dictionary keeping track of all cards

    for i in range(Starting_Hand):
        for x in range(1,1+len(Player_lst)):
            a='Master["P{}"]=Master["P{}"]+[Master["Stack"][0]]'.format(x,x)
            exec(a)
            Master['Stack'].pop(0)


#setup done maybe in the future put this into a function with paramenter in the config file deciding wether to give the first card or not
#to change the order of players chagnge Player_lst
#finished
