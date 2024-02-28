n = 35
k = 3

curr_month = 1
unmatured = 1
matured = 0

for i in range(n):
    if i == 0:
        continue
    elif i == 1:
        unmatured -= 1
        matured += 1
    else:
        temp = matured * k
        matured += unmatured
        unmatured = temp

print(matured + unmatured)

