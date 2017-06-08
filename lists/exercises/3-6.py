# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

interesting_people = ['Einstein', 'Jack Black', 'The Queen']

cant_attend = interesting_people.pop(1)

print("Mr/Mrs " + cant_attend+ ", can not attend the dinner")

interesting_people.append('Elvis')

interesting_people.insert(0, 'SuperMan')
interesting_people.insert(2, 'Munk')
interesting_people.append('Josh')

print(interesting_people)

print("Mr/Mrs, " + interesting_people[0] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[1] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[2] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[3] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[4] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[5] + ". I would like to invite you to dinner")
