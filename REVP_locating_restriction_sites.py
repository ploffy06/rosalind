from helper import getDNAStringsList, getReverseComplement

dna_string = getDNAStringsList()[0]
reverse_palindromes = []

def isReversePalindrome(dna):
    return dna == getReverseComplement(dna)

for idx, base in enumerate(dna_string):
    for i in range(idx+4, len(dna_string)+1):
        if i - idx > 14: break
        if isReversePalindrome(dna_string[idx:i]):
            reverse_palindromes.append((idx+1, i-idx))

for reverse_palindrome in reverse_palindromes:
    print(reverse_palindrome[0], reverse_palindrome[1], sep=' ')