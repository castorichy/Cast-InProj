from baseModel import BaseModel

class HardRiddle(BaseModel):
   def playEasy(self):
      self.Instanciate_from_csv("hardRiddle.csv")


if __name__ == "__main__":
    HardRiddle()

