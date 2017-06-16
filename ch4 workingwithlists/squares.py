squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)


# this is more concise
sq = []
for value in range(1, 11):
    sq.append(value**2)

print(sq)


# list comprehensions
squares2 = [value**2 for value in range(1, 11)]
print(squares2)