from helper import getDNAStringsList

dna_strings = getDNAStringsList()
s= dna_strings[0]
t= dna_strings[1]

indices = []
i = 0
for idx, base in enumerate(s):
    if i >= len(t):
        break
    if t[i] == base:
        indices.append(idx + 1)
        i += 1

print(' '.join(str(n) for n in indices))

