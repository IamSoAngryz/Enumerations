"""
Try - except - else - finally

Tratarea exceptiilor (identificarea erorilor care apar de-a lungul executiei
programului) este implementat blocul try-except

Sintaxa:
try:
    instructiuni
except:
    instructiuni_tratare_exceptii
else:
    instructiuni_executate_daca_nu_se_ridica_exceptii
finally:
    instructiuni_executate_neconditionat
Regula:
Ordinea blocurilor except trebuie sa respecte ierarhia exceptilor(exception
hierarchy), cele mai specifice (subclasele) trebuie sa fie plasate inaintea
exceptiilor instante ale claselor parinte, generice (mai sus in ierahie, superclase)
as - afisarea exceptiei (erorii)
"""

# Convertim o suma introdusa de la tastatura dupa o rata de conversiei

rata_conversie = 4.9
suma = input('Introduceti suma: ')

try:
    suma = float(suma)      # coversie de la string la float
except ValueError as e:
    print(e.__class__.__name__, e)
except Exception as e:
    print(e)
else:
    print(f'Suma {suma} covertita este: {suma * rata_conversie}')
finally:
    print('Mesaj la final de try except')