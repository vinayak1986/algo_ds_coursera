# Uses python3

def optimal_weight(W, w, n):
    # write your code here
    optimal_value = {}
    for j in range(n):
    	optimal_value[(0, j)] = 0
    for i in range(W + 1):
    	optimal_value[(i, 0)] = 0
    for j in range(1, n):
    	for i in range(1, W + 1):
    		optimal_value[(i, j)] = optimal_value[(i, j - 1)]
    		if w[j] <= i:
    			val_w_removed = optimal_value[(i - w[j], j - 1)] + w[j]
    			if optimal_value[(i, j)] < val_w_removed:
    				optimal_value[(i, j)] = val_w_removed
    return optimal_value[(W, n - 1)]

if __name__ == '__main__':
	total_weight, n = list(map(int, input().split()))
	w = [0]
	w.extend(list(map(int, input().split())))
	w = sorted(w)
	print(optimal_weight(total_weight, w, n + 1))
	
