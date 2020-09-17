# Uses python3

def optimal_summands(n):
    summands = [1]
    sum_list = 1
    for num in range(2, n):
    	result = sum_list + num
    	if result < n:
    		summands.append(num)
    		sum_list += num
    	elif result == n:
    		summands.append(num)
    		break
    	else:
    		last_num = summands.pop()
    		current = n - sum_list + last_num
    		summands.append(current)
    		break
    return summands

if __name__ == '__main__':
    n = int(input())
    if n <= 2:
    	print(1, n, sep = '\n')
    else:
    	summands = optimal_summands(n)
    	print(len(summands))
    	for x in summands:
        	print(x, end=' ')
