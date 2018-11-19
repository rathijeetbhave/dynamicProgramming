# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

val = [60, 100, 120]
wt = [10, 20, 30]
w = 50

subset = [[0]*(w+1) for i in range(len(val)+1)]

for i in range(len(val)+1) :
    subset[i][0] = 0

for j in range(w+1) :
    subset[0][j] = 0

for i in range(1, len(val)+1) :
    for j in range(1, w+1) :
        if j < wt[i-1] :
            subset[i][j] = subset[i-1][j]
        else :
            subset[i][j] = max(subset[i-1][j-wt[i-1]] + val[i-1], subset[i-1][j])

print subset[len(val)][w]
# for row in subset :
    # print row

