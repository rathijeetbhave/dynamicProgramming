# Given a sequence of matrices A1,A2,...,An, insert parentheses so that the product of the matrices,
# in order, is unambiguous and needs the minimal number of multiplication

# This subproblem finds the minimum number of multiplications to multiply matrices A1...An. Size of matrix Ai is given as P(i-1)xPi
# Input will consist an array P as [P0,...Pn] with n+1 values which denote sizes of matrices A1 ... An

p = [30, 35, 15, 5, 10, 20, 25] #-- for matrices A1 ... A6

#-- Recurrence relation = M[i,j] = 0 if i == j else {min(m[i,k] + m[k+1,j] + p(i-1)*p(k)*p(j)) for k in [i,...,j-1]}

def minimum_multiplications(i, j) :
    global p
    if i == j :
        return 0
    min_calc = 10000000
    for k in range(i, j) :
        m = minimum_multiplications(i, k) + minimum_multiplications(k+1, j) + p[i-1]*p[k]*p[j]
        min_calc = min(min_calc, m)

    return min_calc

def diagonal_matrix(n) :
    m = []
    for i in range(n) :
        row = []
        for j in range(n) :
            if i == j :
                row.append(0)
            else :
                row.append(10000000)
        m.append(row)

    return m

#--Some Error
def minimum_multiplications(n) :
    m = diagonal_matrix(n)
    for i in range(n) :
        for j in range(i+1) :
            if i != j :
                for k in range(j, i) : #j=0, i=1, k=0
                    temp = m[j][k] + m[k+1][i] + p[j]*p[k+1]*p[i+1]
                    m[j][i] = min(m[j][i], temp)

    for row in m :
        print row
    return m[0][n-1]



#print diagonal_matrix(6)
print minimum_multiplications(6)

