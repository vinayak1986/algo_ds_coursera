#Uses python3

def get_larger_num(num1, num2):
	num1_len = len(str(num1))
	num2_len = len(str(num2))
	is_num1_higher = False
	if num1_len == num2_len:
		is_num1_higher = num1 > num2
	else:
		joined_nums_one = int(str(num1) + str(num2))
		joined_nums_two = int(str(num2) + str(num1))
		is_num1_higher = joined_nums_one > joined_nums_two
	return is_num1_higher
		
def largest_number(a):
	sorted_digits = []
	while a:
		max_digit = 0
		for digit in a:
			if get_larger_num(digit, max_digit):
				max_digit = digit
		sorted_digits.append(str(max_digit))
		a.remove(max_digit)
	sorted_digits = int(''.join(sorted_digits))
	return sorted_digits

if __name__ == '__main__':
    n = int(input())
    digits = list(map(int, input().split()))
    print(largest_number(digits))
    
