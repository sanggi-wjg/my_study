# 프로파일링으로 병목지점 찾기

## cProfile
```shell script
감으로 코드를 작성하는 습관을 버리고
가설을 세우고 프로파일링을 통한 검증으로 코드를 작성해라.
이는 시간을 투자 할만한 가치가 충분하고 코드 작성의 근거가 될 수 있다.
```

### cProfile 테스트
테스트 코드  
피보나치 수열을 dp와 recursion 으로 구현한 함수
```python
def fibonacci_dp(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

num = 30
fibonacci_dp(num)
fibonacci_recursion(num)
```
### 출력
* `ncalls`: 프로파일링 주기 동안 함수 호출 횟수
* `tottime`: 함수가 실행되는 동안 소비한 초 단위 시간, 다른 함수 호출 시간은 배제
* `tottime percall`: 함수를 호출하는 데 걸린 평균 시간. tottime / ncalls
* `cumtime`: 함수를 실행하는 데 걸린 초 단위 누적 시간, 다른 함수 호출 시간 포함
* `cumtime percall`: 함수를 호출할 때마다 걸린 시간에 대한 초 단위 평균 시간. cumtime / ncalls
```
C:\Script_Project\my_study>python -m cProfile -s cumulative  High-Performance-Python\2-프로파일링으로-병목지점-찾기\2-1-cProfile.py
832040
832040
         2692573 function calls (37 primitive calls) in 0.532 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.532    0.532 {built-in method builtins.exec}
        1    0.000    0.000    0.532    0.532 2-1-cProfile.py:1(<module>)
2692537/1    0.531    0.000    0.531    0.531 2-1-cProfile.py:13(fibonacci_recursion)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 2-1-cProfile.py:6(fibonacci_dp)
       29    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.setrecursionlimit}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```