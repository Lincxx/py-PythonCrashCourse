# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

cities = ['flint', 'detroit', 'erwin', 'asheville']

print(cities[2])
print(cities[-1])

cities[2] = 'johnson city'
print(cities)

cities.append('erwin')
print(cities)

cities.insert(0, 'blaney park')
print(cities)