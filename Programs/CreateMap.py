from Vertex import Vertex
from Algorithm import a_star
import time

#Init vertex
arthur = Vertex("Arthur's House",1,6)
jared = Vertex("Jared's House",1,7)
trade = Vertex("Trade Post",1,4)
general = Vertex("General Store",3,4)
dutch = Vertex("Dutch's House",3,6)
tom = Vertex("Tom's House",3,7)
sheriffs = Vertex("Sheriff's Office",4,6)
cornwall = Vertex("Leviticus Cornwall Estate",5,1)
bank = Vertex("Town Bank",5,4)
courtyard = Vertex("Courtyard",5,6)
stable = Vertex("Horse Stable",5,7)
hall = Vertex("Town Hall",6,4)
office = Vertex("Post Office",6,8)
army = Vertex("Army Recruitment",7,3)
micah = Vertex("Micah's House",7,4)
saloon = Vertex("Saloon",7,6)
grave = Vertex("Graveyard",7,7)
hotel = Vertex("Hotel",7,6)
ranch = Vertex("Emerald Ranch",9,5)

#Graph dictionary
rivendale_graph = {
  arthur: set([(trade,2),(dutch,2),(jared,1)]),
  jared: set([(arthur,1),(tom,2)]),
  trade: set([(arthur,2),(general,2),(cornwall,7)]),
  general: set([(trade,2),(dutch,2),(bank,3)]),
  dutch: set([(tom,1),(arthur,2),(general,2)]),
  tom: set([(jared,2),(dutch,1)]),
  sheriffs: set([(dutch,1),(courtyard,1)]),
  cornwall: set([(trade,7),(army,4)]),
  bank: set([(courtyard,2),(hall,1)]),
  courtyard: set([(bank,2),(saloon,2),(stable,2)]),
  stable: set([(courtyard,2),(office,1),(grave,2)]),
  hall: set([(bank,1),(micah,2)]),
  office: set([(stable,1),(grave,1)]),
  army: set([(cornwall,4),(micah,1)]),
  micah: set([(hall,2),(army,1),(saloon,2),(ranch,2)]),
  saloon: set([(grave,1),(courtyard,2),(hotel,1),(micah,2)]),
  grave: set([(office,1),(stable,2),(saloon,1)]),
  hotel: set([(saloon,1),(ranch,1)]),
  ranch: set([(micah,2),(hotel,1)])
}


def check(num):
    for number in list(range(19)):
        if int(num) == number:
            return True
    return False   

def navigate():
    buildings = (arthur,jared,trade,general,dutch,tom,sheriffs,cornwall,bank,courtyard,
                 stable,hall,office,army,micah,saloon,grave,hotel,ranch)
    ui1 = input("Where are you currently? ")
    if not check(ui1):
        print("Wrong input... restarting navigation process")
        time.sleep(0.5)
        navigate()
    else:  
        ui2 = input("Where are you headed? ")
        if not check(ui2):
            print("Wrong input... restarting navigation process")
            time.sleep(0.5)
            navigate()  
        else:               
            a_star(rivendale_graph,buildings[int(ui1)-1],buildings[int(ui2)-1])

def start():
    print("Welcome to Rivendale!\n")
    time.sleep(0.5)
    print("Buildings: ")
    print("1 - Arthur's House, 2- Jared's House, 3- Trade Post, 4 - General Store,")
    print("5 - Dutch's House, 6 - Tom's House, 7 - Sheriff's Office, 8 - Leviticus Cornwall Estate,")
    print("9 - Town Bank, 10 - Courtyard, 11 - Horse Stable, 12 - Town Hall,")
    print("13 - Post Office, 14 - Army Recruitment, 15 - Micah's House, 16 - Saloon")
    print("17 - Graveyard, 18 - Hotel, 19 - Emerald Ranch")
    time.sleep(0.5)
    print("")
    print("Please enter a building's numbers below for each of the questions asked:")
    navigate()

start()