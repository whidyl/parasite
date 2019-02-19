
def main():
    """
    Game Loop
    """
    #start story at first decision
    while running:
        print()
        story1.currentDecision.display()
        userInput = getInputFromUser()
        processUserInput(userInput, story1)

def getInputFromUser():
    userInput = input("Which option do you choose? ")
    return userInput

def processUserInput(userInput, story):
    # if a number, choose the corresonding action
    # get option number from user
    try:
        userOption = int(userInput)
    except:
        print("Invalid input... Try again.")
    
    if (userOption > 0) and (userOption <= (len(story1.currentDecision.options))):
        # if the option has an associated action, do it.
        if (story1.currentDecision.options[userOption - 1].action):
            story1.currentDecision.options[userOption - 1].action()
        story1.currentDecision = story1.currentDecision.options[userOption - 1].destination
        
        
    else:
        print(len(currentDecision.options))
        print("Not a valid option... Try again.")

class Character():
    def __init__(self, name):
        """Character class is used to represent the player aswell as NPCs"""
        self.name = name
        self.friends = []
        self.inventory = {}
        self.probabilityOfDeath = 0
        self.infected = False
        self.health = 3

class Option():
    def __init__(self, text, destination = None, action = None):
        """
        Represents a choice that the player is given.
        A decision object will usually hold a few different options.
        @param destination: the decision object which the option leads to.
        @param action: should be a function that contains a set of things that happen when the option is picked.
        @param active: if the option is active, it will be available to the player
        """
        self.text = text
        self.destination = destination
        self.action = action
        self.active = True

class Decision():
    def __init__(self, text = 'unset decision', options = []):
        self.text = text
        self.options = options
    def display(self):
        print(self.text)
        for optionNumber, option in enumerate(self.options):
            print("[" + str(optionNumber + 1) + ": " + option.text + "] ", end = '')
        print()

class StoryTree():
    def __init__(self):
        """ Initiate characters """
        self.player = Character(input("What's your name? "))
        NAME = self.player.name

        """ DECISION 1 - 1 : Where to? """
        self.decision1_1gowhere = Decision("Hello " + NAME + ", Where do you go first?")

        option1 = Option("The Gun Store")
        def option1action(player = self.player):
            player.inventory['Pistol'] = 1
            player.inventory['Pistol Bullets'] = 2
            player.inventory['Grenade'] = 1
        option1.action = option1action
        option2 = Option("The Hospital")
        self.decision1_1gowhere.options = [option1, option2]
        # current decision is initialized as 1-1
        self.currentDecision = self.decision1_1gowhere
        """ DECISION 2 - 1: The Gun Store """
        self.decision2_1gunstore = Decision("You hear movement and muffled talking from the floor above you. What do you do?")
        # d1-1-1 leads here
        self.decision1_1gowhere.options[0].destination = self.decision2_1gunstore

        option1 = Option("Exit hospital")
        option2 = Option("Continue searching quitely")
        option3 = Option("Go upstairs")
        self.decision2_1gunstore.options = [option1, option2, option3]

        """ DECISION 2 - 2: The Hospital """
        self.decision2_2hospital = Decision("You notice a locked safe on the floor. Glancing at the grenade you picked up, you get a bright idea.")
        # d1-1-2 leads here
        self.decision1_1gowhere.options[1].destination = self.decision2_2hospital

        option1 = Option("Keep grenade and dismiss safe")
        option2 = Option("Open safe with grenade")
        self.decision2_2hospital.options = [option1, option2]

running = True
story1 = StoryTree()
currentDecision = story1.decision1_1gowhere
main()
        


        

