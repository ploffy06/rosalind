from helper import monoisotopic_mass_table

protein_string = ''
with open('data.txt', 'r') as file:
    for line in file:
        protein_string += line.replace('\n', '')

total_weight = 0
for protein in protein_string:
    total_weight += monoisotopic_mass_table[protein]

print(round(total_weight, 3))