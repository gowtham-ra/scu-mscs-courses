# Strassen's Algorithm Pseudocode

strassen_matrix_multiply(A, B):
	n = length of A
	C = nxn matrix

	if n == 1:
		c11 = a11 * b11
	else:
		partition A, B, C

		Initiate 10 new matrices, S1, ... S10 of size (n/2)x(n/2)
		Initiate 7 new matrices, P1, ... P7 of size (n/2)x(n/2)

		# Calculating the 10 sum/diff matrices
		S1 = B12 – B22
		S2 = A11 + A12
		S3 = A21 + A22
		S4 = B21 – B11
		S5 = A11 + A22
		S6 = B11 + B22
		S7 = A12 – A22
		S8 = B21 + B22
		S9 = A11 – A21
		S10 = B11 + B12

		# 7 Recursive calls for calculating the products
		P1 = strassen_matrix_multiply(A11, S1)
		P2 = strassen_matrix_multiply(S2, B22)
		P3 = strassen_matrix_multiply(S3, B11)
		P4 = strassen_matrix_multiply(A22, S4)
		P5 = strassen_matrix_multiply(S5, S6)
		P6 = strassen_matrix_multiply(S7, S8)
		P7 = strassen_matrix_multiply(S9, S10)

		# Result sub-matrices values
		C11 = P4 + P5 + P6 - P2
		C12 = P1 + P2
		C21 = P3 + P4
		C22 = P1 + P5 - P3 - P7

	return C










