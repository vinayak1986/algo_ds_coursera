# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    while True:
        if a == 0 or b == 0:
            current_gcd = max(a, b)
            break
        else:
            temp = min(a,b)
            b = max(a, b) % min(a, b)
            a = temp
    return current_gcd

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
