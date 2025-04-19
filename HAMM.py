from helpers.file_read_helper import read_lines

def hamming_distance(s, t):
    hamming_distance = 0

    for s_ntide, t_ntide in zip(s, t):
        if s_ntide != t_ntide:
            hamming_distance += 1

    return hamming_distance

if __name__ == '__main__':
    s, t = read_lines()
    distance = hamming_distance(s, t)

    print(distance)
