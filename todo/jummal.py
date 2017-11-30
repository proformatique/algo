T0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
T1 = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
T2 = ['ا', 'أ', 'ٱ', 'إ', 'ٔ', 'ئ', 'ؤ', 'ب', 'آ', 'ج', 'د', 'ه', 'ة', 'و', 'ز', 'ح', 'ط', 'ى', 'ي', 'ئ', 'ك', 'ل', 'م', 'ن', 'س', 'ع', 'ف', 'ص', 'ق', 'ر', 'ش', 'ت', 'ث', 'خ', 'ذ', 'ض', 'ظ', 'غ']



def jummal(t):
    """
    >>> texte = "في الجنة"
    >>> jummal(texte)
    92
    >>> texte = "محمد"
    >>> jummal(texte)
    801
    """
    s = 0
    for c in t:
        s+= T1[T2.index(c)]
    return s

print(jummal(texte))