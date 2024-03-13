from helper import getDNAStringsList

dna_strings = getDNAStringsList()
s1 = dna_strings[0]
s2 = dna_strings[1]
assert len(s1) == len(s2)

purines = ['A', 'G']
pyramidines = ['C', 'T']
transitions = 0
transversions = 0

for base1, base2 in zip(s1, s2):
    if base1 != base2:
        if base1 in purines and base2 in purines:
            transitions += 1
        elif base1 in pyramidines and base2 in pyramidines:
            transitions += 1
        elif base1 in purines and base2 in pyramidines:
            transversions += 1
        elif base1 in pyramidines and base2 in purines:
            transversions += 1

print(round(transitions / transversions, 11))



