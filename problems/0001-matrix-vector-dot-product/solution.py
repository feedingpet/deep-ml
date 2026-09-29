def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1

	m = len(a)
	n = len(a[0])

	result = [0.0] * m
	for i in range(m):
		sum = 0
		for j in range(n):
			sum += a[i][j] * b[j]
		result[i] = sum
		
	return result