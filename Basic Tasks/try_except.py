try:
   # answer = 10/0
   # is Commented out for ZeroDivisionError

    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Yo! This is a invalid input, Try again.")

except ZeroDivisionError as err:
    print("Bruh, it's")
    print(err)
    print("🤦‍♂️")

# Notes:
# Is good Practice to have more than except:
# and to use except "something:".
