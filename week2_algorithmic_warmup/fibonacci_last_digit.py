# Uses python3
import sys

def get_fibonacci_last_digit(n):
    fib_list = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for num in range(2, n + 1):
        last_digit = (fib_list[-1] + fib_list[-2]) % 10
        fib_list.append(last_digit)
    return last_digit

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
