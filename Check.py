'''Checks wether rules have to be applied'''
def Check(Master,Rule_set):
    Trash=Master['Trash']
    for i in Rule_set:
        if Trash[0][0]==i[0]:
            Rule=i[1].split(',')

        elif i[0]=='':
            return -1
