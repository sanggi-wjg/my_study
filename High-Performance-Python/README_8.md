## 비동기 I/O

개발 업무를 하면서 실제 코드 자체보다는 코드에 필요한 데이터를 얻어오는 작업이 병목이 생기는 것을
많이 겪었을 것이다. 이런경우 프로그램 ``I/O 위주``라 하고 I/O 효율이 속도를 제한 한다는 것을 의미한다.

I/O는 프로그램 흐름에 큰 영향을 미친다. 파일이나 네트워크 소켓 연결을 통해 데이터를 읽을 때까지
실행을 멈추고 커널에 연산을 요청한 후 끝날때 까지 기다려야 하기 때문이다.

비동기 I/O를 활용하면 I/O 연산을 기다리는 동안 다른 연산을 수행하여 유휴 시간을 활용할 수 있다.
작업1,2,3 을 순차적으로 실행한다면 지연을 세번 감수해야 하지만 세 작업을 동시에 실행한다면 
시간을 감소할 수 있을 것이다.

파이썬에서는 제너레이터 기반의 Coroutine과 ``async 함수``로 ``Native Coroutine``을 사용한다.
async 는 Python 3.6 부터 지원한다.

### 샘플
```python
import asyncio
from openpyxl import load_workbook

async def load(path):
    workbook = load_workbook(path, read_only = True, data_only = True)
    return workbook

async def something_big():
    return [i for i in range(10000000)]

async def something_small():
    return [i for i in range(1000000)]

async def get_sheet_and_somethings(path):
    # create_task 와 동시에 실행
    task1 = asyncio.create_task(load(path))
    task2 = asyncio.create_task(something_big())
    task3 = asyncio.create_task(something_small())
    # 대기
    await task1
    await task2
    await task3
    return task1.result()

result = asyncio.run(get_sheet_and_somethings('YTO-2021-10-SHA.xlsx'))
```

```python
import asyncio
from urllib.request import Request, urlopen


async def fetch(num):
    request = Request('http://localhost:9000/ping')
    response = await loop.run_in_executor(None, urlopen, request)
    return num, response


async def ping():
    tasks = [asyncio.ensure_future(
        fetch(i)
    ) for i in range(100)]

    result = await asyncio.gather(*tasks)
    print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(ping())
loop.close()
```

## Thread 와 async 의 차이
CPU bound 작업을 할 때에만 GIL로 인해 한번의 한 쓰레드에서만 파이썬 코드를 실행 할 수 있는데 
I/O bound 작업의 경우 Thread와 async 모두 GIL을 해체하여 다른 쓰레드가
이어서 작업을 진행할 수 있도록 여러개의 쓰레드를 사용해 동시 처리가 가능하다.

* `Thread` 객체는 개발자가 직접 생성하지만 `Task` 객체는 직접 생성하지 않고
`ensure_future()`를 통해 생성 된다.
* `Thread` 는 `start()`를 통해 실행 되지만 `Task` 는 `ensure_futer()` 에서 예약 실행 된다.
* `Thread` 객체는 외부에서 쓰레드 내부를 제어할 수 있는 API 가 없고
아무때나 중단 시키면 시스템의 무결성을 해칠수 있다. 반면, `Task` 객체는 
코루틴 안에서 `CancledError` 를 발생 시키는 `Task.cancel()` 이 있다.


## Ref
```
https://nachwon.github.io/asyncio-and-threading/
```
