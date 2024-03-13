from helper import getDNAStringsList, translateRNAtoProtein

dna_strings = getDNAStringsList()
dna_string = dna_strings[0]
substrings = dna_strings[1:]

for s in substrings:
    dna_string = dna_string.replace(s, '')

dna_string = dna_string.replace('T', 'U')
protein = translateRNAtoProtein(dna_string)
print(protein)