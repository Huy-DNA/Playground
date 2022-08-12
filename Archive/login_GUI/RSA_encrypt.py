#key = 11
import random
def RSA(string):
    encrypted = ""
    for char in string:
        encrypted += str(ord(char)**11 % 127) + random.choice(["ab", "ap", "pa", "..", ".;"]) + str(random.randrange(129, 300)) + random.choice(["~%!!", "!@%", "#^-@!", "+*&",",a"])
    return encrypted