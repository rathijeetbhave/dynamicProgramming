# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
# how many ways can we make the change? The order of coins doesn't matter.
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.


# idea here is to divide the solution set into two parts. One which contains the mth coin and other which contains atleast one instance of that coin.

def change(coins, num_coins, s) :
    if s == 0 :
        return 1

    if s < 0 :
        return 0

    if num_coins <= 0 and s > 0 :
        return 0

    return change(coins, num_coins-1, s) + change(coins, num_coins, s-coins[num_coins-1])


print change([1,2,3], 3, 4)

def change_dp(coins, s) :
    matrix = [[0]*(s+1) for _ in range(len(coins)+1)]

    for row in matrix[1:] :
        for 


