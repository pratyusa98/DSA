

def subArrayExists(arr, n):
	# traverse through array
	# and store prefix sums
	n_sum = 0
	s = set()

	for i in range(n):
		n_sum += arr[i]

		# If prefix sum is 0 or
		# it is already present
		if n_sum == 0 or n_sum in s:
			return True
		s.add(n_sum)

	return False


# Driver code
arr = [4,2,-3,1,6]
n = len(arr)
if subArrayExists(arr, n) == True:
	print("Found a sunbarray with 0 sum")
else:
	print("No Such sub array exits!")


