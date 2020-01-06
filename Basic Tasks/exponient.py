print(2**3)  # easiest function

print("Example above, Try it now!: ")
print("")


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


base = int(input("What's your base number? "))
power = int(input("how much is it going to get powered by? "))
print(raise_to_power(base, power))
