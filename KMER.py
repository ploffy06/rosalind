from helpers.file_read_helper import read_fasta
import itertools

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def kmer(k, dna):
    k_mers = []
    for perm in itertools.product('AGTC', repeat=int(k)):
        str_perm = ''.join(p for p in perm)
        k_mers.append(str_perm)

    k_mers = sorted(set(k_mers))

    a = []
    for m in k_mers:
        a.append(occurrences(dna, m))

    return a

if __name__ == '__main__':
    dna = read_fasta().seq
    four_mer = kmer(4, dna)

    print(' '.join(map(str, four_mer)))

