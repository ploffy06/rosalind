"""
Copy the data into a file called data.txt
be really careful that the DNA strings are all in one line as well
as I use the splitlines method

This will then write to another file called result.txt

Rosalind is slightly annoying in that you have no clue what the dataset will look like
sometimes D:
"""
file = open("data.txt", "r").read().splitlines()
arr = [[0 for i in file[1]] for i in range(4)]

for i, line in enumerate(file):
    if i % 2 == 0:
        continue
    for j, char in enumerate(line):
        if char == "A":
            arr[0][j] += 1
        elif char == "C":
            arr[1][j] += 1
        elif char == "G":
            arr[2][j] += 1
        elif char == "T":
            arr[3][j] += 1

f = open("result.txt", "a")
for i in range(len(arr[0])):
    max_base = 0
    max_counts = arr[0][i]

    if arr[1][i] > max_counts:
        max_base = 1
        max_counts = arr[1][i]
    if arr[2][i] > max_counts:
        max_base = 2
        max_counts = arr[2][i]
    if arr[3][i] > max_counts:
        max_base = 3
        max_counts = arr[3][i]

    if max_base == 0:
        f.write("A")
    elif max_base == 1:
        f.write("C")
    elif max_base == 2:
        f.write("G")
    elif max_base == 3:
        f.write("T")
f.write("\n")

for base, counts in enumerate(arr):
    if base == 0:
        f.write("A: ")
    elif base == 1:
        f.write("C: ")
    elif base == 2:
        f.write("G: ")
    elif base == 3:
        f.write("T: ")
    for num in counts:
        f.write(f"{num} ")
    f.write("\n")


