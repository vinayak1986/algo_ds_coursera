# Uses python3
def evalt(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
    	assert False
        
def min_and_max(i, j):
	if i == j:
		return
	min_val = 1000000000000
	max_val = -1000000000000
	for k in range(i, j):
		a = evalt(max_dict[(i, k)], ops[k], max_dict[(k + 1, j)])
		b = evalt(max_dict[(i, k)], ops[k], min_dict[(k + 1, j)])
		c = evalt(min_dict[(i, k)], ops[k], max_dict[(k + 1, j)])
		d = evalt(min_dict[(i, k)], ops[k], min_dict[(k + 1, j)])
		min_val = min(min_val, a, b, c, d)
		max_val = max(max_val, a, b, c, d)
	return min_val, max_val
	
def get_maximum_value():
    #write your code here
    for i in range(n):
    	min_dict[(i, i)] = digits[i]
    	max_dict[(i, i)] = digits[i]
#    breakpoint()
    for s in range(n - 1):
    	for i in range(n - 1 - s):
    		j = i + s + 1
    		min_dict[(i, j)], max_dict[(i, j)] = min_and_max(i, j)
    return max_dict[(0, n - 1)]

if __name__ == "__main__":
	dataset = input()
	len_input = len(dataset)
	ops = [dataset[i] for i in range(len_input) if i % 2]
	digits = [dataset[i] for i in range(len_input) if not(i % 2)]
	digits = list(map(int, digits))
	n = len(digits)
	min_dict = {}
	max_dict = {}
	print(get_maximum_value())
