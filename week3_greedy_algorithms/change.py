# Uses python3

def get_change(m):
    coins_num = 0
    den_list = [1, 5, 10]
    while m > 0:
        current_den = den_list.pop()
        if (m // current_den) > 0:
            coins_num += m // current_den
        m = m % current_den
    return coins_num

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
