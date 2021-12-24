## slots
기본적으로 파이썬에서는 객체의 인스턴스 속성을 저장하기 위해서 dict 를 사용 하는데  
이를 통해 런타임 중 속성을 변경할 수 있다. 
하지만 dict 는 메모리를 낭비하는 경향이 있다.

slots를 사용하는 경우 두가지 효과가 있다.
### 속성에 대한 빠른 접근 
```python
class Normal(object):
    pass

class UsingSlots(object):
    __slots__ = ['name']

normal = Normal()
use_slots = UsingSlots()

def fn_set_get_delete(cls):
    def set_get_delete():
        setattr(cls, 'name', 'foo var')
        getattr(cls, 'name')
        delattr(cls, 'name')
    return set_get_delete

r1 = timeit.repeat(fn_set_get_delete(normal))
r2 = timeit.repeat(fn_set_get_delete(use_slots))
print(r1)
print(r2)

# output
[0.187666, 0.1858013, 0.17950610000000006, 0.1788223, 0.18067900000000003]
[0.15390950000000014, 0.15378409999999998, 0.1545802999999999, 0.1493369, 0.1511072]
```

### dict 에 비해 적은 메모리 사용
```python
class Normal(object):
    pass

class UsingSlots(object):
    __slots__ = ['foo', 'some', 'any']

normal = Normal()
use_slots = UsingSlots()

def show_sizeof(cls):
    setattr(cls, 'foo', 'var')
    setattr(cls, 'some', 'thing')
    setattr(cls, 'any', 'thing')
        if hasattr(cls, '__dict__'):
        print(cls.__dict__, sys.getsizeof(cls.__dict__))
    else:
        print(cls.__slots__, sys.getsizeof(cls.__slots__))

show_sizeof(normal)
show_sizeof(use_slots)

# output
{'foo': 'var', 'some': 'thing', 'any': 'thing'} 104
['foo', 'some', 'any'] 80
```

### slots 와 dict 동시 사용
```python
class Foo(object):
    __slots__ = ['bar', 'baz', '__dict__']
```

### 상속에서의 slots 문제
```python
class Base_A(object):
    __slots__ = ['a']

class Base_B(object):
    __slots__ = ['b']

class Sample(Base_A, Base_B):
    pass

s = Sample()

# output
TypeError: multiple bases have instance lay-out conflict
```
이렇게 해주면 됨
```python
# 1
class Abstract_A(ABC):
    __slots__ = ()

class Base_A(Abstract_A):
    __slots__ = ('a',)

class Abstract_B(ABC):
    __slots__ = ()

class Base_B(Abstract_B):
    __slots__ = ('b',)

class Sample(Abstract_A, Abstract_B):
    __slots__ = ('a','b')

s = Sample()

# 2
class Base_A(object):
    __slots__ = ('a',)

class Base_B(object):
    __slots__ = ('b',)

class Sample():
    __slots__ = ('a','b')

s = Sample()
```

#### Ref
https://stackoverflow.com/questions/472000/usage-of-slots