tab = [2, 5, 4, 2, 9]
j = 0
resultat = 0
# I : resultat == sum(tab[:j])
while j < len(tab):
    # si resultat == sum(tab[:j])
    resultat += tab[j]
    j += 1
    # => I : resultat == sum(tab[:j])
print(resultat)
