motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change an element in a list

motorcycles[0] = 'ducati'
print(motorcycles)

# append to a list

motorcycles.append('Indian')
print(motorcycles)

# Start with an empty list

friends = []

friends.append("Jeff")
friends.append("Nick")
friends.append("Corey")
friends.append("Erick")
friends.append("Chuck")

print(friends)

# inserting into a list

letters = ['a', 'c', 'd']
letters.insert(1, 'b')
print(letters)

# remove an element from a list

pets = ['dog', 'cat', 'fish', 'bird']
del pets[1]
print(pets)

# pop an item from a. The pop() method removes the last item in a list,
# but it lets you work with that item after removing it

sports = ['football', 'hockey', 'fencing', 'skiing']
print(sports)

# How might this pop() method be useful? Imagine that the sports
# in the list are stored in chronological order according to when we played
# them.

popped_sport = sports.pop()
print(sports)
print(popped_sport)

# popping items from any position in a list

fav_sport = sports.pop(1)
print("This has been one of my fav sports since I was a child " + fav_sport)
print(sports)

# Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove, you
# can use the remove() method

lab_colors = ['yellow', 'black', 'chocolate']
print(lab_colors)

lab_colors.remove('yellow')
print(lab_colors)


