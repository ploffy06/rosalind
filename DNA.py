from helpers.file_read_helper import read_single_line
def count_nucleotides(dna):
    a_count, c_count, g_count, t_count = 0, 0, 0,0
    for base in dna:
        if base == "A": a_count += 1
        if base == "G": g_count += 1
        if base == "T": t_count += 1
        if base == "C": c_count += 1

    return a_count, c_count, g_count, t_count

if __name__ == '__main__':
    dna = read_single_line()
    counts = count_nucleotides(dna)

    print(" ".join(map(str, counts)))