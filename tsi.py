def nombre_de_fermat(n) -> int:
    fn = 2 ** 2 ** n + 1
    return fn

def produit(n) -> int:
    prod = 1# R. I
    for k in range(n):
        prod *= nombre_de_fermat(k) # Construction
    return prod # R. Final

def verif(n) -> bool:
    res = produit(n) == nombre_de_fermat(n+1) -2
    return res 
  
