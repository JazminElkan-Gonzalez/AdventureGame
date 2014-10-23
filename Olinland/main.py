
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *
from hunter import *
from ninja import *
from butterfly import *
from teleporter import *

REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():
    mh353 = Room('Riccardo-Office', "Riccardo's office is on the 3rd floor of Milas Hall. ")
    mh3rd = Room('Milas-Hall-Third-Floor', "There are many professor's offices here")
    mh2nd = Room('Milas-Hall-Second-Floor', "There are musical instruments and rooms to offices.")
    mh1st = Room('Milas-Hall-First-Floor', "There is a grand set of stairs.")
    oval = Room('Oval', "Smack in the center of Olin College.")
    dhall = Room('Dining-Hall', "Om nom nom.")
    ac1st = Room('Academic-Center-First-Floor', "Where dreams go to die.")
    ac113 = Room('Academic-Center-113', "The best class ever is taught here.")
    cc1st = Room('Campus-Center-First-Floor', "Contains the dining hall and nothing else of relevance.")
    westh = Room('West-Hall', "Only children live here. Why go here?")
    easth1 = Room('East-Hall-1', "What's that smell...")
    easth2 = Room('East-Hall-2', "Much color. Very art. Wow.")
    easth3 = Room('East-Hall-3', "Home sweet home.")
    easth4 = Room('East-Hall-4', "Too many stairs.")
    babson = Room('Babson-College', "Bro.")

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  westh)
    biconnect(cc1st, 'north', dhall)
    biconnect(westh, 'east',  easth1)
    biconnect(easth1, 'up', easth2)
    biconnect(easth2, 'up', easth3)
    biconnect(easth3, 'up', easth4)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval, "You're a Blubbering-Fool")

    # Radar('handy radar',mh353, "A nifty wifty little dood-dah.") 
    Radar('handy radar',oval, "A nifty wifty little dood-dah.") 
    Teleporter('Telepro!', ac113, "Olin Corp's Solution to all yopur telporting needs!!!") 


    Thing('blackboard', ac113, "Singing in the dead of the night.")
    Thing('lovely-trees', oval, "You must be seeing things.")
    Thing('grass', oval, "Not removable.")
    MobileThing('muffin', easth1, "What is in this mysterious package of nom?")
    MobileThing('cell-phone', easth3, "Won't work at Olin anyway.")
    MobileThing('map', dhall, "Really? This map is irrelevant. Olin is too small.")
    MobileThing('bean-bag', easth4, "Bean-y.")
    MobileThing('cs-book', oval, "Book of wonders.")
    MobileThing('math-book', oval, "Book of death.")

    Computer('hal-9000', ac113, "It's friendly voice fills you with feelings of uncertainty.")
    Computer('johnny-5', easth1, "Johnny-5 is alive.")

    Professor('Riccardo',mh353,random.randint(1,5),2, "Awesomesauce.")
    TrollHunter('Storm-Bringer', oval, random.randint(1,5), 1, "Destroyer of Souls.")
    TrollHunter('Melvin', westh, random.randint(1,5), 100, "Is..Is that a freshmen?")
    BadNinja('Trogdor', oval, random.randint(1,5), "The Burninator.")
    Butterfly('FlipFlap', oval, random.randint(1,2), "Eater of worlds. A caterpillar.")

    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']

    hwNumOld = 0
    hwNum = 1
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms), "Distress level = " + str(hwNum + hwNumOld))
        hwNumOld = hwNum
        hwNum = hwNum + hwNumOld        
    Homework("done-hw-7", oval, "this shit is done yo")
    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    studentDescriptions = ['He will always be a Freshman.',
                           'Pretty sure his mother is a kangaroo.',
                           'An actual person at Olin!',
                           "Hopefully he won't die in the tournament!"]

    for i in range(len(students)):
        NPC(students[i],
            random.choice(Room.rooms),
            random.randint(1,5),
            random.randint(1,5),
            studentDescriptions[i])

    trolls = ['Polyphemus',
              'Gollum']
    trollDescriptions = ['Might be Greek.',
                         'Kid needs a bath.']

    for j in range(len(trolls)):
        Troll(trolls[j],
            random.choice(Room.rooms),
            random.randint(1,3),
            random.randint(1,3),
            trollDescriptions[j])



VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'peek' : Peek(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()
    
    Player.me.look_around()
    Player.clock.register(print_tick_action, 1)
    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.clock.tick()
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
