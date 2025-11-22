from re import Pattern,compile
from stringa_input import creazione_stringa


class espressione_regolare:
    def __init__(self, espressione):
        self.espressione = compile(espressione)
        self.stringa = creazione_stringa.stringa()

    def match_stringa(self):
        corrisponde = Pattern.match(self.espressione, self.stringa)
        if corrisponde:
            return "match"
        else:
            return "mismatch"

# controllo di una data gg/mm/20aa
espressione_regolare1 = espressione_regolare(
    r"(0[1-9]|[1-2][0-9]|3[0-1])\/(0[0-9]|1[0-2])\/20(\d{2})"
)
risultato = espressione_regolare1.match_stringa()
print(risultato)
