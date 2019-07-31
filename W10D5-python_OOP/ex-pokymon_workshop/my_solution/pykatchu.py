import random
class Pokemon:
    def __init__(self, name, noise):
        self.name= name
        self.noise= noise
        self.health = random.randint(1,7)
        self.strengh = random.randint(1,7)
        self.armor = random.randint(1,7)
    
    def getName(self):
        return self.name
    
    def isDead(self):
        if self.health <= 0 :
            return True
        else:
            return False
    
    def getAttackNoise(self):
        return self.noise
        # return getattr(self, 'noise') ?
    
    # def attack(self, other):
    #     self.bonus= random.randint(1,5)
    #     other.bonus= random.randint(1,5)
    #     if ((self.strengh + self.bonus) > (other.armor + other.bonus)):
    #         other.health -= ((self.strengh + self.bonus) - (other.armor + other.bonus))
    #         return True
    #     else:
    #         False

    def attack(self, other): #/new attack method- If the random attack bonus is even increase it by 2, else decrease it by 1.
        self.bonus= random.randint(1,5)
        other.bonus= random.randint(1,5)
        if self.bonus == other.bonus:
            self.bonus += 2
            other.bonus += 2
        else:
            self.bonus -= 1
            other.bonus -= 1
        
        if ((self.strengh + self.bonus) > (other.armor + other.bonus)):
            other.health -= ((self.strengh + self.bonus) - (other.armor + other.bonus))
            return True
        else:
            False


class Pikatchu(Pokemon):
    def __init__(self):
        super().__init__("Pikatchu", "Pikatchuuu")
        # Pokemon.__init__(self)

class Aipom(Pokemon):
    def __init__(self):
        super().__init__("Aipom", "Aipooooom")

class Mopom(Pokemon):
    def __init__(self):
        super().__init__('Mopom', "Mooopoooom")
        self.health += 1 if self.health < 6 else 6

class Loli(Pokemon):
    def __init__(self):
        super().__init__("Loli", "Loliiiiii")
        self.armor = random.randint(4,7)