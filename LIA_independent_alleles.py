# in the 0th generation, we have AaBb
# each generation breeds two children
# each organism always mates with AaBb
# return: prob(at least N organisms) in the kth generation

# AA, Aa, aa
# AA x Aa = Aa -> 1/2
# Aa x Aa = Aa -> 1/2
# aa x Aa = Aa -> 1/2
# this then means
# AaBb x AaBb -> 1/2 * 1/2
# AABb x AaBb -> 1/2 * 1/2
# and so on

# 0: 1
# 1: 1 + 2 = 3
# 2: 3 + 4 = 7
import math

k = 5
N = 9

total = 2 ** k
not_n = 0
result = 0

for i in range(N, total+1):
    result += (0.75 ** (total - i)) * (0.25 ** i) * math.comb(total, i)

print(f"%.3f" % result)