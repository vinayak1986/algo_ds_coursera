# Uses python3
def calc_fib(n):
    fib_list = [0, 1]
    if n <= 1:
        return n
    for num in range(2, n + 1):
        last_two_sum = fib_list[-1] + fib_list[-2]
        fib_list.append(last_two_sum)
    return fib_list[-1]

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    n_mod_60 = n % 60
    n_fib_last_dig = calc_fib(n_mod_60) % 10
    n_plus_one_mod_60 = (n + 1) % 60
    n_plus_one_fib_last_dig = calc_fib(n_plus_one_mod_60) % 10
    sum_squares_last_digit = (n_fib_last_dig * n_plus_one_fib_last_dig) % 10
    return sum_squares_last_digit
    
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
