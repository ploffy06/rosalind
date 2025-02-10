file = open('data.txt', 'r')

input_nums = [int(n) for n in file.read().split()]
pi = input_nums[1:]

file.close()

def longest_increasing_subsequence(nums):
    n = len(nums)
    # Initialize an array to store the length of the longest increasing subsequence ending at each index
    dp = [1] * n

    # Iterate over the elements to compute the longest increasing subsequence length at each index
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum length of the increasing subsequence
    max_length = max(dp)

    # Backtrack to construct the longest increasing subsequence
    lis = []
    curr_length = max_length
    for i in range(n - 1, -1, -1):
        if dp[i] == curr_length:
            lis.append(nums[i])
            curr_length -= 1

    # Return the longest increasing subsequence
    return lis[::-1]

def longest_decreasing_subsequence(nums):
    # Reverse the permutation to find the longest decreasing subsequence
    return longest_increasing_subsequence(nums[::-1])[::-1]


# Find the longest increasing and decreasing subsequences
increasing_subsequence = longest_increasing_subsequence(pi)
decreasing_subsequence = longest_decreasing_subsequence(pi)

print(' '.join(map(str, increasing_subsequence)))
print(' '.join(map(str, decreasing_subsequence)))
