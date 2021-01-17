# Aka Maps
drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple": 6}

print(drinks)
print(drinks.keys())
print(drinks.get("Buttery Nipple"))
print(drinks.get("Tea"))    # None because its not in dictionary

drinks["Whiskey"] = 5  # Put by key
print(drinks)

drinks.update({"Coffee": 1})    # Put with update
print(drinks)

movies = ["Harry Potter", "The Lord of the Rings", "Shutter Island"]
person = ["Me", "Other dudes", "Her"]
movie_dictionary = {key: value for key, value in zip(movies, person)}
