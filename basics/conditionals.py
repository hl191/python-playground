def soda(money):
    if money < 0:
        return "This is a joke right?"
    elif money >= 2:
        return "Get your soda"
    else:
        return "Get out poor guy"


print(soda(-1))
print(soda(1))
print(soda(3))
