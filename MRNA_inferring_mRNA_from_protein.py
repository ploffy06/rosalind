from helper import getRNACodonTable

file = open('data.txt', 'r')
protein_string = file.read().replace('\n', '')
file.close()

rna_count = 3 # for stop codons
codon_table = getRNACodonTable()
for protein in protein_string:
    num_codons = len([i for i in codon_table.values() if i == protein])
    rna_count *= num_codons

print(rna_count % 1000000)