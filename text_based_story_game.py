#Text-Based Story Game
#This file contains the code for a simple text-based story game where the player makes choices that affect the outcome of the story.
#The purpose of this game is to practice Classes and Objects in Python while having creating a fun and interactive story.

class Character():
    def __init__(self, name, status, health, inventory):
        self.name = name
        self.status = status
        self.health = health
        self.inventory = inventory

    def display_status(self):
        print(f"{self.name} is currently {self.status} with {self.health} health.")
    def char_inventory(self):
        print(f"{self.name} has the following items in their inventory: {self.inventory}")