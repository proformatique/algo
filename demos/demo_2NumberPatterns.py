
# <demo> stop
 # Script 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 


N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 


N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 


N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 


N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 


N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 


N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 


N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 


N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef * acldeo:<6acldef =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    #print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
# msg = 'acldeo:>6acldef^2  =acldeo:^10acldef'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    #print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * acldeo0:<10acldef = acldeo1:^20acldef '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = 'acldeo0:>10acldef * acldeo1:>2acldef = acldeo2:^10acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = 'acldeo0:>10acldef * 9 + acldeo1:<2acldef = acldeo2:<10acldef '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = 'acldeo0:>6acldef * acldeo1:>2acldef = acldeo2:0>7acldef '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = 'acldeo:>6acldef^2 = acldeo:^12acldef '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
# msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    #print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
# msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    #print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
# msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    #print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
# msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    #print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
# msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    #print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
# msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
# msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    #print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))

# <demo> stop
 # Script 
 
N = 9
k = 1
n = 0
msg = '{0:>10} * {0:<10} = {1:^20} '
# Initialisation faite
for i in range(N):
    n = n * 10 + k
    n2 = n ** 2  # BPoint
    print(msg.format(n,n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 12345679
msg = '{0:>10} * {1:>2} = {2:^10} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i * k  # BPoint
    print(msg.format(n, i*k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 1
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    k = i + 1
    n = n * 10 + i
    n2 = n * 9 + k  # BPoint
    print(msg.format(n, k, n2))


# <demo> stop
 # Script 
 

N = 9
k = 9
n = 0
msg = '{0:>10} * 9 + {1:<2} = {2:<10} '
# Initialisation faite
for i in range(N):
    n2 = n * 9 + k - (i + 1) # BPoint
    print(msg.format(n, k -(i+1), n2))
    n = n * 10 + k - i


# <demo> stop
 # Script 
 

N = 11
n = 999999
msg = '{0:>6} * {1:>2} = {2:0>7} '
# Initialisation faite
for i in range(1, N):
    n2 = n * i  # BPoint
    print(msg.format(n, i ,n2))


# <demo> stop
 # Script 
 

N = 7
c = 3
k = 4
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 8
k = 7
c = 6
n = 0
msg = '{:>6}^2 = {:^12} '
# Initialisation faite
for i in range(1, N):
    n2 = (n * 10 + k) ** 2  # BPoint
    print(msg.format(n * 10 + k ,n2))
    n = (n * 10 + c)


# <demo> stop
 # Script 
 

N = 6
k = 7
c = 9
n = 0
n2 = 0
msg = '{:>6} * {:<6} ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = (n * 10 + k)   # BPoint
    n2 = (n2 * 10 + c)   # BPoint
    print(msg.format(n, n2, n * n2))


# <demo> stop
 # Script 
 

N = 6
c = 9
n = 0
n2 = 0
msg = '{:>6}^2  ={:^10}'
# Initialisation faite
for i in range(1, N):
    n = n * 10 + c   # BPoint
    n2 = n ** 2   # BPoint
    print(msg.format(n ,n2))
