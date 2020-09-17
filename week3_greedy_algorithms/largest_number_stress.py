#Uses python3

from itertools import permutations
from numpy.random import seed, randint

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
	
def naive_solution(a):
	a_perms = [str(number) for number in a]
	a_perms = list(permutations(a_perms))
	a_perms = [int(''.join(perm)) for perm in a_perms]
	return max(a_perms)		

if __name__ == '__main__':
	seed(1)
	while True:
		some_n = randint(1, 5, 1)[0]
		some_array = list(randint(1, 1000, some_n))
		some_array_copy = some_array[:]
		naive_sol = naive_solution(some_array)
		logic_sol = largest_number(some_array)
		if naive_sol != logic_sol:
			print(some_array_copy)
			print('Error!, Naive solution = {}, Logic Solution = {}'.format(naive_sol, logic_sol))
			break
			
    
