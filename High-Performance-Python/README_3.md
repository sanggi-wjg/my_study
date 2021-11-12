## 리스트
리스트는 동적 배열로 크기를 자유자재로 조절할 수 있는데
이러한 변경 가능한 특성 때문에 리스트는 메모리와 추가 연산을 필요로 한다.

리스트에 object 추가 시 기존에 object들과 추가되는 object를 새로운 리스트를 추가하여
생성한다. 새로 추가된 리스트의 크기는 기존 N개와 추가되는 1개 더하여 N+1이 아니라 M개
(M > N+1) 의 크기를 가진다. 크기에 여유를 두는 이유는 메모리 할당과 복사 요청 횟수를 줄이기 위하여다.

### 리스트의 크기 
1을 할당한 이후 크기는 동일하다가 5를 할당하니 크기가 커진다. 이는 새로 리스트를 생성한 것.
```python
a = []
print('0', sys.getsizeof(a))

a.append(1)
print('1', sys.getsizeof(a))

a.append(2)
print('2', sys.getsizeof(a))

a.append(3)
print('3', sys.getsizeof(a))

a.append(4)
print('4', sys.getsizeof(a))

a.append(5)
print('5', sys.getsizeof(a))
``` 
```shell script
0 64
1 96
2 96
3 96
4 96
5 128
```
### 리스트 크기별로 달라지는 메모리 여유 크기 
리스트는 현재 크기별로 여유크기를 점점 높게 가져간다.  
계산을 해보면 69160 / 8 = 8645.   
즉, 7672개 object가 들어갔을때 약 1000개의 object를 넣을 수 있는 크기가
추가로 할당 되어 메모리를 차지 한다는 것을 알수 있다. 
```python
a = []
for i in range(1, 8001):
    a.append(i)
    print(i, sys.getsizeof(a))
```
```
1 96
2 96
3 96
4 96
5 128
6 128
7 128
8 128
9 192
10 192
11 192
12 192
13 192
14 192
15 192
16 192
17 264
...
7670 61432
7671 61432
7672 69160
...
8000 69160
```

### 리스트 append() 와 리스트 내포의 차이
```python
def create_list_1():
    a = []
    for i in range(1, 100001):
        a.append(i)

def create_list_2():
    return [i for i in range(1, 100001)]

create_list_1()
create_list_2()
```
![3-1](https://github.com/sanggi-wjg/my_study/blob/main/High-Performance-Python/data/3-1.png?raw=true)

## 리스트 복잡도 
|Operation|Example|Complexity|Notes|  
|----|:----|:----|:----|
|Index         | l[i]         | O(1)	     |
| | | |
|Store         | l[i] = 0     | O(1)	     |
|Length        | len(l)       | O(1)	     |
|Append        | l.append(5)  | O(1)	     | mostly: ICS-46 covers details
|Pop	      | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
|Clear         | l.clear()    | O(1)	     | similar to l = []
| | | |
|Slice         | l[a:b]       | O(b-a)	     | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
|Extend        | l.extend(...)| O(len(...))   | depends only on len of extension
|Construction  | list(...)    | O(len(...))   | depends on length of ... iterable
| | | |
|check ==, !=  | l1 == l2     | O(N)          |
|Insert        | l[a:b] = ... | O(N)	     | 
|Delete        | del l[i]     | O(N)	     | depends on i; O(N) in worst case
|Containment   | x in/not in l| O(N)	     | linearly searches list 
|Copy          | l.copy()     | O(N)	     | Same as l[:] which is O(N)
|Remove        | l.remove(...)| O(N)	     | 
|Pop	      | l.pop(i)     | O(N)	     | O(N-i): l.pop(0):O(N) (see above)
|Extreme value | min(l)/max(l)| O(N)	     | linearly searches list for value
|Reverse	      | l.reverse()  | O(N)	     |
|Iteration     | for v in l:  | O(N)          | Worst: no return/break in loop
| | | |
|Sort          | l.sort()     | O(N Log N)    | key/reverse mostly doesn't change
|Multiply      | k*l          | O(k N)        | 5*l is O(N): len(l)*l is O(N**2)
