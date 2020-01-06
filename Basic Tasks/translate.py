# My lang KFChinese
# Vowels -> KFC


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "KFC"
            else:
                translation = translation + "Kfc"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase: ")))

# Formatting matters, Indenting is Key in python and Colons :c
