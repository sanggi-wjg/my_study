## 사전(dict)과 셋(set)
dict와 set은 미리 정해진 순서로 정렬 되지 않는다.
dict와 set의 차이점은 set은 key만 가지고 있다는 것이다.

리스트와 튜플은 경우에 따라 검색을 O(logN) 시간 복잡도로 구현할 수 있다.
반면, dict와 set은 O(1)이다.

dict와 set은 보통 많은 메모리를 사용한다. 또 해시 함수에 의존 함으로 
해시 함수가 느리다면 연산속도도 느릴 것이다. 


### 리스트와 사전 검색 성능 차이
리스트 or 튜플로 구현시 O(N)  
dict로 구현시 O(1)
```python
phonebook_list = [
    ("홍길동", "010-1111-1111"),
    ("김철수", "010-1111-1234"),
    ("국영수", "010-1234-1234"),
]

def find_phonebook_list(phonebook, needle):
    for name, number in phonebook:
        if name == needle:
            return number
    return ''

phonebook_dict = {
    "홍길동": "010-1111-1111",
    "김철수": "010-1111-1234",
    "국영수": "010-1234-1234",
}
```
결과는 약 6배정도 dict가 빠르다  
물론 데이터의 크기나 컴퓨터 혹은 서버의 사양마다 차이는 있겠지만 이렇든 저렇든 dict가 빠를 것이다
```
%timeit find_phonebook_list(phonebook_list, '국영수')
171 ns ± 0.692 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

%timeit phonebook_dict['국영수']
27.8 ns ± 0.272 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

### 검색 성능 차이 2
dict와 set은 모두 hash table을 사용해서 시간복잡도가 O(1)이다.

```python
phonebook_list = [
    ("홍길동", "010-1111-1111"),
    ("김철수", "010-1111-1234"),
    ("국영수", "010-1234-1234"),
]

def unique_names_list(phonebook):
    unique_names = []
    for name, number in phonebook:
        if name[0] not in unique_names:
            unique_names.append(name[0])
    return unique_names

def unique_names_set(phonebook):
    unique_names = set()
    for name, number in phonebook:
        unique_names.add(name[0])
    return unique_names
```
```
%timeit unique_names_list(phonebook_list)
603 ns ± 5.55 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit unique_names_set(phonebook_list)
515 ns ± 2.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

## 해시함수와 엔트로피
파이썬의 객체는 __hash__와 __cmp__ 함수를 이미 구현하므로 일반적으로 해시가 가능하다.  
만약, x와 y값이 동일한 Point 객체를 여러개 생성했다면 각자 서로 다른 메모리 위치를 가지고 있으므로
해시값이 서로 다르다. 아래 예시를 확인.  
```python
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 1)
p2 = Point(1, 1)
s = { p1, p2 }

print(type(s), s)
print(Point(1, 1) in s)
```
```
<class 'set'> {<__main__.Point object at 0x00000276700F5408>, <__main__.Point object at 0x000002767059FB08>}
False
```

### 사용자 정의 해시 함수 구현
사용자 정의 해시 함수를 구현해서 같은 내용의 객체에 대해서 항상 같은 결과를 반환할 수 있도록 할 수 있다.
```python
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 1)
p2 = Point(1, 1)
s = { p1, p2 }

print(type(s), s)
print(Point(1, 1) in s)
```
```
<class 'set'> {<__main__.Point object at 0x0000023D57938448>}
True
```

## Set 복잡도
```
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Length        | len(s)       | O(1)	     |
Add           | s.add(5)     | O(1)	     |
Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
Remove        | s.remove(..) | O(1)	     | compare to list/tuple - O(N)
Discard       | s.discard(..)| O(1)	     | 
Pop           | s.pop()      | O(1)	     | popped value "randomly" selected
Clear         | s.clear()    | O(1)	     | similar to s = set()

Construction  | set(...)     | O(len(...))   | depends on length of ... iterable
check ==, !=  | s != t       | O(len(s))     | same as len(t); False in O(1) if
      	      	     	       		       the lengths are different
<=/<          | s <= t       | O(len(s))     | issubset
>=/>          | s >= t       | O(len(t))     | issuperset s <= t == t >= s
Union         | s | t        | O(len(s)+len(t))
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))

Iteration     | for v in s:  | O(N)          | Worst: no return/break in loop
Copy          | s.copy()     | O(N)	     |
```

## Dict 복잡도
```
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.get(k)     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     | 
Pop item      | d.popitem()  | O(1)	     | popped item "randomly" selected
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
View          | d.keys()     | O(1)	     | same for d.values()

Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items
	      	      	       		     | Worst: no return/break in loop
```