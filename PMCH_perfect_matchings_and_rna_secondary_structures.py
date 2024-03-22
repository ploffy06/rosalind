from helper import getDNAStringsList

s = getDNAStringsList()[0]
basepairs_au = s.count('A')
basepairs_gc = s.count('G')

p_au = 1
for i in range(1, basepairs_au+1):
    p_au *= i

p_gc = 1
for i in range(1, basepairs_gc+1):
    p_gc *= i

print(p_au * p_gc)