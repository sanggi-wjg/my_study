class Person(object):

    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = self._clean_name(name)
        self.age = self._clean_age(age)

    def _clean_name(self, name: str):
        if not (1 < len(name) < 10):
            raise ValueError("Name can not exceed 10 or below 1 characters")
        return name

    def _clean_age(self, age: int):
        if age <= 0:
            raise ValueError("Age can not be negative")
        return age


person1 = Person("홍길동", 100)
person2 = Person("홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
person3 = Person("홍길동", 0)  # ValueError: Age can not be negative
