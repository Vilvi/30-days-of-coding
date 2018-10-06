import random

rooms = ['river', 'castle', 'village', 'farm house', 'dungeon', 'prison', 'cave', 'tower', 'gardem']
creatures = {'crocodile': 4, 'bird': 2, 'rhinocerous': 5, 'ant': 1, 'bear': 7}

def randomizeRoom():

    return random.choice(rooms)


def encounterChance():

    monster = random.choice(list(creatures.keys()))

    for k, v in creatures.items():

        if k == monster:

            experienceGain = v

    encounter = random.randint(0, 1)

    if encounter == 0:

        result = 'You did not encounter any monsters.'

    elif encounter == 1:

        result = f'You encounted a {monster} and gained {experienceGain} experience points!'

    return result
