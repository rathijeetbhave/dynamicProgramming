# Given an array find if there is a subset with sum S in it.
# Here for each element we have two choices, we can include it in our solution or exclude it.
# if we include it then we have to solve problem of finding subset with sum S - a[i] for smaller array with n - 1 elements.
# if we dont include i'th element then we have to find subset for sum S for n - 1 elements.

# We convert this problem to a yes/no problem of whether i'th element is included in final solution or not.
# we define Q(N, S) as a function which tells us if it is possible to have a sum S with N elements.

# So Q(N, S) = Q(N-1, S) || Q(N-1, S-a[N]) || a[N] == S
# Base case will be Q(1, S) which can be solved by checking a[i] == S for i (- [0...N]

# How can we be sure that we have already calculated Q(N-1, S-a[N]).
# let a be the sum of all -ve numbers in array and b be sum of all +ve numbers. So any sum S will satisfy a <= S <= b
# We will have an array of length (B - A).
# Here we will only consider array with +ve numbers so that A = 0. We dont have to maintain an array of length B as we will be finding sums less than S.
# So we need an array of length S
# refer - https://en.wikipedia.org/wiki/Subset_sum_problem; https://www.youtube.com/watch?v=s6FhG--P7z0

# This will return if such a subset exists. To find the subset we have to find a way to track the elements in DP.

# We maintain a matrix with sum on X and array elem on Y. We keep filling row by row. We check if it is possible to make sum S using elements upto i'th row.
def get_matrix(a, r, c) :
    matrix = [0] * (r+1)
    for i in range(r+1) :
        if i == 0 :
            matrix[i] = [-1] + range(1, c+1)
        else :
            matrix[i] = [a[i-1]] + range(1, c+1)
    return matrix

def sub_sum(a, s) :
    matrix = get_matrix(a, len(a), s)
    # initialise 1st col to True as we can always have sum 0 with an empty set
    # for row in matrix :
        # print row
    matrix = [[False]*(s+1) for _ in range(len(a)+1)]
    for r in range(1, len(a)+1) :
        matrix[r][1] = True

    matrix[1] = [False] * len(matrix[1])

    #set true on 1st index of 1st row as we can have sum 1 with 1st element
    matrix[1][a[0]] = True

    # start filling from 2nd row
    for r in matrix[2:] :
        for c in r[1:] :
            if c - r[0] > 0 :
                matrix[r][c] = matrix[r-1][c] or matrix[r-1][c-r[0]]
            else :
                print r, c
                matrix[r][c] = matrix[r-1][c]

    print matrix

    return matrix[r][c+1]

a = [1,2,4,5,9]
sub_sum(a, 15)


