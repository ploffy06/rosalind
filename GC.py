from helpers.file_read_helper import read_fasta

def gc_content(dna):
    gc_count = 0

    for base in dna:
        if base in ["G", "C"]:
            gc_count += 1

    return (gc_count / len(dna)) * 100

def find_highest_gc(records):
    gc_contents = {}

    for record in records:
        gc_contents[record.name] = gc_content(record.seq)

    gc_key = max(gc_contents, key=gc_contents.get)
    return gc_key, gc_contents[gc_key]

if __name__ == '__main__':
    records = read_fasta()
    id_code, percentage = find_highest_gc(records)
    print(f"{id_code}\n{percentage:6f}")
