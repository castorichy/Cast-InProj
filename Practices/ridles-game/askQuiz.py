from re import A, T
from quizes import BaseModel
import csv
""" This modules creates user input and output by asking Guastions to the user """

class AskQuize(BaseModel):

    def __Instanciate_from_csv(self):
        with open("quize.csv", "r") as fd:
            items = list(csv.DictReader(fd))

            return items

    def EasyQuastions(self):
        i = 1
       # j: int = 0
        items_list = self.__Instanciate_from_csv()
        for item in items_list:
            while i <= 3:
                user_anser = input("{} ".format(item.get("Quize")))
                sys_a = item.get("anser")
                sys_anser = sys_a.split('"')
                ret = self.checkAns(user_anser, sys_anser[1], i)
                print(type(user_anser))

                if ret == None:
                    i = 1
                    break
                i += 1



