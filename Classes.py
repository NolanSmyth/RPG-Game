class Die:
    """Represents a die with any number of sides. 
    Can be used to simulate rolls"""

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return r.randint(1, self.sides)

class Character(object):
    """A character for the RPG. Has atributes such as health,
    attack, defense, etc."""

    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.invintory = {}  # Initialize empty invintory

    def __str__(self):
        return "hp: {} \nattack: {} \ndefense: {}".format(self.hp, self.attack, self.defense)

    def check_health(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def display_invintory(self):
        return "Invintory: \n" + "\n".join(self.invintory)

class Troll(Character):
    """A Troll character which has low attack and high defence"""
    monst_type = "Troll"

    def __init__(self, hp, attack, defense):
        super(Troll, self).__init__(hp, attack, defense)

    def __str__(self):
        return "Type: {} \n".format(self.monst_type) + super(Troll, self).__str__()

class Underling(Character):
    """An underling character which has low stats"""
    monst_type = "Underling"

    def __init__(self, hp, attack, defense):
        super(Underling, self).__init__(hp, attack, defense)

    def __str__(self):
        return "Type: {} \n".format(self.monst_type) + super(Underling, self).__str__()

class Hero(Character):
    '''The almighty hero who will save this godforsaken world'''

    def __init__(self, name, hp, attack, defense):
        super(Hero, self).__init__(hp, attack, defense)
        self.name = name

    def __str__(self):
        return "Name: {} \n".format(self.name) + super(Hero, self).__str__()

class Grid(object):
    '''A grid which represents the game area'''
    def __init__(self, height, width):
        self.board = []
        for i in range(height):
            self.board.append(["0"]*width)
    def __str__(self):
        result = ""
        for row in self.board:
            result += "".join(row) +"\n"
        return result

def main():
    g = Grid(10,10)
    print g
main()

