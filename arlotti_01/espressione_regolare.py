import re
from stringa_input import creazione_stringa
class espressione_regolare:
    def __init__(self,espressione):
        self.espressione = re.compile(espressione)
        self.stringa = creazione_stringa.stringa()

    def match(self):
        corrisponde = bool(re.pattern.match(self.espressione,self.stringa))
        if corrisponde:
            return "match"
        else:
            return "mismatch"

espressione_regolare1 = espressione_regolare(r"(0[1-9]|[1-2][0-9]|3[0-1])\/(0[0-9]|1[0-2])\/20(\d{2})")
risultato = espressione_regolare.match()
print(risultato)