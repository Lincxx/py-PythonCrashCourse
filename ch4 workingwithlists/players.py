players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

#omit the first index
print(players[:3])

#omit the second index
print(players[2:])

print(players[-3:])

#looping through a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

