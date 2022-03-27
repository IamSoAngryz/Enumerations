"""
Exceptions hierachy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
Erori in Python:
1. erori de sintaxa - determinate de nerespectarea sintaxei (erori de parsare)
2. exceptii - erori de rulare / executie (run-time errors)

Exceptie (exception) = un eveniment care apare in timpul executiei programului
                    si care determina oprirea rularii
Exemple(subclare ale unei clase pe baza BaseException):
TypeError - concatenare string cu int (' ' + 3)
ZeroDivisionError - impartire la zero
NameError - o variabila nu a fost definita (declarata)
BaseException - clasa de baza (superclasa) pentru exceptii build-in
Toate exceptile sunt instante ale unor clase derivate din BaseException
Ierahia exceptilor (exception hierarchy) - utila in tratarea exceptilor,
construirea unei cai alternative care va fi urmata cand o exceptie este lansata
Pe baza ierarhiei, cand prindem o exceptie vom prinde toate erorile derivate
din acea exceptie (instantele claselor derivate din clasa exceptilor pe care
o prindem)

Python are un mecanism de identificare si rezolvare a erorilor (exceptilor)
care apar in timpul executiei unui program:
blocul try except - anticipeaza o exceptie si previne oprirea executiei

"""


def impartire(x, y):
    # if y != 0:
    #     return x / y
    # else:
    #     return 'Impartire la zero'
    try:
        return x / y
    except ZeroDivisionError:
        return 'Impartire la zero'


x = 2
print('Testam exceptii')
print('Mesaj')
print(impartire(4, 3))
print(impartire(4, 0))

# print('un string' + 2)   # TypeError
# z = x + y
