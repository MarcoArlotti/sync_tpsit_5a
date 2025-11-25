import random
import re


class estrai_numeri:
    def __init__(self, lista_alunni):
        self.lista_alunni = lista_alunni

    def cerca_alunni(self,input):
        contatore = 0
        lista_papabili = []
        for alunno in self.lista_alunni:
            risultato = re.match(string = alunno,pattern = input)
            if risultato:
                contatore = contatore + 1
                lista_papabili.append(alunno)

        if contatore > 3:
            self.estrai_numero(lista_papabili,3)
        else:
            re.

    def estrai_numero(self,lista_alunni,volte):
        lista_scelti = []
        lista_buffer = lista_alunni
        for i in range(volte):
            risultato = random.choice(lista_buffer)
            lista_scelti.append(risultato)
            lista_buffer.remove(risultato)
        return lista_scelti

alunni = [
    "Marco Rossi",
    "Giulia Bianchi",
    "Luca Verdi",
    "Sara Neri",
    "Paolo Conti",
    "Anna Galli",
    "Francesco Moretti",
    "Chiara Romano",
    "Davide Esposito",
    "Martina De Luca",
    "Stefano Greco",
    "Elisa Marchetti",
    "Alessandro Fontana",
    "Valentina Riva",
    "Giorgio Ferri",
    "Federica Colombo",
    "Simone Villa",
    "Claudia Fabbri",
    "Matteo Ricci",
    "Ilaria Puglisi"
]

estrai1 = estrai_numeri(alunni)
estrai1.cerca_alunni("Arl")
#TODO fare con tutte le 3 casistiche