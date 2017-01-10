'''Markup but not'''
def Clear():
    import os
    from sys import platform
    if platform == "win32":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X
