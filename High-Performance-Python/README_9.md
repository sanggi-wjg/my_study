# multiprocessing

파이썬은 기본적으로 여러 CPU를 사용하지 않는다. 단일 코어 시대에 설계 되었고
병렬 처리를 효율적으로 실행하기가 어렵기도 하다.

로직을 병렬화하면 N배의 속도를 기대하지만 실제로는 프로세스간 통신 비용이 발생 등  
N배 만큼에 성능 향상이 이루어지지는 않는다. 또는 어떻게 설계하냐에 따라서
오히려 더 느려지는 경우도 있기 때문에 설계를 잘 해야한다.

multiprocessing 모듈은 프로세스와 스레드 기반의 병렬 처리를 사용해 작업 대기열을
분산시키고 프로세스 간에 데이터를 공유할 수 있도록 한다.

작업을 병렬화 하려면 순차적으로 작성하는 방식과는 달리 다른 관점으로 작성을 해야하며
일반적으로 디버깅이 어렵다. 따라서 `성능도 중요하지만 유지보수 측면에서 단순하게 
작성을 해야한다`.

**multiprocessing 모듈로 처리하는 전형적인 예**
* CPU 위주의 작업을 ``Process``나 ``Pool`` 객체로 병렬화
* dummy 모듈을 사용해 I/O 위주의 작업을 스레드를 사용하는 Pool로 병렬화
* Queue를 통해 Pickling 한 결과를 공유
* 병렬화 작업자 사이에 바이트, 원시 데이터 타입, 사전, 리스트 등의 상태 공유

프로세스를 사용하여 여러 파이썬 인터프리터를 병렬로 실행할 수 있고
각 인터프리터는 독립된 메모리 공간과 GIL 을 가진다.

## multiprocessing 모듈
* `Process` : 현재 프로세스에서 `fork` 한 복사본으로 운영체제상 별도의 자식 프로세스이다. Process를 시작하고
상태를 쿼리할 수 있으며 실행할 target 메소드를 지정할 수 있다.
* `Pool` : `Process` 나 `threading.Thread` 를 감싸서 편한 작업자 Pool 로 만들고 작업을 공유하고
합쳐진 결과를 반호나
* `Queue` : `Producer` 와 `Consumer` 를 사용할 수 있는 FIFO
* `Pipe` : 두 프로세스의 단방향, 양방향 통신 채널
* `Manager` : 프로세스간 파이썬의 객체를 공유하는 고수준 인터페이스

## 간단한 원주율 측정 
```python
import os
import random
import time
from multiprocessing import Pool

def estimate(number):
    trials_in_quarter_unit_circle = 0
    print(f"PID : {os.getpid()} / number: {number}")

    for step in range(number):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_circle = (x * x) + (y * y) <= 1.0
        trials_in_quarter_unit_circle += is_in_circle

    return trials_in_quarter_unit_circle

if __name__ == '__main__':
    start = time.time()

    total_number = int(1e8)
    process_count = 8
    pool = Pool(process_count)

    number_per_process = total_number // process_count
    trial_per_process = [number_per_process] * process_count
    print(f"number per process : {number_per_process} / trial per process : {trial_per_process}")

    result = pool.map(estimate, trial_per_process)
    print(result)
    print(time.time() - start)
```