# Uses python3

def calc_fib(n):
    fib_list = [0, 1]
    if n <= 1:
        return n
    for num in range(2, n + 1):
        last_two_sum = fib_list[-1] + fib_list[-2]
        fib_list.append(last_two_sum)
    return fib_list[-1]


def fibonacci_sum(n):
    if n <= 1:
        return n
    # The sum of the first n fibonacci numbers is the (n + 2)nd fibonacci number - 1.
    # To get the last digit of the (n + 2)nd fibonacci number, we use F(n + 2) % 10.
    # To do this, we get (n + 2) % 60, where 60 is the pisano period of 10 and then
    # get the fibonacci of this number followed by mod 10 on the result.
    n_plus_two_mod_60 = (n + 2) % 60
    n_plus_two_fib_last_digit = calc_fib(n_plus_two_mod_60) % 10
    sum_last_digit = n_plus_two_fib_last_digit - 1
    if sum_last_digit < 0:
        sum_last_digit += 10
    return sum_last_digit

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
