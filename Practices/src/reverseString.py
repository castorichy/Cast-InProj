""" reversing a string """
def reverseString(string):
    """ This function reverses a string provided and returnes reversed string
    Args:
        str: string to be reversed"""
    s = ""
    for leter in string:
        s = leter + s
    return s
