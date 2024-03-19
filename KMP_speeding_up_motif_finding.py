from helper import getDNAStringsList

dna_string = getDNAStringsList()[0]

P = [0]
i = 1
j = 0

while i < len(dna_string):
    if dna_string[i] == dna_string[j]:
        j += 1
        i += 1
        P.append(j)
    elif j > 0:
        j = P[j - 1]
    else:
        P.append(0)
        i += 1



print(' '.join(str(p) for p in P))