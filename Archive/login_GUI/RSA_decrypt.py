#key = 23
def decrypt(string):
    string += " "
    newstring = ""
    decrypted = ""
    for i in string:
        if str.isdigit(i):
            newstring += i
        elif newstring != "":
            if int(newstring) < 127:
                decrypted += chr(int(newstring)**23 % 127)
            newstring = ""
    return decrypted
    