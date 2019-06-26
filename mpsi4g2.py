def puissance(a, n):
    produit = 1
    for i in range(n):
        produit = produit * a
    return produit

print(puissance(5, 2))