input = 100

# fibo(2) fibo(1) = 1
# fibo(n) =  fibo(n-1) +fibo(n-2)

def fibo_recursion(n):
    # 재귀함수시 항상 탈출조건 생각할 것
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765