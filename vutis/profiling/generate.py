import random

# Save the numbers to a file
max = 1000000
numbers = 10
with open('numbers0.txt', 'w') as file:
    for n in range(numbers):
        file.write(str(random.randint(0, max)) + '\n')

numbers = 1000
with open('numbers1.txt', 'w') as file:
    for n in range(numbers):
        file.write(str(random.randint(0, max)) + '\n')

numbers = 1000000
with open('numbers2.txt', 'w') as file:
    for n in range(numbers):
        file.write(str(random.randint(0, max)) + '\n')