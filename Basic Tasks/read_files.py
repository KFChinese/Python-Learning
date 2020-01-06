goal = open("goals.txt", "r")
# key: r == Read ; w == Write a = Append (Adding to file)
# r+ == Read + Write (Thanos Power)

print(goal.readable())
# Checks if file is readable

#print(goal.read())
# Spits out read file

# print(goal.readline())
# reads the first line and so on and so fourth..

# print(goal.readlines())
# reads the line in a list.

# print (goal.readlines()[1])
# reads the SECOND line in the list.
print("")

for goal in goal.readlines():
    print(goal[0])

goal.close()

# Notes:
# 1) Make sure that close your file
