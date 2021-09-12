# 함수

## 함수는 한 가지만!
문제의 코드다.  
session_initialize() 를 주목하자.  
최초 개발시 로그인시에 암호 체크용으로 개발을 했는데  
이후에 다른 곳에서도 암호를 체크가 필요한 경우가 생겼고  
똑같이 가져다 썻을 경우 Session이 초기화 되어 문제가 생길수 있다.

문제를 해결하기 위해서는   
함수명을 check_password_and_session_init() 등으로 함수기능 명시하는 방법  
(그래도 함수가 2가지 역할을 담당하여 문제)  
함수의 기능을 두개로 다시 작성을 진행하는 방법이 있다.
```python
def check_password(username: str, password: str) -> bool:
    try:
        user = User.object.get(username = username)

        encrypt = User.object.get_encrypt_password(username = username)
        if password == decrypt_password(encrypt):
            session_initialize()
            return True

    except User.DoseNotExist:
        raise UserDoesNotExist("user is not exist")

    return False
```

## 파이썬 팁
파이썬에서 내가 사용하는 방법으로 
Controller 시 소스 실행전에 체크하도록 하던가  
Decorator를 사용해서 체크하는 방법 두가지를 사용할수 있다. 

방법 1 : Class 상속
아래처럼 하면 당연히 소스는 변경을 해야하겠지만  
class PermissionRequired 등의 여러가지 기능을 유연하게 확장할 수 있다. 
```python
class Required:
    pass

class LoginRequired(Required):
    def dispatch(self, *args, **kwargs):
        if True:
            print('required login')
            raise Exception('required login')

        return super().dispatch(*args, **kwargs)

class Controller:
    def __init__(self):
        if hasattr(self, 'dispatch'):
            self.dispatch()

class Login(LoginRequired, Controller):
    def login(self):
        print('로그인!')
```

방법 2 : Decorator 사용
```python
def required_login(func: Callable):
    def wrapper(*args, **kwargs):
        if True:
            print('required login')
            raise Exception('required login')
        return func(args, kwargs)
    return wrapper

class Login:
    @required_login
    def login(self, *args, **kwargs):
        print('로그인!')
```

## 함수는 한 가지만 2!

이렇게 짜는 사람이 있는가? 싶지만 일단 작성...
아래는 key와 value를 받아서 If문으로 체크 후  
없으면 등록 후 True, 있으면 False 를 반환한다. 
```python
def set_value(self, key: str, value: str) -> bool:
    if key not in self.my_dict.keys():
        self.my_dict.setdefault(key, value)
        return True
    else:
        return False
``` 
문제는 bool로 인해서 발생 한다.
아래처럼 되어있다면 뭔가 이상하지 않는가?  
```python
def func_something(self):
    if set_value('First', 'Secont'):
        ...
```
아래처럼 하도록 하자
근데 누가 위처럼 짬 ㅋㅋㅋ
```python
def is_exist_key(self,key) -> bool:
    return key in self.my_dict.keys()

def set_value(self, key, value):
    if not is_exist_key(key):
        self.my_dict.setdefault(key, value)

def func_something(self):
    set_value(key, value)
```