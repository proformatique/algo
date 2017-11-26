#v:"N,k,n"
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
#i:
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  ##bp:
    print(msg.format(n,n2))

##s:
#v:"n,n2"
N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
#i:
for i in range(1, N):
    n2 = n * i * k  ##bp:
    print(msg.format(n, i*k, n2))

##s:
#v:"k,n,n2"
N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
#i:
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  ##bp:
    print(msg.format(n, k, n2))

##s:
#v:"n,n2"
N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
#i:
for i in range(N):
    n2 = n * 9 + k - (i + 1) ##bp:
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i

##s:
#v:"n,n2"
N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
#i:
for i in range(1, N):
    n2 = n * i  ##bp:
    print(msg.format(n, i ,n2))

##s:
#v:"n,n2"
N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
#i:
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  ##bp:
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)

##s:
#v:"n,n2"
N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
#i:
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  ##bp:
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)

##s:
#v:"n,n2,n*n2"
N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
#i:
for i in range(1, N):
    n = (n * 10 + k)   ##bp:
    n2 = (n2 * 10 + c)   ##bp:
    print(msg.format(n, n2, n * n2))

##s:
#v:"N,c,n,n2"
N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
#i:
for i in range(1, N):
    n = n * 10 + c   ##bp:
    n2 = n ** 2   ##bp:
    print(msg.format(n ,n2))
