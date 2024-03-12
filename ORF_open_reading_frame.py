from helper import getDNAStringsList, getDNACodonTable, getReverseComplement

dna_string = getDNAStringsList()[0]
reverse_complement = getReverseComplement(dna_string)
codon_table = getDNACodonTable()

start_codon = 'ATG'
all_protein_strings = []

def getProteins(input_dna_string):
    protein_strings = []
    for i in range(3, len(input_dna_string) + 1,1):
        if input_dna_string[i-3:i] == start_codon:
            protein_string = ''
            for j in range(i, len(input_dna_string) + 1, 3):
                curr_codon = input_dna_string[j-3:j]
                protein = codon_table[curr_codon]
                if protein == '*':
                    break
                protein_string += protein

            if protein_string not in all_protein_strings and protein == '*':
                protein_strings.append(protein_string)
    return protein_strings


all_protein_strings = getProteins(reverse_complement)
all_protein_strings.extend(getProteins(dna_string))

for protein_string in all_protein_strings:
    print(protein_string)