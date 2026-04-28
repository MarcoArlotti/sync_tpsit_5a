4. Realizza una pagina web in tecnologia AJAX che consenta di visualizzare il prezzo e le caratteristiche tecniche dei prodotti di un’azienda di informatica.

La pagina è costituita da un form contenente un campo di testo editabile dall’utente.

Il campo di testo deve consentire all’utente di inserire il codice identificativo del prodotto di interesse.

Il codice è costituito da una stringa composta da un carattere alfabetico seguito da tre caratteri numerici. 

Il form inoltre è dotato di un bottone che consente di inviare la request al server;
a seguito della pressione del bottone la pagina deve:
   a. verificare che il codice identificativo del prodotto immesso dall’utente rispetti il formato specificato;

   b. nel caso in cui il codice identificativo del prodotto verifichi il formato specificato, si chiede di inserire sotto il form una lista puntata in cui vengano riportati prezzo e caratteristiche del prodotto cercato.
   
   Per semplicità assumiamo che il prodotto sia sempre presente sul server e che i dati che questi ci restituisce siano in formato XML e organizzati come segue:

```xml
<?xml version='1.0' encoding='UTF-16'?>
<prodotto>
<prezzo> prezzo </prezzo>
<marca> marca </marca>
<modello> modello </modello>
</prodotto>
```

dove prezzo, marca e modello rappresentano rispettivamente il prezzo del prodotto, la sua marca e il suo modello.

Le informazioni devono essere richieste al server in modo asincrono tramite una chiamata GET e passando il codice del prodotto richiesto;

