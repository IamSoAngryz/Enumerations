"""
Raising (throwing) exceptions manually
- ridicarea exceptiilor manual
raise - lansam exceptii in functie de context
"""

# conversia unei sume dupa o rata de conversie
rata_conversie = 4.9
suma = input('Suma: ')
try:
    suma = float(suma)
    if suma < 0:
        raise ValueError('Suma nu poate fi negativa')
except ValueError as exceptie:
    print(exceptie.__class__.__name__, ' :', exceptie)
except Exception as exceptie_generica:
    print(exceptie_generica.__class_.__name__, exceptie_generica)
else:
    print(f'Rezultatul conversiei sume {suma} este: {suma * rata_conversie:.2f}')
