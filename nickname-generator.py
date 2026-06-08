import random

adjectives = []
animals = []

with open('adjectives.txt') as f:
    content = f.readlines()
    for adjective in content:
        adjectives.append(adjective.strip())

with open('animals.txt') as f:
    content = f.readlines()
    for animal in content:
        animals.append(animal.strip())

random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)
random_2_digit = random.randint(1, 99)

if random_2_digit < 10:
    random_2_digit = str(random_2_digit)
    random_2_digit = '0' + random_2_digit
else:
    random_2_digit= (str(random_2_digit))

nickname = random_adjective + random_animal + random_2_digit

print(f"Your nickname is {nickname}")

