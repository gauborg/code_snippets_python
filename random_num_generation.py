'''

This is an example for showing different types of random number generation for quick reference.

'''
# code snippet for different random options

import os
import random

# generates a floating point number between 0 and 1
random1 = random.random()
print(f"\nRandom floating value value between using random.random() = {random1}\n")

# generates a floating number between a given range
random2 = random.uniform(1, 5)
print(f"Random floating vlaue between 1 and 5 using random.uniform() = {random2}\n")

# generates a number using Gaussian distribution
random3 = random.gauss(10, 2)
print(f"Gaussian distribution with mean 10 and std deviation 2 using random.gauss() = {random3}\n")

# generates a random integer between a range
random4 = random.randrange(100)
print(f"Random integer value between using random.randrange() = {random4}\n")

# generates a random integer between a range with inclusion
random5 = random.randrange(0, 100, 11)
print(f"Random integer value with spacing 11 between using random.randrange() = {random5}\n")

# choosing an element from a list at random
random6 = random.choice(['win', 'lose', 'draw'])
print(f"Random element chosen from the list using random.choice() = {random6}")
print("If sequence is empty, it will raise IndexError.\n")

# shuffling a list
some_numbers = [1.003, 2.2, 5.22, 7.342, 21.5, 76.3, 433, 566, 7567, 65463]
random.shuffle(some_numbers)
print(some_numbers)

