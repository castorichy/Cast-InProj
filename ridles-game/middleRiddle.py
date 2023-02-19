from baseModel import BaseModel
class MiddleRiddle(BaseModel):
   def playEasy(self):
      self.Instanciate_from_csv("middleRiddle.csv")

if __name__ == "__main__":
    MiddleRiddle()
