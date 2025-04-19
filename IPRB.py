from helpers.file_read_helper import read_single_line

# The probability that two randomly selected mating organisms will display dominant phenotype
# # Assuming any two organisms can mate

# k, m, n = homozygous dominant, heterozygous, homozygous recessive
# 25 28 20 -> 0.785198
# 2 2 2 -> 0.78333

def prob_dominant(k, m, n):
    total = k + m + n

    d_branch = (k/total)*((k-1)/(total-1)) + (k/total)*(m/(total-1)) + (k/total)*(n/(total-1))
    m_branch = (m/total)*((m-1)/(total-1))*(3/4) + (m/total)*(k/(total-1)) + (m/total)*(n/(total-1))*(1/2)
    n_branch = (n/total)*((n-1)/(total-1))*0 + (n/total)*(m/(total-1))*(1/2) + (n/total)*(k/(total-1))
    p_dominant = d_branch + m_branch + n_branch

    return p_dominant


if __name__ == '__main__':
    k, m , n = map(int, read_single_line())
    p_dominant = prob_dominant(k, m, n)

    print(f"{p_dominant:4f}")
