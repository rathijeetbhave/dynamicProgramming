# Given two sequences, find the length of longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.


a = "ABCDGH"
b = "AEDFHR"

def lcs(s1, s2) :
    if not s1 or not s2 :
        return 0

    if s1[0] == s2[0] :
        return 1 + lcs(s1[1:], s2[1:])
    else :
        return max(lcs(s1, s2[1:]), lcs(s1[1:], s2))

print lcs(a, b)

# DP Solution

#a = "AGGTAB"
#b = "GXTXAYB"
def dp_lcs(s1, s2) :
    soln = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

    for i in range(1, len(s2)+1) : # rows are chars of s2
        for j in range(1, len(s1)+1) : # cols are chars of s1
            if s1[j-1] == s2[i-1] :
                soln[i][j] = 1 + soln[i-1][j-1]
            else :
                soln[i][j] = max(soln[i][j-1], soln[i-1][j])

    print s1, s2
    for row in soln :
        print row

    return soln
    #return soln[len(s2)][len(s1)]

# we select the character only when we go diagonally upwards
def print_str(matrix, s1) :
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1

    s = ''
    while rows >= 0 and cols >= 0 :
        if matrix[rows][cols] == matrix[rows-1][cols] :
            rows -= 1
        elif matrix[rows][cols] == matrix[rows][cols-1] :
            cols -= 1
        elif matrix[rows][cols] == matrix[rows-1][cols-1] + 1 :
            s = s1[cols-1] + s
            rows -= 1
            cols -= 1

    return s

print print_str(dp_lcs(a, b), a)
