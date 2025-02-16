from helper import getDNAStringsList
import numpy as np

dna_list = getDNAStringsList()
n = len(dna_list)
dna_len = len(dna_list[0])
distances = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dna1 = dna_list[i]
        dna2 = dna_list[j]
        hamming_d = 0
        for base1, base2 in zip(dna1, dna2):
            if base1 != base2:
                hamming_d += 1
        d_p = hamming_d / dna_len
        distances[i][j] = d_p

for row in distances:
    for col in row:
        print("{:.4f}".format(col), end=' ')
    print("")