# 6.Can you change the self-parameter inside a class to something else (say “harry”).
#Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:

    def __init__(slf, trainNo):   ## if we change self to self in this line
        slf.trainNo = trainNo      ## then we have to change this here also

    def book(harry, fro, to):      ##  here if we put harry instead of self nothing will be changed
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")