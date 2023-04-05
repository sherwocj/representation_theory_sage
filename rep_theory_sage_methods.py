def f_p(n, m, p):
    'f_p function from James pg. 106'
    a = n+1
    a = a.digits(p)
    b = m.digits(p)
    s = len(a)
    r = len(b)
    if s <= r:
        #print("Error: s must be greater than r")
        return
    else:
        cont = 1
        for i in range(r):
            if a[i] < b[i]:
                cont = 0
                break
        return(cont)              
        
def isirred2(n, j):
    'test if S^(n-j,j) is irreducible in a field of characteristic 2'
    l_k = 0
    while 2^l_k <= j:
        l_k += 1
    if (n-2*j +1) % (2^l_k) == 0:
        return(True)
    else:
        return(False)
        
def SpechtCompFactp(n, m,p):
    'gives list of composition factors for S^(n-j,j) when char(F) = p'
    if 2*m > n:
        print("ERROR")
        return
    else:
        factors = []
        for j in range(0,m+1):
            if f_p(n-2*j, m-j,p) == 1:
                factors.append(j)
        return(factors)
    
    
def dimSpecht(n, j):
    'dimension of S^(n-j,j)'
    return(binomial(n, j)-binomial(n, j-1))

def dimIrred(n,j,p):
    'dimension of D^(n-j,j)'
    if 2*j >= n:
        print('ERROR')
        return
    comps = SpechtCompFactp(n,j,p)
    dim_full = dimSpecht(n,j)
    if comps == [j]:
        return(dim_full)
    else:
        numFacts = len(comps)
        dim = dim_full
        for i in range(numFacts-1):
            dim -= dimIrred(n, ZZ(comps[i]), p)
        return(dim)
    
def subset_intersection(n, k, l, m):
    'Returns a matrix comparing k subsets vs l subsets of an n element set. If an entry has a value of 1 then the corresponding subsets share m elements in common.'
    'Input: n - number of elements in set, k - size of subsets, l - size of subsets, m - size of intersection'
    'Output: A - intersection mtx, each row and collumn represent a different subset of size k or l'
    
    #define collection of subsets
    R = Subsets(n, k)
    S = Subsets(n, l)

    #create matrix with appropriate size
    A = matrix(ZZ, binomial(n,k), binomial(n,l))

    #create empty lists and append subsets
    r = []
    s = []

    for i in R:
        r.append(i)

    for j in S:
        s.append(j)

    #check for size of intersection and adjust value of A if necessary
    for i in range(len(r)):
        for j in range(len(s)):
            if (r[i].intersection(s[j])).cardinality() == m:
                A[i,j]=1
                
    return(A)

def elem_divisors_abbr(A):
    #use sage method to find divisors
    divs = A.elementary_divisors()
    #count how many of each divisor
    D = dict((i, divs.count(i)) for i in divs)
    return(D)