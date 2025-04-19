from helpers.file_read_helper import read_single_line

# note: recursion is almost always slower than iterative solution

def rabbits_recurse(n, k):
    if n == 0 or n == 1 or n == 2:
        return 1

    return rabbits_recurse(n-1, k) + k * rabbits_recurse(n-2, k)

def rabbits_iterative(n, k):
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

    return matured + unmatured

if __name__ == '__main__':
    n, k = map(int, read_single_line())
    rabbits = rabbits_iterative(n, k) # change recurse or iterative here

    print(rabbits)


