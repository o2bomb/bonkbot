import random

class Enemy:
    def __init__(self, name, max, health, attack, mattack, mresistance, resistance, speed):
        self.name = name
        self.max = max
        self.hp = health
        self.atk = attack
        self.matk = mattack
        self.res = resistance
        self.mres = mresistance
        self.spd = speed

class Milkman(Enemy):
    
    def spawn():
        print('''A tall, pasty man walks up to you. He's wearing a pair of white 
        pants hitched just below his exposed pecs with a black leather belt, 
        like a push-up bra. He bites his lip and starts gently circling his 
        nipples between his index and middle finger.\n "Hey," he says. 
        "Got any milk?"''')
        
    def idle():
        if self.hp == 100:
            print('''The Milkman sinks into a fighting stance. The way the sunlight
            fragments on his trousers makes you think they weren't always
            white.''')
        elif self.hp < 100 and self.hp > 50:
            print('''Smoke curls from the Milkman's furious anticipatory nipple
            rubbing. He waits for your move.''')
        elif self.hp < 50:
            print('''The Milkman's teets have been scorched purple, but his resolve 
            remains unshaken. You hear him listing the benefits of dairy products
            under his breath.''')

    def attack():
        print("The Milkman yanks your tits.")
        
    def win():
        print('''You crumple to the ground, your will as shrivelled as your nipples. 
        The Milkman's words sound muffled, but you manage to hear him say "spilt milk"
        before beginning to giggle to himself. You see him clank a pair of empty milk
        bottles beside you as your vision fades to black.''')
        
    def defeat():
        print('''The Milkman topples backwards like a plank of wood, hitting the
        unconscious. His fingers continue to twirl his nipples, transcending
        consciousness as milk spirals from his teets, as if a courtyard fountain.''')
        a = input("No one is looking. Do you catch some milk in your tongue?")
        a.strip(a)
        if a == "y" or a == "Y" or a == "yes" or a == "Yes":
            print('''Sweet, yet bitter. Like dark chocolate.\n Attack + 2\n Magic
            Resistance + 3\n HIV + 1''')
            
        elif a == "n" or a == "N" or a == "no" or a == "No":
            print('''You resist your temptations.\n Resistance + 2\n Health + 5''')


class Player:
    def __init__(self, name, max, health, attack, mattack, mresistance, resistance, speed):
        self.name = name
        self.max = max
        self.hp = health
        self.atk = attack
        self.matk = mattack
        self.res = resistance
        self.mres = mresistance
        self.spd = speed

def gameplay(currEnemy):
    
        
def shuffle():
    for i in range(len(enemyList) -1, 0, -1):
        r = random.randint(0, i)
        enemyList[i], enemyList[r] = enemyList[r], enemyList[i]

def main():
    max = 100
    hp = 100
    atk = 10
    matk = 10
    res = 10
    mres = 10
    spd = 10
    
    n = input("What is your name?\n")
    n.strip(n)
    
    a = "z"
    while(a == "z"):
        a = input("Do you think of yourself more as a lover or a fighter?\n")
        a.strip(a)
        if a == "l" or a == "L" or a == "lover" or a == "Lover":
            print("Well you're gonna be fighting.\n")
            res += 2
            a = "l"
        elif a == "f" or a =="F" or a == "fighter" or a == "Fighter":
            print("Big man on campus.\n")
            atk += 2
            a = "f"
        else:
            print("Sorry, I don't speak typo. Try again.\n")
            a = "z"
            
    a = "z"
    while(a == "z"):
        a = input("Cake sparklers. Yea or nay?\n")
        a.strip(a)
        if a == "y" or a == "Y" or a == "yea" or a == "Yea":
            print("If there's no fire hazard, there's a fun hazard.\n")
            matk += 2
            a = "y"
        elif a == "n" or a =="N" or a == "nay" or a == "Nay":
            print("What, are we *trying* to disrupt air traffic?\n")
            mres += 2
            a = "n"
        else:
            print("Sorry, I don't speak typo. Try again.\n")
            a = "z"

    a = "z"
    while(a == "z"):
        a = input("Do you prefer dogs or cats?\n")
        a.strip(a)
        if a == "d" or a == "D" or a == "dog" or a == "Dog":
            print("Same. Especially with mayo.\n")
            max += 10
            hp += 10
            a = "y"
        elif a == "c" or a =="C" or a == "cat" or a == "Cat":
            print("I love pussies.\n")
            spd += 2
            a = "n"
        else:
            print("Sorry, I don't speak typo. Try again.\n")
            a = "z"

    player = Player(n, max, hp, atk, matk, res, mres, spd)
    shuffle()
    currEnemy = enemyList.pop()
    
    print(currEnemy)


enemyList = ["Milkman"]
enemydict = {
    Milkman: [100, 100, 15, 10, 10, 10, 15]
    }
main()
