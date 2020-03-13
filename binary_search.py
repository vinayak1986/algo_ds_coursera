# Uses python3

def binary_search(a, left, right, x):
    # write your code here
    if (left == right) and (a[left] == x):
        return left
    else:
        return -1
    if right == (left + 1):
        if a[left] == x:
            return left
        elif a[right] == x:
            return right
        else:
            return -1
    mid = left + (right - left) // 2
    if a[mid] == x:
        return mid
    elif x > a[mid]:
        return binary_search(a, mid + 1, right, x)
    else:
        return binary_search(a, left, mid - 1, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    row1 = list(map(int, input().split()))
    n = row1[0]
    a = row1[1:]
    row2 = list(map(int, input().split()))
    k = row2[0]
    b = row2[1:]
    left = 0
    right = len(a) - 1
    for x in b:
        # replace with the call to binary_search when implemented
        print(binary_search(a, left, right, x), end = ' ')
