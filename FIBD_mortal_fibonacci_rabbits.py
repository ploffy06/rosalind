n = 81
m = 17

matured = []
unmatured = 1

for i in range(1, n+1):
    if i == 1:
        continue
    elif i == 2:
        unmatured -= 1
        matured.append(1)
        continue

    temp = sum(matured)
    matured.append(unmatured)
    unmatured = temp

    if i > m:
        matured.pop(0)
    # print(f'month: {i}, unmatured: {unmatured}, matured: {matured}')

print(unmatured + sum(matured))




