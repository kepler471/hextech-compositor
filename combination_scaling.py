# To help answer RQ1, for what `n` does the scale of available data become insufficient
# Available data is defined as: Total games played, per patch (, per region)

import math
import matplotlib.pyplot as plt
import numpy as np

def nCr(n, r):
    f = math.factorial
    return f(n) // (f(r) * f(n - r))


def nPr(n, r):
    f = math.factorial
    return f(n) // f(n - r)

#
# for i in range(10, 140):
#     print(f'n = {i}, r = 10, nPr = {nPr(i, 10):e}')
#     print(f'n = {i}, r = 10, nCr = {nCr(i, 10):e}')

p = [nPr(i, 10) for i in range(10, 140)]
c = [nCr(i, 10) for i in range(10, 140)]
n = [i for i in range(10, 140)]

plt.semilogy(n, c, 'b')
plt.semilogy(n, p, 'g')
plt.semilogy(n,1e9*np.ones(len(n)))
plt.semilogy(n,1e8*np.ones(len(n)))
plt.semilogy(n,1e7*np.ones(len(n)))
plt.semilogy(n,1e6*np.ones(len(n)))
plt.grid(b='on', which='both')
plt.show()
