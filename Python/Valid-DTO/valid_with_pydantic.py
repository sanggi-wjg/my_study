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

    person2 = Person(
        id = -1,
        name = Name(first_name = "길동", last_name = "홍"),
        age = -1,
        birthday = "1990-01-32",
        email = "@mail.com"
    )
    print(person2)

except ValidationError as e:
    print(e.json())
    """
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
    """
# person2 = Person(2, "홍", 100)  # ValueError: Name can not exceed 10 or below 1 characters
# person3 = Person(3, "홍길동", 0)  # ValueError: Age can not be negative
