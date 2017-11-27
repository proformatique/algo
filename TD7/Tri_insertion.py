def tri_insertion(T):
    for i in range(1, len(T)):
        j = i
        temp = T[j]                                     ;print('Mal placé ?', temp, i)
        while j > 0 and temp < T[j-1]:
            T[j] = T[j-1]                               ;print('Décalage de ', T[j-1], ' de ', j-1, ' à ', j, T)
            j -= 1
        T[j] = temp
...                                                     ;print('Non!' if i == j else 'Insertion de ', temp, ' de ', i, ' à ', j, T)


T = [1, 4, 2, 7, 0, 8]
tri_insertion(T)
print(T)