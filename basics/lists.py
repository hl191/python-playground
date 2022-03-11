movies = ["Harry Potter", "The Lord of the Rings", "Shutter Island"]
print(movies[0])
print(movies[0:2])  # Start included, end excluded
print(movies[1:])  # From 1 to end
print(movies[:1])  # From start to 1

print(movies[-1])  # Last Item
print(movies[-2])  # Second Last Item

print(len(movies))  # Size of list

movies.append("Tucker and Dale")
movies[0] = "New stuff"
print(movies)
movies.pop()  # Pops last if index not given

person = ["Me", "Other dudes", "Her"]
print(list(zip(movies, person)))

print("Tuples have paranteses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[0])
