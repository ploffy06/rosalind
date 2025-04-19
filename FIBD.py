from helpers.file_read_helper import read_single_line

# n = 81, m = 16 -> 37577591247583251
# n = 6, m = 3 -> 4

def rabbits_recurse(n, m):
    # TODO: implement recursive relationship

    return None

def rabbits_iterative(n, m):
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

    return unmatured + sum(matured)

if __name__ == '__main__':
    n, m = map(int, read_single_line())
    rabbits = rabbits_iterative(n, m)

    print(rabbits)


