import csv
import json
from baseModel import BaseModel

""" This module Contains All Quizess To Be Asked """

class User(BaseModel):
    userDetDict = {}

    def __login(self):
        print("\n\tLog in to Your Account")
        print("*"*50)
        i = 0
        count = 3
        while i < count:
            logName = input("Name: ")
            logPasswd = input("Password: ")

            with open("userDetails.json", "r") as fd:
                loadUserDet = json.load(fd)
                if loadUserDet["UserName"] == logName and loadUserDet["Password"] == logPasswd:
                    self.__dispay()
                    break
                else:
                    print("User Name or Password is not Valid\nPlease Re-try:")

            i += 1


    def __signup(self):
        userName = input("Enter Your Name: ")
        Passwd = input("Enter Your Password: ")
        conf_passwd = input("Confirm Password: ")
        if Passwd == conf_passwd:
            ret = self.__check_existence(userName)
            if ret == 0:
                self.userDetDict.update({"UserName": userName, "Password": Passwd})
                self.__save_to_jason()
                self.__login()
        else:
            print("Password Didn't match Please Re-try")
            self.__signup()


    def __check_existence(self, username):
        try:
            with open("userDetails.json", "r") as fd:
                loadUserDet = json.load(fd)
                for key in loadUserDet.keys():
                    if loadUserDet[key] == username:
                        print("user name Exist")
                        return 0
        except FileNotFoundError:
            return 0

    def __save_to_jason(self):
        with open("userDetails.json", "w") as fd:
            json.dump(self.userDetDict, fd)

    def userDetails(self):
        choice = int(input("""\
                    CASTO RIDDLE PROGRAM
                    --------------------
    Test Your Mental Mettle With These Ridiculous Riddle
    -----------------------------------------------------
    First You need to sign up or Login to access your account;
    1. Login
    2. Sign up
    3. Quit
    >>> """))

        match choice:
            case 1:
                self.__login()
            case 2:
                self.__signup()
            case 3:
                exit()
            case other:
                print("Invalid Choice")

    def __dispay(self):
        from easyRiddle import EasyRidles
        from middleRiddle import MiddleRiddle
        from hardRiddle import HardRiddle

        choice = int(input("""\
                    CASTO RIDDLE PROGRAM
                    --------------------
    Test Your Mental Mettle With These Ridiculous Riddle
    -----------------------------------------------------
    1. Easy Ridles
    2. Midd leRiddle
    3. Hard RIddles
    4. View Points
    5. Quit
    >>> """))
        match choice:
            case 1:
                easy = EasyRidles()
                easy.playEasy()
            case 2:
                middle = MiddleRiddle()
                middle.playEasy()
            case 3:
                hard = HardRiddle()
                hard.playEasy()
            case 4:
                print(f"Total Points: {self.getPoints()}")
            case 5:
                quit()
            case other:
                print("Invalid Choice To Play")
