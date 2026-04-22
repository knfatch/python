#(Placeholder for Name of Game): Text Based Story Game
#This file contains the code for a simple text-based story game where the player makes choices that affect the outcome of the story.
#The purpose of this game is to practice Classes and Objects in Python while creating a fun and interactive story.
#------------Classes-----------------
class Character():
    def __init__(self, name, stamina, health, attack, mana):   #Constructor for the Character class, which initializes the character's name, stamina, health, attack, and mana.
        self.name = name
        self.stamina = stamina    #Used to determine how many actions that can be taken during an encounter. Turn order is determined by stamina, with higher stamina characters going first.
        self.health = health      #Health points of the character. If health reaches 0, the character dies.
        self.attack = attack      #How much damage the character can deal to an enemy during an attack.
        self.mana = mana          #Used to determine how many spells the character can cast during an encounter.

    def display_status(self):     #A method to display the current status of the character, including health and mana.
        print(f"{self.name} Status:\nHealth: {self.health}\nStamina: {self.stamina}\nMana: {self.mana}")

class Mage(Character):            #High mana and attack, but low health.
    pass
    
class Knight(Character):          #High health and attack, but low mana.
    pass
    
class Cleric(Character):          #High health and mana, but low attack.
    pass

class Enemy():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack(self):
        return self.attack

class Bandit(Enemy):              #A common low health and attack enemy.
    pass

#--------------Functions--------------------

def potions():     #A method to display the current inventory of the character.
        print(f"{player.name}'s Inventory:\n{potions}")

def inventory():    #A method to display the current inventory of the character.
        print(f"{player.name}'s Inventory:\n{inventory}")

#-------------Game-Variable-Block-----------

potions = {"Health Potion": 0, "Mana Potion": 0, "Energy Potion": 0, "Sword": 0, "Armor": 0}   #A dictionary to keep track of the player's inventory items and their quantities.
inventory = []   #A list to keep track of the player's inventory items.

#-------------Testing-Block-----------------

player = Character("Armon", 100, 100, 20, 50)
player.display_status()
print(f"{player.name}'s Potions:\n{potions}")
print(f"{player.name}'s Inventory:\n{inventory}")