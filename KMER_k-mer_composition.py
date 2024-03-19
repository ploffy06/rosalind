from helper import getDNAStringsList
import itertools

k = 4
dna_string = getDNAStringsList()[0]

k_mers = []
for perm in itertools.product('AGTC', repeat=int(k)):
    str_perm = ''.join(p for p in perm)
    k_mers.append(str_perm)

k_mers = sorted(set(k_mers))

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

A = []
for m in k_mers:
    A.append(occurrences(dna_string, m))

print(' '.join(map(str, A)))
