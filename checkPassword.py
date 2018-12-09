def checkPassword(password):
    number = False
    upcase = False
    for i in password:
        if i.isdigit():
            number = True
        if i.isupper():
            upcase = True
    return number and upcase


print(checkPassword('KillerT123'))
