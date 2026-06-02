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
random_3_digit = random.randint(1, 99)

if random_3_digit < 10:
    random_3_digit = str(random_3_digit)
    random_3_digit = '0' + random_3_digit
else:
    random_3_digit= (str(random_3_digit))

nickname = random_adjective + random_animal + random_3_digit

print(f"Your nickname is {nickname}")

