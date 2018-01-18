def zigzag(mt):
    """
    >>> n = 5
    >>> mt = [[0] * n for _ in range(n)]
    >>> zigzag(mt)
    >>> printf(mt)
    +--+--+--+--+
    |01|02|06|07|
    +--+--+--+--+
    |03|05|08|13|
    +--+--+--+--+
    |04|09|12|14|
    +--+--+--+--+
    |10|11|15|16|
    +--+--+--+--+
    >>> somme(mt)
    """
    n = len(mt)
    a = 1
    for i in range(n):
        if i % 2 == 0:
            pas_i = -1
            pas_j = 1
            i_d = i
            j_d = 0
        else:
            pas_i = 1
            pas_j = -1
            i_d = 0
            j_d = i
        for p in range(i + 1):
            mt[i_d + p * pas_i][j_d + p * pas_j] = a
            a += 1
    for j in range(1, n):
        if j % 2 != 0 and n % 2 == 0:
            pas_i = -1
            pas_j = 1
            i_d = n - 1
            j_d = j
        else:
            pas_i = 1
            pas_j = -1
            i_d = j
            j_d = n - 1
        for p in range(n - j):
            mt[i_d + p * pas_i][j_d + p * pas_j] = a
            a += 1


def printf(M):
    line = "{:0>2}|" * len(M[0])
    line2 = "{:0>2}+" * len(M[0])
    print('+' + line2.format(*(['--'] * len(M[0]))))
    for l in M:
        print('|' + line.format(*l))
        print('+' + line2.format(*(['--'] * len(l))))


def somme(M):
    n = len(M)
    m = len(M[0])
    for j in range(m):
        s = 0
        for i in range(n):
            s += M[i][j]
        print(s, end=' ; ')


if __name__ == '__main__':
    import doctest as dt
    dt.testmod()
