import random

numbered_list = []
print("Generating list with 10 random numbers:")

for x in range(10):
    numbered_list.insert(0, random.randint(1,100))

print(numbered_list)
print()
print("Highest value from the list: ", max(numbered_list))