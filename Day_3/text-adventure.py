weapon = False


def introScene():
    directions = ["left", "right", "backward"]
    print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward: ")
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            hauntedRoom()
        else:
            print("Please enter a valid option.")


def showShadowFigure():
    directions = ["right", "backward"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward: ")
        userInput = input()
        if userInput == "right":
            cameraScene()
        elif userInput == "left":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")


def cameraScene():
    directions = ["forward", "backward"]
    print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Option: forward/backward: ")
        userInput = input()
        if userInput == "forward":
            print("You made it! You have found an exit.")
            quit()
        elif userInput == "backward":
            showShadowFigure()
        else:
            print("Please enter valid options")


def hauntedRoom():
    directions = ["right", "left", "backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward: ")
        userInput = input()
        if userInput == "right":
            print(
                "Multiple goul-like creatures start emerging as you enter the room. You are killed.")
            quit()
        elif userInput == "left":
            print("You made it! You have found an exit.")
            quit()
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option")


def showSkeletons():
    directions = ["forward", "backward"]
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userInput = ""
    global weapon
    while userInput not in directions:
        print("Options: forward/backward/left: ")
        userInput = input()
        if userInput == "left":
            print(
                "You find that this door opens into a wall. You open some of the dry wall to discover a knife")
            weapon = True
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            strangeCreature()
        else:
            print("Please enter a valid option.")


def strangeCreature():
    actions = ["fight", "flee"]
    global weapon
    print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee: ")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print(
                    "You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("The goul-like creature has killed you.")
            quit()
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please enter a valid option")


if __name__ == "__main__":
    while True:
        print('''
             *                                        !
      _.---._       !                         |>>>
    .'       '.     |>>>   *                  |>>>     *
   /           \    |>>>                      |               !
  |             |   |                   *    /~\              |>>>  
  |             |  /~\        _             /~~~\             |>>>   *
   \           /  /~~~\    /\(")/\         /~~~~~\  *  _   _  |_   _   _
    '.       ,'  /~~~~~\  //\   /\\       /~~~~~~~\   | |_| |_| |_| |_| |
      !'---'`   /~~~~~~~\ `  `m`  `      /~~~~~~~~~\ [___________________]
      |>>>     /~~~~~~~~~\              /~~~~~~~~~~~\ |           _     |
      |>>>  !  U_U_U_U_U_U         __  U _ U U U U U U|         .'|'.   |
 *    |     |>>>\ \| |/ /      _  (OO)_.'/ \ | | / / /|         |oo=|   |
     /~\    |>>> |  _  |       \'._)   .'___________/ |         |_|_|   |
    /~~~\   |    |.'|'.|        '..-'._ `'._   _   |  |   _             |
   /~~~~~\ /~\   ||=OO||    *          '.__.'.'|'. |  | .'|'.           |
  /~~~~~~~\~~~\  ||_|_||                 |   |=+=| |  | |=+=|           |
 (XXXXXXXXX)~~~\ |     |         !       |   |_|_| |  | |_|_|           |
  |   _   |xxxxx)U_U_U_U_U_U_U   |>>>    |         |_ |                 |
  | .'|'. |[]  | \ \  | |  / /   |>>>    |     _   | \|    _________    |
  | |=+=| | _  |_ |         | _  |_   _  |_  .'|'. |  |   [_________]   |
  | |_|_| || |_| ||  .-.    || |_| |_| |_| | |OO=| |  __   |XXXXXXX|    |
  |   _   |       |  | |    |    %     %   | |_|_| |_(oo)  _\/\/\/\|    |
  | .'|'. |       |  |_|    |    |'._.'|   |       |   (_.'/ " " " |    |
  | |=+=|_|   __  |         |    |__|  |   |       |_.'-..'|       |    |
  | |_|_|\'._(oo) | _       |    |'. .'|   |.---.  |  |____|_______|____|
  |   _   `.    (_.'/   .-. |    \  '  /   ||   |  | /~~~~/=========\~~~
~"| .'|'_.'  _.'-..'    | | |     '._.'    ||_  |  |/~~~~/...........\~~
  | |=+'.__.'     |     |_| |          _   ||   |  |~^"^/_____________\~^
  | |_|_| |       |         |     _    )\  ||___|__|
  |       |_______|         |_____))_.'~~'.|    ~"^"
  |       |~^^"^~"|_________|~^~.'~~'.x  x :
  lc______|        "~"^"~~"^~  : x  x :~~_.'
  ~"^"~"^"                      `-~~-'"^"^"^^
                           ~^"~^"~^
        ''')
        print("Welcome to the Adventure Game!")
        print("As an avid traveller, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        introScene()
