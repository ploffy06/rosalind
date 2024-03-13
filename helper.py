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

monoisotopic_mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

def translateRNAtoProtein(rna_string):
    protein = ''
    codon_table = getRNACodonTable()
    for i in range(3, len(rna_string) + 1, 3):
        codon = rna_string[i-3:i]
        protein += codon_table[codon]

    return protein

