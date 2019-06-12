import random
import time
import Milkman

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
    def spawn(self):
        print(currEnemy[spawn])

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
    currEnemy.spawn()
    pass
        
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
            print("Well, you're gonna be fighting.\n")
            res += 2
            a = "l"
        elif a == "f" or a =="F" or a == "fighter" or a == "Fighter":
            print("Big man on campus.\n")
            atk += 2
            a = "f"
        else:
            print("Sorry, I don't speak typo. Try again.\n")
            a = "z"
    time.sleep(2)        

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
    time.sleep(2)

    a = "z"
    while(a == "z"):
        a = input("Do you prefer dogs or cats?\n")
        a.strip(a)
        if a == "d" or a == "D" or a == "dog" or a == "Dog" or a == "dogs" or a == "Dogs":
            print("Same. Especially with mayo.\n")
            max += 10
            hp += 10
            a = "y"
        elif a == "c" or a =="C" or a == "cat" or a == "Cat" or a == "cats" or a == "Cats":
            print("I love pussies.\n")
            spd += 2
            a = "n"
        else:
            print("Sorry, I don't speak typo. Try again.\n")
            a = "z"
    time.sleep(2)
    player = Player(n, max, hp, atk, matk, res, mres, spd)
    shuffle()
    currEnemy = enemyList.pop()
    gameplay(currEnemy)


enemyList = [Milkman]
enemydict = {
    Milkman: [100, 100, 15, 10, 10, 10, 15]
    }
main()
