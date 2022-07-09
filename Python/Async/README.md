# Python Thread와 Async를 이용한 비동기 방법



이후 Client에서  Request 보낼 Server의 소스는 다음과 같다.
```python
@router.get("/second")
async def second():
    return {
        "second": random.randint(1, 100),
    }
```

그리고 일반 함수를 생성해서 Server로 Request 했을 때, 약 20초 걸린다.
```python
import datetime
import requests


def second_request():
    resp = requests.get("http://localhost:8090/second")


start = datetime.datetime.now()
for _ in range(0, 10):
    second_request()
print(datetime.datetime.now() - start)

# output
# 0:00:20.466531
```

---
## 1. theading.Thread 사용 
`threading.Thread`를 사용

```python
import datetime
import threading
import requests


class MyThread(threading.Thread):

    def run(self) -> None:
        resp = requests.get("http://localhost:8090/second")

        
start = datetime.datetime.now()
threads = []
for _ in range(0, 10):
    threads.append(MyThread())

for th in threads:
    th.start()

for th in threads:
    th.join()
print(datetime.datetime.now() - start)

# output
# 0:00:02.077700
```

### Thread를 사용할 때 주의할 점
총 1000개의 `Thread`를 생성할 것이고 부하를 줄이기 위해서 `각 100번씩 나누어 10번을 반복`한다고 가정하자.

이렇게 될 경우 역할을 수행한 `Thread`는 종료가 되어도 요청으로 실행된 메인 프로세스가 
종료될때 까지는 각 `Thread`는 `DB Connection을 Close하지 않는다`.  
따라서, `Thread에서 DB를 접근할 경우에는 몇가지 추가 구현과 DB 설정이 필요`하다.

### Database 와 관계된 것이기 때문에 매우 중요하니 꼭 알아두자.
다른 프로세스 로직들이 `Max Connection Error`가 발생하거나, `database lock` 이 걸릴수 있다

1. 첫번째로 Database의 Max connection 수를 확인하고 설정을 해주어야 한다.
2. Try - Catch - Finally 구문을 활용하여 Finally 부분에서 꼭 Thread의 DB를 Close 해주어야 한다.  
3. Thread에서 Database Update, Insert를 한다면 Database에게 부담을 줄 수 있으니 너무 많은 생성은 하지 말자.  
괜히 다른 Transaction이랑 얽혀서 Deadlock 걸리고 후회하지 말자.
4. 새로운 로직에 Thread가 추가 된다고 하면 시간을 계산해서 동시에 DB Connect가 많지는 않은지 계산을 해보자.

---
## 2. async와 aiohttp 사용
`async` `await`, `aiohttp` 를 사용 

https://docs.aiohttp.org/en/stable/index.html

```python
import asyncio
import datetime
import aiohttp


async def second_request():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8090/second") as response:
            resp = await response.json()
            return resp


async def ping():
    tasks = [asyncio.ensure_future(second_request()) for _ in range(100)]
    result = await asyncio.gather(*tasks)
    print(result)


start = datetime.datetime.now()
loop = asyncio.get_event_loop()
loop.run_until_complete(ping())
loop.close()
print(datetime.datetime.now() - start)

# output
# [{'second': 75}, {'second': 1}, {'second': 8}, {'second': 79}, {'second': 96}, {'second': 15}, {'second': 72}, {'second': 99}, {'second': 69}, {'second': 93}, {'second': 98}, {'second': 75}, {'second': 47}, {'second': 38}, {'second': 23}, {'second': 85}, {'second': 60}, {'second': 41}, {'second': 29}, {'second': 49}, {'second': 13}, {'second': 98}, {'second': 93}, {'second': 72}, {'second': 18}, {'second': 32}, {'second': 54}, {'second': 37}, {'second': 48}, {'second': 63}, {'second': 67}, {'second': 65}, {'second': 78}, {'second': 37}, {'second': 32}, {'second': 56}, {'second': 38}, {'second': 85}, {'second': 89}, {'second': 46}, {'second': 27}, {'second': 27}, {'second': 46}, {'second': 91}, {'second': 78}, {'second': 47}, {'second': 49}, {'second': 94}, {'second': 79}, {'second': 94}, {'second': 11}, {'second': 57}, {'second': 77}, {'second': 55}, {'second': 59}, {'second': 50}, {'second': 57}, {'second': 64}, {'second': 25}, {'second': 28}, {'second': 28}, {'second': 70}, {'second': 58}, {'second': 100}, {'second': 81}, {'second': 47}, {'second': 62}, {'second': 37}, {'second': 10}, {'second': 38}, {'second': 5}, {'second': 17}, {'second': 20}, {'second': 82}, {'second': 32}, {'second': 16}, {'second': 8}, {'second': 14}, {'second': 13}, {'second': 54}, {'second': 56}, {'second': 93}, {'second': 86}, {'second': 1}, {'second': 77}, {'second': 17}, {'second': 24}, {'second': 38}, {'second': 4}, {'second': 66}, {'second': 52}, {'second': 93}, {'second': 6}, {'second': 3}, {'second': 88}, {'second': 72}, {'second': 39}, {'second': 70}, {'second': 18}, {'second': 67}]
# 0:00:02.212621
```
