# 이해하기

### 어느 search 가 빠르고 느린지 확인 하는 방법
```python
import csv

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle):
    is_exist = False
    for item in haystack:
        if item == needle:
            is_exist = True
    return is_exist

def search_unknown_1(haystack, needle):
    return any((item == needle for item in haystack))

def search_unknown_2(haystack, needle):
    return any([item == needle for item in haystack])

def get_dataset(filename: str) -> list:
    ...

haystack = get_dataset('banklist.csv')
needle = 'Hana Bank'

search_fast(haystack, needle)
search_slow(haystack, needle)
search_unknown_1(haystack, needle)
search_unknown_2(haystack, needle)
```
당연히 search_fast() 는 함수 중간에 return 하기 때문에 빠르다는 것을 알 수 있고
search_slow() 는 끝까지 탐색을 이어가기 때문에 느리다는 것을 한눈에 확인이 가능하다.

그렇다면 search_unknown_1() 과 search_unknown_2() 는?
 
### 프로파일링 하면서 확인을 위해 데이터를 생성했다.
임의에 약 35만개 row에서 "hana bank" 만이 유일 값으로 존재하고 이를 찾을 것이다.
![](data/1-1.png)

### 결과는 이렇다.
![](data/1-2.png)

### 시간 차이가 발생한 이유를 찾아보자
이유는 generator 와 list의 iterator 처리 방식의 차이에서 발생한다.  
generator는 메모리 측면에서는 좋지만 loop 형식으로는 iterator 보다 좋지 않다.
```python
def search_unknown_1(haystack, needle):
    print(type((item == needle for item in haystack)))
    return any((item == needle for item in haystack))

def search_unknown_2(haystack, needle):
    print(type([item == needle for item in haystack]))
    return any([item == needle for item in haystack])

"""
출력
<class 'generator'>
<class 'list'>
"""
```


### 참고로 파이썬 data type 의 Big-O 복잡도
https://2dowon.netlify.app/python/data-type-big-o/