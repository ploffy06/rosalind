# 25 28 20
k = 25 # homozygous dominant
m = 28 # heterozygous
n = 20 # homozygous recessive
total = k + m + n
 # The probability that two randomly selected mating organisms will produce
 # an individual possessing a dominant allele
 # (and thus displaying the dominant phenotype).
 # Assume that any two organisms can mate.


D_branch = (k/total)*((k-1)/(total-1)) + (k/total)*(m/(total-1)) + (k/total)*(n/(total-1))
M_branch = (m/total)*((m-1)/(total-1))*(3/4) + (m/total)*(k/(total-1)) + (m/total)*(n/(total-1))*(1/2)
N_branch = (n/total)*((n-1)/(total-1))*0 + (n/total)*(m/(total-1))*(1/2) + (n/total)*(k/(total-1))
P = D_branch + M_branch + N_branch
print(f"{P:4f}")