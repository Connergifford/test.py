#
name = input("please enter a name for your hero. ")
print ("Your name is " == __name__)



class orge:
    hp = 100
    luck = 5
    attackdamage = 10
    enemyname = "shrek"
    defense = 20
    reward = 2

    def __init__(self, name, hp, luck, attackdamage, defense, reward):
        self.hp = hp
        self.luck = luck
        self.attackdamage = attackdamage
        self.enemyname = name
        self.defense = defense
        self.reward = reward

    def enemyattack(self, player):
        player.hp -= (self.attackdamage - player.defense)

    def enemydefend(self, player):
        pass

class player():
    hp = 100
    attackdamage = 20
    playername = "Conner the knight"
    defense = 5
    gold = 50
    luck = 10

    def __init__(self, name, hp, attackdamage, luck, defense, gold):
        self.hp = hp
        self.attackdamage = attackdamage
        self.defense = defense
        self.gold = gold
        self.luck = luck

    def playerattack(self, enemy):
        enemy.hp -= (self.attackdamage - enemy.defense)

        print(f"{self.playername} attacked {enemy.enemyname} for {(self.attackdamage - enemy.defense)} damage.")

        if enemy.hp <= 0:
            print(f"{enemy.enemyname} died.")

    def playerdefend(self, enemy):
        pass

    def heal(self, target):
        target.hp += int(self.attackdamage / 2)


shrektheorge = orge("shrektheorge", 100, 3, 10, 3, 100)
fionatheorge = orge("Fionatheorge", 300, 10, 50, 10, 500)

jasontheslasher = player("jasontheslasher", 100, 20, 5, 10, 100)
masonthemathmaticion = player("masonthemathmaticion", 150, 20, 5, 10, 100)
woodstheally = player("woodstheally", 150, 20, 5, 10, 100)
reznovtherussian = player("reznovtherussian", 150, 20, 5, 10, 100)

print(f"{fionatheorge.enemyname} attacks for {fionatheorge.attackdamage} damage.")

fionatheorge.attackdamage *= 1.5

print(f"{fionatheorge.enemyname} gets a blessing from the gods and gets a 1.5 times increase in damage and attacks again for {fionatheorge.attackdamage} damage.")

jasontheslasher.playerattack(shrektheorge)
masonthemathmaticion.playerattack(shrektheorge)
masonthemathmaticion.playerattack(shrektheorge)
woodstheally.playerattack(shrektheorge)
reznovtherussian.playerattack(shrektheorge)