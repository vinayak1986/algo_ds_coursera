#Uses python3

def get_larger_num(num1, num2):
	num1_len = len(str(num1))
	num2_len = len(str(num2))
	highest_pow = max(num1_len, num2_len)
	second_highest_pow_ten = 10 ** (highest_pow - 1)
	num1_by_pow_ten = num1 // second_highest_pow_ten
	num1_mod_pow_ten = num1 % second_highest_pow_ten
	num2_by_pow_ten = num2 // second_highest_pow_ten
	num2_mod_pow_ten = num2 % second_highest_pow_ten
	is_num1_higher = False
	if num1_len == num2_len:
		is_num1_higher = num1 > num2
	elif num1_len > num2_len:
		if num1_by_pow_ten > num2:
			is_num1_higher = True
		elif num1_by_pow_ten == num2:
			is_num1_higher = num1_mod_pow_ten > num2
	else:
		if num1 > num2_by_pow_ten:
			is_num1_higher = True
		elif num1 == num2_by_pow_ten:
			is_num1_higher = num1 > num2_mod_pow_ten
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
    
