

is_male = False  # 1st Condition is marked true
is_small = True  # 2nd Condition is marked true

if is_male:  # Checks 1st condition if true
    print("you are a male.")

else:  # if first condition is false
    print: ("You are not a male.")

if is_male or is_small:  # Checks either first or second condition is true.
    print("You are either Male or Small.")

else:  # if both condition is both false.
    print("You are neither male or small.")


# Second Condition
print("")  # Seperates the first condition with the second condition.

if is_male and is_small:  # Checks conditions if both are true.
    print("You are a small male.")
# elif is else if. Checks 1st condition if it's true and check's 2nd condition is false.
elif is_male and not(is_small):
    print("You are a tall male.")
elif not (is_male) and is_small:
    print("you are a Small Female.")
else:  # if both are false.
    print("You are neither male or small.")
