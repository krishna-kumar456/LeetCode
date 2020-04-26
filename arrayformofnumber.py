A = [1,2,0,0]
K = 34

A_str = int(''.join([str(x) for x in A]))
A_add = int(A_str) + K
print([int(x) for x in list(str(A_add))])
