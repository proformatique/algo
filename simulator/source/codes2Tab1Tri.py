#v:"i,a[:]"
a , i = [8, 5, 2, 6, 7, 9], 0
#i:
#bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:
a.insert(i,a.pop(a.index(min(a[i:])))); i += 1  ##bp:

#A:
print(a)
