'''Markup but not'''
def Clear():
    import os
    from sys import platform
    if platform == "win32":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X

def Card_display(Set):
    #in future cards should be translated adding a dictionary to the config file
    print('Type 0 for to select no card\n')
    a=''
    for i in range(len(Set)):
        a+='{}.'.format(i+1)+str(Set[i])+'\n'
    print(a)
