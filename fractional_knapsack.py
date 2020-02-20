# Uses python3
from operator import itemgetter
def get_optimal_value(capacity, weights, values, n):
    value = 0
    weights_value = []
    for index in range(n):
        sublist = []
        sublist.append(weights[index])
        sublist.append(values[index] / weights[index])
        weights_value.append(sublist)
    weights_value = sorted(weights_value, key = itemgetter(1))
    while capacity > 0:
        last_item = weights_value.pop()
        if last_item[0]:
            w = min(last_item[0], capacity)
            value += last_item[1] * w
            capacity -= w
    return value


if __name__ == "__main__":
    n, capacity = list(map(int, input().split()))
    values = []
    weights = []
    for _ in range(n):
        value, weight = list(map(int, input().split()))
        values.append(value)
        weights.append(weight)
    opt_value = get_optimal_value(capacity, weights, values, n)
    print("{:.4f}".format(opt_value))
