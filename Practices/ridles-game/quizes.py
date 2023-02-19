""" This module Contains All Quizess To Be Asked """

class BaseModel:
    __Points = 0
    __inst = 0
    __inst_1 = 30
    __inst_2 = 20
    __inst_3 = 10

    _count = 0

    def __init__(self) -> None:
        """def __init__(self, name: str, pin: str):
        assert len(pin) >= 4, f"Pin must be 4 characters long"
        assert type(pin) == str, "pin must be of a group of characters only"

        self.name = name
        self.pin = pin"""

        BaseModel._count += 1

    def checkAns(self, user_anser, sys_anser, No_repeted):
        if type(user_anser) != str and type(sys_anser) != str and type(No_repeted) != str:
            return "Anser or Number repeated must be af type int or str respectively"
        if No_repeted == 1:
            if user_anser == sys_anser:
                BaseModel.__Points += self.__inst_1
            else:
                return 1
        elif No_repeted == 2:
            if user_anser == sys_anser:
                BaseModel.__Points += self.__inst_2
            else:
                return 2
        elif No_repeted == 3:
            if user_anser == sys_anser:
                BaseModel.__Points += self.__inst_3
            else:
                print(f"Sorry You Lost\nThe anser is {sys_anser}")

    def getPoints(self):
        return self.__Points
