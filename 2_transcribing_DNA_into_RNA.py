DNA = "GCATTAAGATGCGAATTCGAGTATCAATTTTCGTCCGTCTACACACGTAGCTATGATCTCTACCCTGGTTTGCAGGTCGACACTGACCAGTAGGAGCGTCCGACGTACGAAGCCATGGTTTTTTAGTAGGAGAATACCGATAGGCGCGGCAACTCACGGCATGTGCCGGTGAGACTGGGCGATTAAGGCAGTATTCGACGATCTACAGGGTGGGACCGCATGTCTTGAGATGACAAGCTTCTCCGCGTAACTGTTAATCGGATCCCATAGGAGAACGATTGATGATGGTCGTGGTTTACGGCTTGACGTGCCACCTGAAGCGACCCATACTTAAGGTACGAAGTTTGATAATTCCCCCGCTGATCCCAGAGTATCATGGGTATGAAGAGGAAAGTCTACGGTACAACACAGCAGAGAGTACGCTACCTATAAAAATCTAGCATACCCATGAGAGGTTCCCTACACCATGGCTGGCCAATGAAACTTACTGTCCATTTGTTTCCCATGTTAGCTGTAAGTATTTGACTATGTTGTACGCGGGGAATTCATAGTCATTAGTAAATGGCCATTGCATCGAACATTTGCTTGGGAGTCTTAAATGCGCGGAATCATAGTTTACCTATCATTGATGACCCAGAGGCGAATACAGGCTCTGTGCTAGCCGGAAGGCGTTATACCAAAACTCGCACTAAGTAATTCGCGTGCGCCCAAAGCCGTACCAAACGGTATCCAGGCGAGTGGCGAACCTCCCGATAGTTACACCAGGGTTTGACCGTGGGCCCCGGCACGATCCACTACGGCTCACTTGAAGGCATATTGCAACGGCCTAGAGGGGGTTCCCGGGTCGTCGGGGGCACAATGGTAGCAAAACCCTCGACACCAGCCTACGTTTTACATTCA"
RNA = ""
for base in DNA:
    if base == "T":
        RNA += "U"
    else:
        RNA += base

print(RNA)
