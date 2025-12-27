import re
#1
def controllo_mac(mac):

    espressione = r"([0-9A-Fa-f]){2}(:[0-9A-Fa-f]{2}){5}"
    valido = re.match(espressione,mac)

    if valido:
        valido = True
    else:
        valido = False

    return valido

#2
def controllo_testo(testo):

    espressione = r"\b[A-Z]{2,}\b"
    lista_validi = re.findall(espressione,testo)

    return lista_validi

#3
def controllo_orario(orario):

    espressione = r"(([0-1][0-9])|(2[0-3])):[0-5][0-9]"
    valido = re.match(espressione,orario)

    if valido:
        valido = True
    else:
        valido = False

    return valido

#4
def controlla_testo_misto(testo):

    espressione = r"[0-9]{2,}"
    lista_validi = re.findall(espressione,testo)

    return lista_validi

#5
def controlla_prezzo(prezzo):

    espressione = r"[0-9]+,[0-9]{2}€?"
    valido = re.match(espressione,prezzo)

    if valido:
        valido = True
    else:
        valido = False

    return valido

#6
def controlla_paragrafo(testo):
    espressione = r"\n[A-Z][a-z]{0,}"
    lista_validi = re.findall(espressione,testo)

    return lista_validi

##1
print("#1")
mac_giusto = "AA:00:CC:DD:99:FF"
mac_sbagliato = "AG:40:CC:DD:99:FF"

valido1= controllo_mac(mac_giusto)
valido2= controllo_mac(mac_sbagliato)

print(valido1)
print(valido2)

##2
print("#2")
testo = "test TEST re RE CIAO ESEMPIO SSH FTP sFTP tFTP"
lista_validi = controllo_testo(testo)

print(lista_validi)

##3
print("#3")
orario1 = "13:40"
orario2 = "08:99"

orario_valido1 = controllo_orario(orario1)
orario_valido2 = controllo_orario(orario2)

print(orario_valido1)
print(orario_valido2)


##4
print("#4")
testo_misto = "ID45A23XID45A23X"

lista_numeri = controlla_testo_misto(testo_misto)
print(lista_numeri)

##5
print("#5")
prezzo1 = "12121,34"
prezzo2 = "12,2"

prezzo_valido1 = controlla_prezzo(prezzo1)
prezzo_valido2 = controlla_prezzo(prezzo2)

print(prezzo_valido1)
print(prezzo_valido2)

##6
testo_paragrafo = """
RegExr was created by gskinner.com.

Edit the Expression & Text to see matches.

Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported,
validate your expression with Tests mode.

The side bar includes a Cheatsheet, full Reference, and Help. 

You can also Save & Share with the Community and view patterns you create or favorite in My Patterns.

Explore results with the Tools below. Replace & List output custom results. Details lists capture groups.

Explain describes your expression in plain English.
"""
print("#6")
lista_parole = controlla_paragrafo(testo_paragrafo)

print(lista_parole)