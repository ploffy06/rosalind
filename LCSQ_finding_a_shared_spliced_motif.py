from helper import getDNAStringsList

dna_strings = getDNAStringsList()
s = dna_strings[0]
t = dna_strings[1]

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    # initialize the table with 0's
    lcs_table = [[0]*(n+1) for i in range(m+1)]

    # fill the table using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i][j-1], lcs_table[i-1][j])

    # find the longest common subsequence by backtracking the table
    lcs = ""
    i = m
    j = n
    while i> 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_table[i-1][j] >lcs_table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

print(lcs(s, t))

