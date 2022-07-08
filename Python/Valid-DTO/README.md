# Validate Class Attributes in Python
Python에서 DTO, Data Class로 사용하는 Class를 Validation 하는 여러 방법


## 1. Validation method 사용
간단한 방법으로 `__init__` 메소드에서 validate 하는 방법이다.
만약 유효하지 않다면 `ValueError` Exception 처리 될것이다.
```python
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


person1 = Person(1, "홍길동", 100)
person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative
```

매우 간단한 방법이지만 객체 생성 이후 attribute들이 재할당 될수 있고
재할당시 에러가 발생하지 않을것이다.
```python
person1 = Person(1, "홍길동", 100)
person1.age = -1
```

---
## 2. @property Decorator 사용
built-in function인 `@property`를 사용하는 방법이다.

```python
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
person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative
```

`@property` Decorator를 사용함으로 첫번째 방법과는 다르게
객체 생성이후 attribute 변경시에도 `ValueError` Exception이 발생한다.
```python
person1 = Person(1, "홍길동", 100)
person1.age = -1  # ValueError: Age can not be negative
```

Attribute `id`는 `setter` method를 생성하지 않았기 때문에 `id`를 변경하면
`AttributeError` Exception이 발생한다.
```python
person1 = Person(1, "홍길동", 100)
person1.id = 2 # AttributeError: can't set attribute
```

---
## 3. Python Descriptor 사용
Python의 `Descriptor`를 사용하는 방법이다.
Community에 사용 예시가 있다.  
https://docs.python.org/3/howto/descriptor.html#validator-class

id는 최초 할당 이후 변경 될 것이 없으니 `@property`를 사용을 해서 재할당을 방지한다.
```python
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
person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative
```

이 방법은 재사용에 있어서 매우 유용하다.
```python
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
```

---
## 4. Decorator와 Descriptor를 같이 사용하는 방법
Python의 `Descriptor`와 `Decorator`를 같이 사용하는 방법이다.
이 방법도 재사용에 있어서 매우 유용한 방법이다.

```python
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


def valid_name(attr):
    def decorator(cls):
        setattr(cls, attr, Name())
        return cls
    return decorator


def valid_positive_number(attr):
    def decorator(cls):
        setattr(cls, attr, Age())
        return cls
    return decorator


@valid_name("name")
@valid_positive_number("age")
class Person(object):

    def __init__(self, id: int, name: str, age: int):
        self._id = id
        self.name = name
        self.age = age

    @property
    def id(self):
        return self._id


person1 = Person(1, "홍길동", 100)
person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative
```

---
## 5. Third-party Pydantic 사용
`Pydantic`은 FastAPI 데모 구현 해보면서 이런게 있는지 처음 알았는데  매우 매우 훌룡하다.   
성능에서 안 좋을 수 있어도 생산성과 가독성에서는 훌룡하다. 똑똑한 애들이 너무 많다.  
https://pydantic-docs.helpmanual.io/

```python
from datetime import datetime

from pydantic import validator, ValidationError, PositiveInt, EmailStr, BaseModel


class Name(BaseModel):
    first_name: str
    last_name: str

    class Config:
        anystr_strip_whitespace = True

    @validator("first_name")
    def valid_first_name(cls, value):
        if not (1 <= len(value) < 10):
            raise ValueError("First name can not exceed 10 or below 1 characters")
        return value

    @validator("last_name")
    def valid_last_name(cls, value):
        if not (1 <= len(value) <= 2):
            raise ValueError("Last name can not exceed 2 or below 1 characters")
        return value


class Person(BaseModel):
    id: PositiveInt
    name: Name
    age: PositiveInt
    birthday: str
    email: EmailStr

    @validator("birthday")
    def valid_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            raise ValueError("birthday must written in YYYY-MM-DD format")

try:
    person1 = Person(
        id = 1,
        name = Name(first_name = "길동", last_name = "홍"),
        age = 100,
        birthday = "1990-01-01",
        email = "user@mail.com"
    )
    print(person1)  # id=1 name=Name(first_name='길동', last_name='홍') age=100 birthday='1990-01-01' email='user@mail.com'
except ValidationError as e:
    print(e.json())
```

아래 경우 `ValidationError` Exception 발생하는데 Error에 대해서 json 형태로 확인 할 수 있다. 
```python
try:
    person2 = Person(
        id = -1,
        name = Name(first_name = "길동", last_name = "홍"),
        age = -1,
        birthday = "1990-01-32",
        email = "@mail.com"
    )
except ValidationError as e:
    print(e.json())
```
Error json
```json
[
  {
    "loc": [
      "id"
    ],
    "msg": "ensure this value is greater than 0",
    "type": "value_error.number.not_gt",
    "ctx": {
      "limit_value": 0
    }
  },
  {
    "loc": [
      "age"
    ],
    "msg": "ensure this value is greater than 0",
    "type": "value_error.number.not_gt",
    "ctx": {
      "limit_value": 0
    }
  },
  {
    "loc": [
      "birthday"
    ],
    "msg": "birthday must written in YYYY-MM-DD format",
    "type": "value_error"
  },
  {
    "loc": [
      "email"
    ],
    "msg": "value is not a valid email address",
    "type": "value_error.email"
  }
]
```
