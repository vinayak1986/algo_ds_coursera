# Uses python3
import sys

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
    
def get_pisano(num):
    fib_num = [0, 1]
    period = 0
    for n in range(2, 6 * num + 1):
        fib = calc_fib(n)
        fib_mod = fib % num
        if fib_num[-1] == 0 and fib_mod == 1:
            period = len(fib_num) - 1
            break
        else:
            fib_num.append(fib_mod)
    return period
    
def get_fibonacci_huge(n, m):
    pisano = get_pisano(m)
    n_mod_m = n % pisano
    fib_n_mod_m = calc_fib(n_mod_m) % m
    return fib_n_mod_m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
