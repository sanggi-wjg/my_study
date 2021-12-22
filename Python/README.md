## Python

### 파이썬 Magic Method
https://docs.python.org/ko/3.7/reference/datamodel.html#special-method-names

#### new
* 인스턴스 생성시 호출되며 Static method 이다.
* 일반적인 구현은 super().__new__(cls) 로 인스턴스 생성후 Return 전에 필요한 작업을 함
* 만약 인스턴스를 Return 하지 않는다면 __init__ 은 호출되지 않는다.
```python
class Sample(object):

    def __new__(cls, *args, **kwargs):
        print('new', args, kwargs)
        this = super().__new__(cls)
        cls.args = args
        cls.kwargs = kwargs
        return this

    def __init__(self, *args, **kwargs):
        print('init', args, kwargs)

    def show(self):
        print('show', self.args, self.kwargs)

sample = Sample(123, key = 'abc')
sample.show()
print(sample)

# output
# 호출 순서는 new -> init -> show
new (123,) {'key': 'abc'}
init (123,) {'key': 'abc'}
show (123,) {'key': 'abc'}
<__main__.Sample object at 0x0000025568411310>
```

* 주로 인스턴스 생성시, 불변의 데이터를 사용하기 위해서 구현 되어 진다.  
(init 에서 인스턴스에 property 변경시에 변경이 가능하니 주의하자.)
```python
class Sample(object):

    def __new__(cls, *args, **kwargs):
        this = super().__new__(cls)
        cls.number = 7
        return this

    def show(self):
        print(__class__, self.number)

for _ in range(5):
    sample = Sample()
    sample.show()

# output
<__main__.Sample object at 0x000001FE7E6859A0> 7
<__main__.Sample object at 0x000001FE7EB31340> 7
<__main__.Sample object at 0x000001FE7E6859A0> 7
<__main__.Sample object at 0x000001FE7EB31340> 7
<__main__.Sample object at 0x000001FE7E6859A0> 7
```
* 혹은 사용자 Meta class 정의를 하기 위해서 사용하기도 한다.
  (metaclass 사용 예시로 유명한 것은 Singleton 구현이 있다.)
```python
class MyPointMeta(type):

    def __new__(mcs, name, bases, namespace):
        namespace['desc'] = 'My Point Meta Class'
        namespace['show'] = lambda self: print(self.x, self.y)
        return super().__new__(mcs, name, bases, namespace)

class MyPoint(metaclass = MyPointMeta):

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = MyPoint(1, 2)
print(point.desc)
point.show()

# output
My Point Meta Class
1 2
```

## 파이썬 개발 이슈
<details> 
<summary>Thread-safe</summary>
<div markdown="1">
https://box0830.tistory.com/333
</div>
</details>
