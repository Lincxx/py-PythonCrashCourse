# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

threes = []

for value in range(0, 31, 3):
    threes.append(value)

print(threes)