from baseModel import BaseModel

class EasyRidles(BaseModel):
   def playEasy(self):
      self.Instanciate_from_csv("easyRiddle.csv")

if __name__ == "__main__":
   EasyRidles()
