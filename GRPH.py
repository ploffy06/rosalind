from helpers.file_read_helper import read_fasta

def overlap_graph(records):
    k = 3
    overlap_graph = []

    for r1 in records:
        for r2 in records:
            if r1.seq == r2.seq:
                continue
            if r1.seq[-3:] == r2.seq[:3]:
                overlap_graph.append(f'{r1.name} {r2.name}')

    return overlap_graph

if __name__ == '__main__':
    records = read_fasta()
    overlap_graph = overlap_graph(records)

    print("\n".join(overlap_graph))
