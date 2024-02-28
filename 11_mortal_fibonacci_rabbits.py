"""
!UNSOLVED
"""

n = 80
m = 17

matured = []
unmatured = 1

for i in range(n):
    if i == 0:
        continue
    elif i == 1:
        matured = [1]
        unmatured = 0
        continue

    temp = unmatured
    unmatured = sum(matured)
    if temp !=0: matured.append(temp)

    if i >= m and (i % 2 == (m % 2)):
        # print("here")
        del matured[1]
    # print(f"i: {i + 1}")
    # print(unmatured)
    # print(matured)
    # print("\n")

print(unmatured + sum(matured))

