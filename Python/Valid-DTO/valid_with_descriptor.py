class Name:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not (1 < len(value) < 10):
            raise ValueError("Name can not exceed 10 or below 1 characters")
        self.value = value


class Age:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Age can not be negative")
        self.value = value


class Person(object):
    name: str = Name()
    age: int = Age()

    def __init__(self, id: int, name: str, age: int):
        self._id = id
        self.name = name
        self.age = age

    @property
    def id(self):
        return self._id


person1 = Person(1, "홍길동", 100)
# person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
# person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative

# person1.age = -1  # ValueError: Age can not be negative
# person1.id = 2  # AttributeError: can't set attribute


class Salary:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary can not be negative")
        self.value = value


class Staff:
    name: str = Name()
    age: int = Age()
    Salary: str = Salary()

    def __init__(self, id: int, name: str, age: int, salary: int):
        self._id = id
        self.name = name
        self.age = age
        self.salary = salary


staff = Staff(1, "김철수", 10, 100)
