# Uses python3

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left] == a[right]
    left1 = left
    right1 = (left + right) // 2
    left2 = right1 + 1
    right2 = right
    if get_majority_element(a, left1, right1) or get_majority_element(a, left2, right2):
        return 1
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
