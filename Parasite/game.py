

def getInputFromUser():
    userInput = input("Which option to you choose? ")
    return userInput

running = True
while running:
    userInput = getInputFromUser()

class Player():
    def __init__(self, name):
        self.name = name
