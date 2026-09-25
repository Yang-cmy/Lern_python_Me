import random

class Character():
    def __init__(self, name, role, hp):
        self.name = name
        self.role = role
        self.hp = hp

def create_profile():
    profile = {
        "john" : Character("john", "knight", 160),
        "bill" : Character("bill", "archer", 120),
        "sarah" : Character("sarah", "mage", 80)
    }

def roll(low, high):
    results = random.randiant(low, high)
    return results

# turn base

