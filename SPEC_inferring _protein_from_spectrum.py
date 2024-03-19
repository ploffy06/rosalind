from helper import monoisotopic_mass_table

file = open('data.txt', 'r')
L = file.readlines()
L = [float(l.replace('\n', '')) for l in L]
file.close()

mass_to_aa = {m:a for a, m in monoisotopic_mass_table.items()}
protein_string = ''

for i in range(len(L) - 1):
    residue = L[i+1] - L[i]
    loss = 100
    aa = ''
    for mass in mass_to_aa:
        if loss > abs(mass - residue):
            loss = abs(mass - residue)
            aa = mass_to_aa[mass]

    protein_string += aa


print(protein_string)
