import random
import string

characters = list(string.ascii_letters + string.digits + "<>/\[]!@#$%^&*()")


def generatePassword():
    # get length of password from user
    passwordLength = int(input("Please, enter the length of password: "))

    random.shuffle(characters)

    password = []

    for char in range(passwordLength):
        password.append(random.choice(characters))

    password = "".join(password)

    print(password)


generatePassword()
