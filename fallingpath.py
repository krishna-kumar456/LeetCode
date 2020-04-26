# A falling path starts at any element in the first row, and chooses one
# element from each row.  The next row's choice must be in a column that is
# different from the previous row's column by at most one.
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

while len(A) >= 2:
    row = A.pop()
    for i in xrange(len(row)):

        A[-1][i] += min(row[max(0, i-1): min(len(row), i+2)])

print(min(A[0]))