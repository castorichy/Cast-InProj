class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x > 2**31:
            return False
        x_str = str(x)
        rev = ""
        for i in x_str:
            rev = i + rev
        if int(rev) == x:
            return True
        else:
            return False
