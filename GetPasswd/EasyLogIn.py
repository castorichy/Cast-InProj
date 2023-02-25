import getpass as gp
"""This module hides password Prompts echoes"""

def easyLog():
    try:
        paswd = gp.getpass(stream=None)
    except Exception as Error:
        print("Error: ", Error)
    else:
        print("Password Entered = ", paswd)

easyLog()
