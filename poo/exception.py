try:
    code()
except ZeroDivisionError:
    traitement()
except Exception:
    traitement()
else:
    code2()
    
finally:
    code()
    