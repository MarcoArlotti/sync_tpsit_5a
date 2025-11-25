Creare nel linguaggio di programmazione che preferisci (PHP, C#, Java, ...) una applicazione che estrae 3 nominativi per l'interrogazione degli studenti di una classe.
Quindi prima di tutto vanno inseriti tutti i nominativi (nome e cognome) in una struttura dati a vostra
scelta.
La procedura richiede come input una stringa di testo e in base a questa applica una espressione regolare
che filtra i nominativi nella suddetta struttura dati.

Tra i nominativi filtrati l'applicazione ne estrae 3, quindi:

    se ci sono più di 3 nominativi filtrati ne estrae 3 in maniera randomica
    se ce ne sono meno di 3 prende tutti i nominativi filtrati.

L’espressione regolare viene generata utilizzando la stringa di testo di input con la seguente priorità:

    come atomo, se non trova nessun match
    come gruppo, se non trova nessun match
    come range di maiuscole e minuscole più lo spazio.

Esempio se la stringa di input fosse “ciao”:

    prima controllo se esiste una sottostringa esatta del nome + cognome che fa match (Luca Ciaone
    non matcha, Matteo Parmiciaoli matcha), in caso negativo
    controllo che il nome + cognome contengano il gruppo di caratteri (Claudio Rossi non matcha, Luigi
    Macioni matcha), in caso negativo
    controllo che il nome + cognome contengano il range di caratteri che va dal carattere minimo al
    massimo, nel nostro esempio a-o A-O e lo spazio (Gino Ricci non matcha, Gino Belli matcha)

Fare dei test di casi affinchè vengano utilizzate a turno tutte le priorità (quindi almeno 3 test).

N.B.: il tutto va versionato in un repository nel vostro GitHub.
La consegna prevede il link al vostro repository!