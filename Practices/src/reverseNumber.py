"""Reverses a number between 10 and 10000"""
def reverseNumber(num):
    if type(num) == str:
        return "only integers are accepted"
    elif num < 10:
        return "Can only reverse number >= 10"
    else:
        if num < 100:
            rem = num % 10
            rev100 = rem * 10 + (num//10)
            return rev100
        elif num < 1000:
            rem0 = num % 100
            rem1 = rem0 % 10
            rev1 = rem1 * 10 + rem0//10

            finRev = rev1*10 + num//100
            return finRev
        elif num < 10000:
            rem = num%1000
            rem0 = rem % 100
            rem1 = rem0 % 10

            rev1 = rem1 * 10 + rem0//10

            RevR = rev1*10 + rem//100

            num4 = RevR * 10 + num//1000

            return num4
