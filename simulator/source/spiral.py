#v:"i,j,n"
N = 5
M = [[0] * N for i in range(N)]
i, j = 0, 0
k = 0
n = 1
#i:
for n in range(1, N**2+1):
    if i == 0:
        j = 0
        i = k
        k += 1
    elif j < i:
        j += 1
    else:
        i -= 1
    M[i][j] = n ##bp:

#A:
print(M)
    
    
##s:
T = (153, 1634, 54748, 548834, 1741725, 24678050, 146511208, 4679307774, 82693916578)
for i, n in enumerate(T):
    N = n
    s = 0
    msg = ''
    while N > 0:
        a = N%10
        k = i + 3
        msg += str(a) +'^'+str(k) + (' + ' if N // 10 > 0 else '')
        s += a ** k
        N //= 10
    if s == n:
        print('{:10} = {}'.format(n,msg))
        
       
       