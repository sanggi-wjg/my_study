## 함수는 작게 만들어라
### 함수는 최대한 작게 만들어라.

If문, While문 등 사용시 블록안에는 라인 1개로 처리하도록 하자.  
이를 통해서 우리는 1단~2단 수준에 들여쓰기 수준을 유지할 수 있고 
함수는 읽기 쉬워지고 이해하기 쉬워진다.

```python
def some_method():
    ...
    if is_something:
        show_something()
```

## 함수는 한 역할만 해라

```python
def request_something():
    response = requests.post('url')
    return response

def handle_response(response: Response):
    if response.status_code == 200:
        do_success()
    else:
        do_failure()
```
