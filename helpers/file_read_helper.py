from Bio import SeqIO

def read_single_line():
    file = open("./data.txt", "r")
    line = file.readline().split()
    file.close()

    return line[0] if len(line) == 1 else line

def read_lines():
    file = open("./data.txt", "r")
    lines = file.readlines()
    file.close()

    lines = (line.replace("\n", "") for line in lines)

    return lines

def read_fasta():
    records =  list(SeqIO.parse("./data.fasta", "fasta"))
    return records[0] if len(records) == 1 else records