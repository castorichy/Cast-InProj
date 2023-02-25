from re import A


class Solution:
    def values(self, value: str) -> int:
        if value == "I":
            return 1
        elif value == "IV":
            return 4
        elif value == "V":
            return 5
        elif value == "IX":
            return 9
        elif value == "X":
            return 10
        elif value == "XL":
            return 40
        elif value == "L":
            return 50
        elif value == "C":
            return 100
        elif value == "XC":
            return 90
        elif value == "D":
            return 500
        elif value == "CD":
            return 400
        elif value == "M":
            return 1000
        elif value == "CM":
            return 900
        else:
            return -1

    def romanToInt(self, s: str) -> int:
        i = 0
        anser = 0
        leng = len(s)
        s1 = 0
        s2 = 0

        while i < leng:
            if i + 1 < leng:
                if s[i] == "I":
                    s2 = self.values("I")
                    match s[i + 1]:
                        case "I":
                            s2 = s1
                            s2 += s1
                        case "V":
                            s2 = self.values("IV")
                        case "X":
                            s2= self.values("IX")
                        case other:
                            return -1
                if s[i] == "X":
                    s2 = self.values("X")
                    match s[i + 1]:
                        case "X":
                            s2 = s1
                            s2 += s1
                        case "L":
                            s2 = self.values("XL")
                        case "C":
                            s2= self.values("XC")
                        case other:
                            return -1
                if s[i] == "C":
                    s2 = self.values("C")
                    match s[i + 1]:
                        case "C":
                            s2 = s1
                            s2 += s1
                        case "D":
                            s2 = self.values("CD")
                        case "M":
                            s2= self.values("CM")
                        case other:
                            return -1
            else:
                s2 = self.values(s[i])


            i += 2

        anser = s2
        return anser


sl = Solution()
print(sl.romanToInt("II"))


