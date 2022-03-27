"""
User-defined exceptions (Exceptii definite de utilizator)
Exceptile sunt:
- build-in (incorporate / predefinite, derivate din BaseException)
- user-defined (derivate prin clase definite de utilizator din Exception)

Sintaxa:
    class Exceptie_definita_de_utilizator(Exception):
        pass
Pentru a crea exceptii user-defined este recomandat sa creeam o clasa
de comuna de baza pentru erori
Conventie de deumite a claselor derivate: sa se termina in Error

Generarea unei exceptii definite de utilizator se realizeaza manual cu 
    raise Nume_Clasa_Exceptie(mesaj)
"""

# class Error(Exception):
#     """Clasa de baza pentru exceptiile definite de utilizator"""
#     pass

# class MyError(Error):
#     """Clasa pentru o exceptie specifica"""
#     pass

# Cream un script care gestioneaza un cont bancar
#    (identificate prin iban si sold)
# si sa realizar operatii de retragere si depunere din cont
# cu verificarea soldului la retragere
#  -ridicarea unei exceptii daca suma de retras depaseste soldul
#  -ridicarea unei exceptii daca suma de retras depaseste o limita stabilita
#   de banca


class Error(Exception):
    """Clasa de baza pentru exceptiile definite de utilizator"""
    pass


class RetragerePesteSoldError(Error):
    """Clasa pentru o exceptie ridicata atunci cand incercam sa retragem din cont
    o suma care il depaseste soldul
    """
    pass


class RetragerePesteLimitaBancaError(Error):
    """Clasa pentru o exceptie ridicata atunci cand incercam sa retragem din
    cont o suma care depaseste limita stabilita de banca
    """


class Cont:
    """Clasa pentru crearea instantelor de tip cont bancar
    Atribute:
        iban(string): codul IBAN
        sold(float): soldul din contul asociat
    """
    limita_retragere = 500

    def __init__(self, iban, sold):
        self.iban = iban
        self.sold = sold

    def __str__(self):
        return f'Contul {self.iban}, sold: {self.sold}'

    def depune(self, suma):
        """Depune suma in cont
        """
        self.sold += suma

    def retrage(self, suma):
        """Retrage din cont suma, daca este disponibila
        Daca suma depaseste soldul se ridica o eroare RetragerePesteSoldError
        Daca suam depaseste limita retragere se ridica o eroare 
        RetragerePesteLimitaBancaError
        """
        try:
            if self.sold >= suma and suma <= Cont.limita_retragere:
                self.sold -= suma       # permitem retragerea
            elif self.sold < suma:
                raise RetragerePesteSoldError(f'Suma {suma} depaseste soldul')
            else:
                raise RetragerePesteLimitaBancaError(
                    f'Suma {suma} depaseste limita {Cont.limita_retragere}'
                )
        except RetragerePesteSoldError as exceptie:
            print(f'{exceptie.__class__.__name__}: {exceptie}')
        except Exception as exceptie:
            print(f'{exceptie.__class__.__name__}: {exceptie}')
    
    @staticmethod
    def limita():
        # return Cont.limita_retragere
        return __class__.limita_retragere


def main():
    cont = Cont('RO23232', 200)
    print(cont)
    cont.retrage(100)
    cont.depune(1000.5)
    print(cont)
    cont.retrage(600)       # ridica o eroare de limita
    cont.retrage(450)
    cont.retrage(450)
    print(cont)
    cont.retrage(350)       # ridica o eroare de sold
    print(cont)
    print(f'Limita retragere: {Cont.limita()}')


if __name__ == '__main__':
    main()
