file = open('data.txt', 'r')

fillers = ["{", "}", " ", ",", "\n"]
sets = file.readlines()
n = int(sets[0].replace("\n", ""))
line2 = sets[1].strip()
line3 = sets[2].strip()
A = set(map(int, line2[1:-1].split(', ')))
B = set(map(int, line3[1:-1].split(', ')))
U = set([i for i in range(1, n+1)])

AuB = A.union(B)
AinB = A.intersection(B)
AdiffB  = A.difference(B)
BdiffA = B.difference(A)
Ac = U.difference(A)
Bc = U.difference(B)

print(AuB)
print(AinB)
print(AdiffB)
print(BdiffA)
print(Ac)
print(Bc)
