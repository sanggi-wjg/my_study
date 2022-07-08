class Person(object):

    def __init__(self, id: int, name: str, age: int):
        self._id = id
        self.name = name
        self.age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self.age

    @name.setter
    def name(self, value):
        if not (1 < len(value) < 10):
            raise ValueError("Name can not exceed 10 or below 1 characters")
        self._name = value

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age can not be negative")
        self._age = value


person1 = Person(1, "홍길동", 100)
# person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
# person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative

# person1.age = -1  # ValueError: Age can not be negative
person1.id = 2 # AttributeError: can't set attribute