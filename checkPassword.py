def checkPassword(password):
    number = False
    upper = False
    if len(password) < 6:
        return False
    for i in password:
        if i.isdigit():
            number= True
        if i.isupper():
            upper= True
    return number and upper

print(checkPassword('Killer123'))
