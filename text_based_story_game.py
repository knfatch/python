#Text-Based Story Game
#This file contains the code for a simple text-based story game where the player makes choices that affect the outcome of the story.
#The purpose of this game is to practice Classes and Objects in Python while creating a fun and interactive story.
#------------Classes-----------------
class Character():
    def __init__(self, name, status, health, attack, mana):
        self.name = name
        self.status = status
        self.health = health
        self.attack = attack
        self.mana = mana
    def display_status(self):
        print(f"{self.name} is currently {self.status} with {self.health} health.")
    def char_inventory(self):
        print(f"{self.name} has the following items in their inventory: {self.inventory}")
class Mage(Character): #High mana and attack, but low health
    pass
    
class Knight(Character): #High health and attack, but low mana
    pass
    
class Cleric(Character): #High health and mana, but low attack
    pass
class Enemy():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
class Bandit(Enemy): #Low health and attack
    pass