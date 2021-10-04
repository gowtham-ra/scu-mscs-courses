import time
from random import seed
from random import randint

"""
Maximum Subarray - Brute Force Approach

Array A passed will hold the changes in the prices between 2 consecutive days
as values, with the first value being 0 for day 1 (since no change)"""

def max_subarray(A):
	N = len(A)
	profit = float('-inf')
	buy = 0 # Day to buy
	sell = 0 # Day to sell

	for i in range(1, N):
		summ = 0
		for j in range(i, N):
			summ += A[j]
			if summ > profit:
				buy = i-1
				sell = j
				profit = summ

	return (buy, sell, profit)

seed(1)
print("Brute Force")
A = [randint(-10, 20) for _ in range(100)]
start_time = time.time()
A.insert(0, 0)
max_subarray(A)
tim = round((time.time() - start_time), 8)
print(tim)


# Recursive Approach
def max_subarray_recursive(A, low, high):
	if high == low:
		return A[low]

	mid = (low + high) // 2

	profit1 = max_subarray_recursive(A, low, mid) 
	profit2 = max_subarray_recursive(A, mid + 1,high)
	profit3 = max_subarray_cross(A, low, mid, high)

	return max(profit1, profit2, profit3)


# Crossing midpoint
def max_subarray_cross(A, low, mid, high):
	left_buy = mid
	left_sell = mid
	left_profit = float('-inf')
	summ = 0

	for i in range(mid, low-1, -1):
		summ += A[i]

		if summ > left_profit:
			left_buy = i
			left_profit = summ


	right_buy = mid
	right_sell = mid
	right_profit = float('-inf')
	summ = 0

	for i in range(mid+1, high+1):
		summ += A[i]

		if summ > left_profit:
			right_sell = i
			right_profit = summ

		return max(left_profit, right_profit)

seed(1)
start_time = time.time()
print("\nRecursive")
A = [randint(-10, 20) for _ in range(101)]
max_subarray_recursive(A, 0, len(A)-1)
time = round((time.time() - start_time), 8)
print(time)














