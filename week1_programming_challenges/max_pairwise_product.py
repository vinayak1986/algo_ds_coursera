# python3


def max_pairwise_product(numbers, size):
    sorted_nums = sorted(numbers);
    max_product = sorted_nums[size - 1] * sorted_nums[size - 2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers, input_n))
