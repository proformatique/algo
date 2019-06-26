    def p1(liste):
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                decision = False
                break
        else:
            decision = True
        return decision
    
    def p2(liste):
        for i in range(len(liste) - 1):
            if liste[i] < liste[i + 1]:
                decision = False
                break
        else:
            decision = True
        return decision
    
    def estenOrdre(liste):
        return p1(liste) or p2(liste)