
def sub_sum_non_dp(a, s) :
    if not a :
        return False

    if s == 0 :
        return True

    for i, elem in enumerate(a) :
        possible = sub_sum_non_dp(a[0:i] + a[i+1:], s-elem) or sub_sum_non_dp(a[0:i] + a[i+1:], s)

    return possible

def sub_sum(a, s) :
    matrix = [[False]*(s+1) for _ in range(len(a)+1)]
    # we can make a sum 0 with any number of elements by selecting an empty set.
    for r in range(len(a)+1) :
        matrix[r][0] = True

    for r in range(1, len(a)+1) :
        for c in range(1, s+1) :
            if c - a[r-1] >= 0 :
                matrix[r][c] = matrix[r-1][c] or matrix[r-1][c-a[r-1]]
            else :
                #print r, c
                matrix[r][c] = matrix[r-1][c]

    for row in matrix :
        print row
    return matrix
    #return matrix[len(a)][s]


def print_ans(matrix, a) :
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1

    ans = []
    while rows > 0 and cols > 0 :
        if matrix[rows][cols] and matrix[rows-1][cols] :
            rows -= 1

        elif matrix[rows][cols] and matrix[rows][cols] == matrix[rows-1][cols-a[rows-1]] :
            #print rows, cols
            ans.append(a[rows-1])
            cols -= a[rows-1]

    return ans

a = [1,2,4,5,9]
a = [10, 7, 5, 18, 12, 20, 15]
print sub_sum_non_dp(a, 15)
#print print_ans(sub_sum(a, 30), a)
