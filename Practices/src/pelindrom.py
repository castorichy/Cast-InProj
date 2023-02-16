""" A module to check if a string is a pelindrom """

def pelindrom(string):
    """This function reverses a string and check if its a pelindrome"""
    strRev = ""
    if type(string) != str:
        print("Only strings are accepted")
        exit()
    else:
        for ch in string:
            if ch == " ":
                print("Only A word can be check if its a pelindrom")
                strRev = None
                exit()
            else:
                strRev = ch + strRev
    if strRev == string:
        print(f"{string} is a pelindrom")
    else:
        print(f"{string} is not a pelindrom")
