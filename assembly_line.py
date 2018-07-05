a = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
t = [[2,3,1,3,4],[2,1,2,2,1]]

e = [2,4]

x = [3,4]

f1 = [9]
f2 = [12]
def shortest_time(a, t, e, x, n) :
    for i in range(1, n) :
        f1.append(min(f1[i-1], f2[i-1] + t[1][i-1]) + a[0][i])
        f2.append(min(f2[i-1], f1[i-1] + t[0][i-1]) + a[1][i])

    return min(f1[n-1] + x[0], f2[n-1] + x[1])



def shortest_time_recursive(n, line) :
    global a, e, t, x

    if n == 0 :
        if line == 1 :
            return e[0] + a[0][0]
        else :
            return e[1] + a[1][0]

    f1 = 10000
    f2 = 10000
    if line == 1 :
        f1 = min(shortest_time_recursive(n-1, 1) + a[0][n], shortest_time_recursive(n-1, 2) + t[1][n-1] + a[0][n])
    else :
        f2 = min(shortest_time_recursive(n-1, 2) + a[1][n], shortest_time_recursive(n-1, 1) + t[0][n-1] + a[1][n])

    return min(f1, f2)

memo_f1 = {}
memo_f2 = {}
def shortest_time_with_paths(n, line) :
    global a, e, t, x, memo_f1, memo_f2

    key = line*10 + n
    if line == 1 :
        if key in memo_f1 :
            return memo_f1[key]
    else :
        if key in memo_f2 :
            return memo_f2[key]

    if n == 0 :
        if line == 1 :
            print "used station {} from line {}".format(n+1, 1)
            return e[0] + a[0][0]
        else :
            print "used station {} from line {}".format(n+1, 2)
            return e[1] + a[1][0]

    f1 = 10000
    f2 = 10000
    if line == 1 :
        t1 = shortest_time_with_paths(n-1, 1) + a[0][n] 
        t2 = shortest_time_with_paths(n-1, 2) + t[1][n-1] + a[0][n]
        if  t1 < t2 :
            print "used station {} from line {}".format(n+1, 1)
            f1 = t1
        else :
            print "used station {} from line {}".format(n+1, 2)
            f1 = t2

        memo_f1[key] = f1

    else :
        t1 = shortest_time_with_paths(n-1, 2) + a[1][n]
        t2 = shortest_time_with_paths(n-1, 1) + t[0][n-1] + a[1][n]
        if  t1 < t2 :
            print "used station {} from line {}".format(n+1, 2)
            f2 = t1
        else :
            print "used station {} from line {}".format(n+1, 1)
            f2 = t2

        memo_f2[key] = f2


    return min(f1, f2)

import time
start = time.time()
print shortest_time_with_paths(5, 1)
print memo_f1
print memo_f2
#print min(shortest_time_with_paths(5, 1) + x[0], shortest_time_with_paths(5, 2) + x[1])
#print shortest_time(a, t, e, x, 6)
#print (time.time() - start)*10000

        


