import math
file = open('data.txt', 'r')

dna_string = file.readline().strip()
A = [float(n) for n in file.readline().strip().split()]

file.close()

B = []
for x in A:
    frequency_c = x / 2
    frequency_g = x / 2
    frequency_a = (1 - x) / 2
    frequency_t = (1 - x) / 2

    b = 1
    for base in dna_string:
        if base == 'C':
            b *= frequency_c
        elif base == 'G':
            b *= frequency_g
        elif base == 'A':
            b *= frequency_a
        elif base == 'T':
            b *= frequency_t

    B.append(round(math.log(b, 10), 3))

print(' '.join(str(b) for b in B))