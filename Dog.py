class Dog:
    def __init__(self, name, type="Unknown", age=0):
        self._name = name
        self._type = type
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def breed(self):
        return self._type

    @breed.setter
    def breed(self, value):
        self._type = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f"{self._name}, {self._type}, {self._age}"

    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"{self._name} is now sitting.")

    def roll_over(self):
        print(f"{self._name} rolled over!")


chaki = Dog("Chaki", "Golden Retriever", 2)
print(str(chaki))
# Output: "Buddy, Golden Retriever, 2"

chaki.bark()
# Output: "Woof!"

chaki.sit()
# Output: "Buddy is now sitting."

chaki.roll_over()
# Output: "Buddy rolled over!"