
def print_numbers(n):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				print(i, j, k)
print_numbers(10) # O(n^3) -> O(n^2) -- any power after n^2 is considered n^2