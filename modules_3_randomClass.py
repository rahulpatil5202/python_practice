import random

food = ["EggCurry", "Chapatis","Buttermilk","Pickle", "friedChily"]

print(random.choice(food))
print(random.choice(food))
print(random.choice(food))

# each time choice function picks random element
# we can shuffle entire list instead as well

random.shuffle(food)
print(food)
random.shuffle(food)
print(food)
