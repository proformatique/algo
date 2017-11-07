def saisie(tab):
    taille = len(tab)
    print('Vous allez saisir', taille, 'valeurs')
    for i in range(taille):
        tab[i] = eval(input('\n\t tab['+str(i)+'] = ? '))


