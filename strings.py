#!/bin/python3

print("Strings")
print('Hi')
print("""Hello there""")

print("Go" + " concatting")
print("\n") # New Line


sentence = "This is a sentence."
print(sentence.split())     # Default delimiter is space

splitted = sentence.split()
print("\n".join(splitted))

print("I said 'give me stuff'")
print("I said \"give me stuff\"")
print("""I said "give me stuff" """)

print("A" in "Apple")       # True - contains?
print("a" in "Apple")       # False - contains?

print("        asdf        ".strip())   # Trim spaces
print(sentence.find("T"))               # Index of

print("Wow {}".format(sentence))        # Placeholder {}
