# Uses python3

def calc_fib(n):
    fib_list = [0, 1]
    if n <= 1:
        return n
    for num in range(2, n + 1):
        last_two_sum = fib_list[-1] + fib_list[-2]
        fib_list.append(last_two_sum)
    return fib_list[-1]
    
def fibonacci_partial_sum(m, n):
    n_plus_two_mod_60 = (n + 2) % 60
    n_plus_two_fib_last_digit = calc_fib(n_plus_two_mod_60) % 10
    m_plus_one_mod_60 = (m + 1) % 60
    m_plus_one_fib_last_digit = calc_fib(m_plus_one_mod_60) % 10
    sum_last_digit = n_plus_two_fib_last_digit - m_plus_one_fib_last_digit
    if sum_last_digit < 0:
        sum_last_digit += 10
    return sum_last_digit

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))