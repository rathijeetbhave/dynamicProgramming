# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing order.
# For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

# Here we will maintain a temp array that will store the values of lis till that index.
# Then we just check if curr elem is smaller then the elem for which we are finding lis, then we can add 1 to lis of curr element.
# In the end we will pick max value from the temp array to get the overall lis.

def lis(a) :
    temp = [1]*len(a) # min lis at any index is 1, the element itself

    for i in range(1, len(a)) :
        for j in range(i) :
            if a[j] < a[i] :
                temp[i] = max(temp[i], temp[j] + 1)

    return temp

def print_ans(temp, a) :
    index = temp.index(max(temp))
    lastIndex = index
    ans = [a[index]]
    while index >= 0 :
        if temp[index] == temp[lastIndex] - 1 :
            ans.append(a[index])
            lastIndex = index
        index -= 1

    return ans

a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
a = [3, 10, 2, 1, 20]
a = [3, 2]
a = [50, 3, 10, 7, 40, 80]
print print_ans(lis(a), a)


