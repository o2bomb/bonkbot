import Roguelike

class Milkman(Enemy):

    def __init__(self):
        pass
    
    def spawn(self):
        print('''A tall, pasty man walks up to you. He's wearing a pair of white 
pants hitched just below his exposed pecs with a black leather belt, 
like a push-up bra. He bites his lip and starts gently circling his 
nipples between his index and middle fingers.\n"Hey," he says. "Got any milk?"''')
        
    def idle():
        if self.hp == 100:
            print('''The Milkman sinks into a fighting stance. The way the sunlight
fragments on his trousers makes you think they weren't always white.''')
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
        print('''The Milkman topples backwards like a plank of wood to the
floor, unconscious. His fingers continue to twirl his nipples, transcending
consciousness as milk spirals from his teets, as if a courtyard fountain.''')
        a = input("No one is looking. Do you catch some milk in your tongue?")
        a.strip(a)
        if a == "y" or a == "Y" or a == "yes" or a == "Yes":
            print('''Sweet, yet bitter. Like dark chocolate.\n Attack + 2\n Magic
            Resistance + 3\n HIV + 1''')
            
        elif a == "n" or a == "N" or a == "no" or a == "No":
            print('''You resist your temptations.\n Resistance + 2\n Health + 5''')