n = int(input('Entrez le nombre n '))
s = 0 # somme vide
k = 0
while s + k + 1 <= n ** 2:
    k = k + 1
    s = s + k
    
    
print(s, k)
# Methode incrémentale : construction petit à petit du resultat f à poartir d'un resultat initial
# 1 R initial
# 2 Construction
# 3 R Final
