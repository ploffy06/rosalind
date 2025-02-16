# {1}, 1 + 1
# {1, 2} 3 + 1
# {1, 2, 3} 7 + 1
# {1, 2, 3, 4} 15 + 1
# add 1 to include empty subset

n = 922
dp = []

for i in range(n):
    if i == 0:
        dp.append(1)
    else:
        subsets = (dp[-1] * 2) + 1
        dp.append(subsets)

total_subsets = (dp[-1] + 1) % 1000000
print(total_subsets)
