import random as r
import Classes 

#Constants 
HERO_STATS = [10.0, 3.0, 3.0]  # hp/atk/def
TROLL_STATS = [4.0, 2.0, 4.0]  # hp/atk/def
UNDERLING_STATS = [3.0, 1.0, 1.0]  # hp/atk/def
MONSTERS = {Classes.Troll: TROLL_STATS, Classes.Underling: UNDERLING_STATS}


def encounter(monsters):
    '''Takes a dictionary with monsters and their stats and
    returns a monster object at random '''
    monst_type = r.choice(list(monsters))
    return monst_type(*monsters[monst_type])


def battle(hero, enemy):
    '''Enters a battle between hero and a number of enemies
    '''
    print "Look out! A wild {} appears!".format(enemy.monst_type)
    print "Prepare for battle {}!".format(hero.name)

    while enemy.check_health():
        while True:
            print
            action = raw_input("What will you do?: \nAttack (a): "
                               + "\nInvintory: (i): \nRun: (r): ").lower()
            print
            if action == "a":
                print "You attack..."
                handle_attack(hero, enemy)
                break
            elif action == "i":
                print hero.display_invintory()
                use_invintory(hero)
            elif action == "r":
                print "Can't run away"
            else:
                print "Invalid input. Try again."
        print
        print hero
        print
        print enemy
        print
    print "Congratulations! You slayed the {}!".format(enemy.monst_type)
    print "You gained {} exp".format(9001)


def handle_attack(attacker, defender):
    # simulates an attack on one character by another
    if attacker.attack/defender.defense <1:
        defender.hp -= 1
    else:
        defender.hp -= float(int((attacker.attack/defender.defense)))


def use_invintory(carrier):
    '''Prompts the user to select an item to use then removes one 
    of those items from the invintory'''
    invintory = carrier.invintory
    while True:
        item = raw_input(
            "Which item would you like to use? (enter b to go back) : ")
        if item in invintory and invintory[item] > 0:
            invintory[item] -= 1
            if item == "Potion":
                print "You have used 1 Potion. You have {} remaining".format(invintory[item])
                print
                use_potion(carrier)
            if invintory[item] == 0:
                # If you run out of an item, remove it from invintory
                invintory.pop(item, None)
            break
        elif item == "b":
            break
        else:
            print "You don't have any " + item + ". Please try again"


def use_potion(healed_person):
    print "The potion heals you for 10 HP. You have a strong resolve and a renewed outlook on life"
    healed_person.hp += 10


def game():
    '''Runs a battle simulator with a random monster'''
    print """
    	  _____      _           _        ___                  _   
	 | ____|   _| | ___ _ __( )___   / _ \ _   _  ___  ___| |_ 
	 |  _|| | | | |/ _ \ '__|// __| | | | | | | |/ _ \/ __| __|
	 | |__| |_| | |  __/ |    \__ \ | |_| | |_| |  __/\__ \ |_ 
	 |_____\__,_|_|\___|_|    |___/  \__\_\\__,_|\___||___/\__| 
	"""

    print "Welcome Hero "
    name = raw_input("What is your name?: ")
    hero = Classes.Hero(name, *HERO_STATS)
    monst = encounter(MONSTERS)

    hero.invintory["Potion"] = 1
    print

    battle(hero, monst)


game()

# euler = Hero("Euler", *HERO_STATS)
# monst = Troll(*TROLL_STATS)
# euler.invintory["Potion"] = 1
# euler.invintory["Sword"] = 1
# print euler.display_invintory()
# print monst.invintory


# gidling = Imp(*IMP_STATS)
# mondus = Troll(*TROLL_STATS)
# print "gidling hp before: " + str(gidling.hp)
# print "mondus hp before: " + str(mondus.hp)
# battle(gidling, mondus)
# print "gidling hp after: " + str(gidling.hp)
# print "mondus hp after: " + str(mondus.hp)
