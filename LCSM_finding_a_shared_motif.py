dna_strings = []

with open('data.txt', 'r') as file:
    current_dna_string = ""
    for line in file:
        if line.startswith('>'):
            if current_dna_string:
                dna_strings.append(current_dna_string)
                current_dna_string = ""
        else:
            current_dna_string += line.strip()

    # Append the last DNA string after the loop
    if current_dna_string:
        dna_strings.append(current_dna_string)

def getCommonLongestSubstrings(dna_string_list, dna_string2):
    max_length = 0
    common_substrings = []

    # Find the length of the longest common substring
    for dna_string1 in dna_string_list:
        length = getLongestCommonSubstringLength(dna_string1, dna_string2)
        max_length = max(max_length, length)

    # Extract all substrings of the maximum length
    for dna_string1 in dna_string_list:
        common_substrings.extend(getSubstringsOfLength(dna_string1, dna_string2, max_length))

    return common_substrings

def getLongestCommonSubstringLength(dna_string1, dna_string2):
    len1 = len(dna_string1)
    len2 = len(dna_string2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    max_length = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if dna_string1[i - 1] == dna_string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

def getSubstringsOfLength(dna_string1, dna_string2, length):
    substrings = []
    len1 = len(dna_string1)
    len2 = len(dna_string2)

    for i in range(len1):
        for j in range(len2):
            k = 0
            while (i + k < len1 and j + k < len2 and dna_string1[i + k] == dna_string2[j + k]):
                k += 1
            if k == length:
                substrings.append(dna_string1[i:i + k])
    return substrings

curr_substrings = []
for i in range(len(dna_strings) - 1):
    if i == 0:
        curr_substrings = getCommonLongestSubstrings(
            [dna_strings[i]], dna_strings[i + 1]
        )
    else:
        curr_substrings = getCommonLongestSubstrings(
            curr_substrings, dna_strings[i + 1]
        )

print(curr_substrings)