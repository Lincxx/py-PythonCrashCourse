# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

interesting_people = ['Einstein', 'Jack Black', 'The Queen']

cant_attend = interesting_people.pop(1)

print("Mr/Mrs " + cant_attend+ ", can not attend the dinner")

interesting_people.append('Elvis')

print("Mr/Mrs, " + interesting_people[0] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[1] + ". I would like to invite you to dinner")
print("Mr/Mrs, " + interesting_people[2] + ". I would like to invite you to dinner")
