#!/bin/python3
class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


class AnotherChild(Parent):
    def printanother(self):
        print("{} {}".format(self.message, "another"))


Child("Hello, and welcome!").printmessage()
another = AnotherChild("what is now")
another.printanother()
another.printmessage()
