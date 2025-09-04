input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]: # 앞 뒤가 같지 않으면 False
        return False
    if len(string) <= 1: # 중간 문자 하나 있으면 True
        return True
    return is_palindrome(string[1:-1]) # 앞과 뒤를 자른 것을 재귀함수 안에 넣으면 한칸 한칸 줄음

print(is_palindrome(input))