## 함수 인수
함수의 이상적인 인수개수는 0개 이다.  
다음은 1개(단항)  
다음은 2개(이항)  
3개(삼항)은 피하는게 좋다.   
4개(다항) 이상은 작성하면 안된다.  
`이유는 개념을 이해하기 어렵게 만든다`  

Test case 에서도 검증하기 위해서 다양한 인수를 작성하는 것도 어렵다.

```
운영 개발할때 경우에 따라서 필요한 경우가 있는데
요즘은 IDE 잘 되어 있어서 상관 없지 않을까 싶다.
그래도 줄일수 있다면 줄이자.
```

## 1개 (단항 함수)
대표적인 단항의 경우는 주로 두가지로 나누어진다.  

1. 질문을 던지는 경우
```python
def is_file_exist(filepath:string) -> bool:
    ...
```
2. Parameter를 변환하여 결과를 Return 하는 경우
```python
def file_open(filepath:string) -> file:
    ...

def list_to_str(targer:list) -> str:
    return ''.join(target)
```

## Boolean Parameter 피해라
Boolean이 Parameter로 있는 경우 함수는 이미 두가지 역할을 처리한다는 것을 의미 한다.  
코드 다시 작성해라.

변경 前
```python
def md5_hash(text:string, returnHex:bool) -> bytes
    m = hashlib.md5(text.encode('UTF-8'))

    if returnHex:
        return m.hexdigest()
    
    return m.digest()
```
변경 後  
이런식으로 하면 될려나?
```python
def md5_hash(text:string) -> string:
    return hashlib.md5(text.encode('UTF-8'))

def md5_hash_digest(text:string) -> bytes
    return md5_hash(text).digest()

def md5_hash_hexdigest(text:string) -> bytes
    return md5_hash(text).hexdigest()
```

## 2개 (이항 함수)
2개 이상의 인자는 1개보다 이해하기 어렵다.  
예를 들어서 전자가 더 쉽게 읽히고 이해하기 쉽다.
```python
write_field(name) 
write_field(stream, name)
```

위에 경우 Class Member로 작성하면 더 쉽게 이해할 수 있다.
```python
def write_field(name:str) :
    ...
    self.stream.append(name)
```

수학적이나 상식적으로 당연한 것은 이항함수를 사용하는 것이 더 이해하기 쉽다.  
예를 들어 좌표가 있다.

```python
point = Point(x=10, y=10)
```
오히려 이렇게 작성되어 있다면 더 이해하기가 어려워진다.
```python
point = Point(10)
```

## 3개 (삼항 함수)
Parameter가 3개가 되면 정말 이해하기 어렵다.  
예를 들어서 아래와 같은 함수가 있다면 작성할 때마다  
함수를 봐야한다. 또 실수할 확률이 높아진다.
```python
def assert_equal(message:str, expected, actual):
    ...
```

## Parameter 정리
만약 함수의 Parameter 가 2~3개가 필요하다면  
함수 내부에서 독립 Class로 선언할수 없는지 혹은  
멤버변수로 처리할 수 있는지 확인해보다

변경 前
```python
class Circle(object):
    
    def __init__(x:float, y:float, radius:float):
        ...
```

변경 後
```python
class Point(object):

    def __init(x:float, y:float):
        ...

class Circle(object):
    
    def __init__(point:Point, radius:float):
        ...
```
