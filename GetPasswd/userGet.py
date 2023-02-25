import getpass as gp
"""This module gets the the loged username from computer database"""

def GetUser():
    user = gp.getuser()
    print(user)

GetUser()
