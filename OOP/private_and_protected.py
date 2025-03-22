class Animal:
    def __init__(self, name):
        self._protected = "Protected Variable"
        self.__private = "Private Variable"
        self.name = name

    def get_private(self):
        return self.__private  # Access private inside class


dog = Animal("Buddy")
print(dog._protected)  # Output: Protected Variable (Not recommended to access)
# print(dog.__private)   # ❌ AttributeError
print(dog.get_private())  # ✅ Output: Private Variable
print(dog.__init__("bro"))
print(dog.name)
