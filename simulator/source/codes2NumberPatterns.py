#v:"N,k,n"
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
#i:
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  ##bp:
    #print(msg.format(n,n2))

##s:
#v:"N,k,n"
N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
#i:
for i in range(1, N):
    n2 = n * i * k  ##bp:
    #print(msg.format(n, i*k, n2))

##s:
#v:"N,k,n"
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
#i:
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  ##bp:
    #print(msg.format(n, k, n2))

##s:
#v:"N,k,n"
N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
#i:
for i in range(N):
    n2 = n * 9 + k - (i + 1) ##bp:
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i

##s:
#v:"N,n"
N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
#i:
for i in range(1, N):
    n2 = n * i  ##bp:
    #print(msg.format(n, i ,n2))

##s:
#v:"N,k,n"
N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
#i:
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  ##bp:
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)

##s:
#v:"N,k,n"
N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
#i:
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  ##bp:
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)

##s:
#v:"N,k,n,n2"
N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
#i:
for i in range(1, N):
    n = (n * 10 + k)   ##bp:
    n2 = (n2 * 10 + c)   ##bp:
    #print(msg.format(n, n2, n * n2))

##s:
#v:"N,c,n"
N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
#i:
for i in range(1, N):
    n = n * 10 + c   ##bp:
    n2 = n ** 2   ##bp:
    #print(msg.format(n ,n2))
