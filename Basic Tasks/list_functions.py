lucky_nums = [1, 2, 3, 4]
the_fam = ["Gab", "Rand", "lol", "papa"]
print(the_fam)
the_fam.extend(lucky_nums)
the_fam.append("mama") #Adds Mama to the end of the list.
the_fam.insert(1, "kelly") 
print(the_fam)
the_fam.remove("lol")
print(the_fam)

# the_fam.clear() # The command clear's the whole list and you can start a fresh list.

the_fam.pop() #Removes End of the list 
print(the_fam)

print(the_fam.index("papa")) #shows posistion on list for "Papa"

print(the_fam.count("papa"))

# the_fam.sort()

print(the_fam)

the_fam.reverse()

print(the_fam)

realfam= the_fam.copy()

print(realfam)