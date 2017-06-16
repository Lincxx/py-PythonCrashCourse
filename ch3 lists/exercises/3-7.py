# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

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

del interesting_people[0]
del interesting_people[0]
print(interesting_people)