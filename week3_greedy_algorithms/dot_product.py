#Uses python3

import numpy as np

def max_dot_product(a, b):
	a = np.array(sorted(a))
	b = np.array(sorted(b))
	return np.dot(a, b)
		

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))
    
