name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


#concat
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#Adding whitspace with tabs or newlines
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#stripping white space
#right end of the string rstrip() removes it and store it back in the variable
fav_lang = "Python "
print(fav_lang.rstrip())

#left end of string lstrip() removes it and store it back in the variable
fav_lang = " Python"
print(fav_lang.lstrip())

#form both end strip()
fav_lang = " C++ "
print(fav_lang.strip())