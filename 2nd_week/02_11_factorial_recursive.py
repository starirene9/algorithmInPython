# 3! = 3 * 2 * 1
# factorial(n) = n * factorial(n-1)
# factorial(n-1) = (n-1) * factorial(n-2)


def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:
        return 1 # 탈출 조건
    return  n * factorial(n - 1)

print(factorial(5))