import random

rooms = ['river', 'castle', 'village', 'farm house', 'dungeon', 'prison', 'cave', 'tower', 'gardem']
creatures = {'crocodile': 4, 'bird': 2, 'rhinocerous': 5, 'ant': 1, 'bear': 7}

def randomizeRoom():

    return random.choice(rooms)

def encounterChance():

    monster = random.choice(list(creatures.keys()))
    encounter = random.randint(0, 1)

    for k, v in creatures.items():

        if k == monster:

            experienceGain = v

    if encounter == 0:

        return = 'but, you did not encounter any monsters.'

    elif encounter == 1:

        return = f'and, you encounted a {monster} and gained {experienceGain} experience points!'

def walking():

    direction = input('Which way do you want to move? u = Up, d = Down, l = Left, r = Right q = Quit. ').lower()
    room = random.choice(rooms)

    if direction == 'u' or\
       direction == 'd' or\
       direction == 'l' or\
       direction == 'r':

       return f'You walked to the {room} {encounterChance()}'
