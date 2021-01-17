vegetables = ["spinach", "carrot", "cucumber", "potatoes"]

for x in vegetables:
    print(x)

for i in range(10):
    if i == 3:
        continue
    elif i == 7:
        break
    print(i)

print("\nWhile")
y = 1
while y < 10:
    print(y)
    y += 1
