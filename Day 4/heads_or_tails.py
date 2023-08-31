import random

print("Ready to flip a coin?")

coin_flip = random.randint(1, 2)
if coin_flip == 1:
    print("You got heads!")
else:
    print("You got tails!")
