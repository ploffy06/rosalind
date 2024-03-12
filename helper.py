def getDNAStringsList():
    dna_strings = []

    with open('data.txt', 'r') as file:
        current_dna_string = ''
        for line in file:
            if line.startswith('>'):
                if current_dna_string:
                    dna_strings.append(current_dna_string)
                    current_dna_string = ''
            else:
                current_dna_string += line.strip()

        # Append the last DNA string after the loop
        if current_dna_string:
            dna_strings.append(current_dna_string)

    return dna_strings

def getRNACodonTable():
    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids)) # maps codon to aa

    return codon_table

def getDNACodonTable():
    bases = ['T', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids)) # maps codon to aa

    return codon_table

def getComplement(dna_string):
    complement = ''
    for base in dna_string:
        if base == 'A':
            complement  += 'T'
        if base == 'T':
            complement += 'A'
        if base == 'C':
            complement += 'G'
        if base == 'G':
            complement += 'C'

    return complement

def getReverseComplement(dna_string):
    return (getComplement(dna_string))[::-1]

