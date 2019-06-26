try:
    f = open('data0.txt', 'r')
    a = 8 / 0
except FileNotFoundError:
    print('Vérifiez le fichier')
except Exception:
    print('/!\\')
else:
    c = f.read()
    print(c)
    f.close()
finally:
    print('Menu')
    