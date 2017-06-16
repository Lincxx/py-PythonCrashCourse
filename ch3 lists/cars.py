# Organizing a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# by passing 'reverse' as an argument we can do just that
cars.sort(reverse=True)
print(cars)


# sorted() function lets you display your list
# in a particular order but doesn’t affect the actual order of the list.
# The sorted() function can also accept a reverse=True
bikes = ['mountain bike', '3 speed', 'beach bike', '10 speed', 'huffy']

print("Here is the org list:")
print(bikes)

print('\nHere is the sorted list:')
print(sorted(bikes))

print("\nHere is the org list again:")
print(bikes)

# reverse a list with the reverse() method. This is a permanant change
# we can always undo this by using reverse() again
pets = ['dog', 'cat', 'frog', 'rhino']
print(pets)
pets.reverse()
print(pets)
print()

# Finding the length of a list with the len() function
friends = ['jeff', 'nick', 'erick', 'chuck', 'mike']
print(len(friends))
