quote = "This is a quote"
print(len(quote))  # Length
print(quote.upper())
print(quote.lower())
print(quote.title())  # Title - Capitalize first letter

name = "Me"
age = 29  # int(29)
height = 1.82  # float(1.82)

print(int(age))
print(int(29.9))  # cast to int

print("Name " + name + " is old this much " + str(age))  # May not have different types string vs int

age += 1
print(age)

birthday = 1
age += birthday
