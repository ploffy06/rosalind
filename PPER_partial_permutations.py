import itertools

MOD = 1000000
n = 85
k = 9

partial_perms = 1

while n > 0 and k > 0:
    partial_perms *= n
    partial_perms %= MOD

    n -= 1
    k -= 1

print(partial_perms)
