# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

interesting_people = ['Einstein', 'Jack Black', 'The Queen']

cant_attend = interesting_people.pop(1)

print("Mr/Mrs " + cant_attend+ ", can not attend the dinner")

interesting_people.append('Elvis')

interesting_people.insert(0, 'SuperMan')
interesting_people.insert(2, 'Munk')
interesting_people.append('Josh')

#print(interesting_people)

print("I'm sorry, I can only invite 2 guests this evening\n")

interesting_people.pop()
interesting_people.pop()
interesting_people.pop()
interesting_people.pop()

print("Mr/Mrs, " + interesting_people[0] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[1] + ". I would like to invite you to dinner")

# 

print('We are inviting ' + str(len(interesting_people)) + ' people')

