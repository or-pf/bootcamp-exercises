import pykatchu
import random

pokemons_to_play=[pykatchu.Pikatchu(),pykatchu.Aipom(), pykatchu.Loli(), pykatchu.Mopom()]
competitors= random.sample(pokemons_to_play, 2)
p1 = competitors[0]
p2 = competitors[1]
gameOn = True
while gameOn:
    print(p1.getAttackNoise())
    print(p1.getName() + (" hit!" if p1.attack(p2) else " miss!"))
    if not p2.isDead():
        print(p2.getAttackNoise())
        print(p2.getName() + (" hit!" if p2.attack(p1) else " miss!"))
    if p1.isDead() or p2.isDead():
        gameOn = False
        print("game is over... ")
        if p1.isDead():
            print(p2.getName() + " won")
        else:
            print(p1.getName() + " won")
