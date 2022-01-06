from numpy import *
a = array([[1, 2, 3], [4, 5, 6]])
b = array([[4, 5], [6, 2], [3, 9]])
m = matrix(a)
n = matrix(b)
o = m.tolist()
p = n.tolist()
d = ''
for i in range(m.shape[0]):
    for j in range(m.shape[0]):
        v = 0
        for k in range(m.shape[1]):
            v += o[i][k] * p[k][j]
        d += str(v) + ' '
    if i != (m.shape[0] - 1):
        d += '; '
print(matrix(d))
