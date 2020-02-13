# Uses python3
def calc_fib(n):
    fib_list = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for num in range(2, n + 1):
        last_two_sum = fib_list[-1] + fib_list[-2]
        fib_list.append(last_two_sum)
    return fib_list[-1]

n = int(input())
print(calc_fib(n))
