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
print(fibonacci_dp(num))
print(fibonacci_recursion(num))
