from re import A


class Solution:

    def values(self, value: str) -> int:
        if value == "I":
            return 1
        elif value == "V":
            return 5
        elif value == "X":
            return 10
        elif value == "L":
            return 50
        elif value == "C":
            return 100
        elif value == "D":
            return 500
        elif value == "M":
            return 1000
        else:
            return -10

    def romanToInt(self, s: str) -> int:
        i = 0
        Anser= 0

        while i < len(s):
            if i + 1 < len(s):
                value = self.values(s[i])
                value_next = self.values(s[i + 1])
                print(value, "\n", value_next)
                if value >= value_next:
                    number = value + value_next
                    Anser += number
                else:
                    number = value_next - value
                    Anser += number
            else:
                Anser += self.values(s[i])
            i += 2
        return Anser

rm = Solution()
ret = rm.romanToInt("MCM")
print(ret)
