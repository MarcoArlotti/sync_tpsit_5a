Si vuole progettare un sistema informativo per gestire tutte le competizioni sportive organizzate annualmente in una determinata regione. Il sistema deve consentire di archiviare in modo strutturato i dati principali delle manifestazioni, così da poterli rappresentare attraverso un file JSON organizzato in oggetti e liste correlate tra loro.


Di ogni competizione si conoscono il nome ufficiale, la data di inizio (formato yyyy-mm-dd), la data di conclusione (formato yyyy-mm-dd), l’impianto sportivo in cui si svolge e la quota di iscrizione. Ogni competizione è suddivisa in più gare, che possono appartenere a discipline diverse (ad esempio corsa, nuoto, ciclismo o sport di squadra).


Ogni gara è descritta da un titolo, da una data e orario di inizio (formato yyyy-mm-ddThh:mm), da una durata prevista (espressa in hh:mm), da una categoria (ad esempio juniores, senior, pro) e da una breve descrizione del regolamento specifico. Per ciascuna gara si registra l’elenco degli atleti o delle squadre partecipanti.


Degli atleti si memorizzano nome, cognome, data di nascita (formato yyyy-mm-dd), nazionalità e disciplina praticata. Nel caso di sport di squadra, si registrano il nome della squadra, l’anno di fondazione e l’elenco dei giocatori, ciascuno descritto da nome, cognome, data di nascita (formato yyyy-mm-dd) e ruolo in campo. Per ogni gara si possono inoltre memorizzare i risultati finali, indicando posizione in classifica e punteggio ottenuto.


Ogni competizione prevede la presenza di strutture di servizi dedicati agli atleti e al pubblico. Per ciascun servizio si conoscono il nome, la tipologia (ad esempio assistenza medica, ristoro, area tecnica, servizio sicurezza), la posizione all’interno dell’impianto (formato intero) e gli orari di disponibilità (ognuno espresso in hh:mm).


Inoltre per l’intera manifestazione si tiene traccia dei giudici di gara registrando nome, cognome, qualifica e anni di esperienza.


N.B.: Il formato yyyy-mm-ddThh:mm è la rappresentazione standard ISO 8601 per data e ora, che combina anno (4 cifre), mese, giorno, una 'T' come carattere separatore, ore (24h) e minuti.