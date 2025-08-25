input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        # print(n)
        # for i in range(2, n):
        for i in prime_list: # 개선된 코드, 소수로 나누기 : 굳이 더 큰 소수로 나누지 않아도 됨.
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n) # 나눠 떨어진 적이 한 번도 없다면 prime_list 배열에 넣는다
    return prime_list


result = find_prime_list_under_number(input)
print(result)