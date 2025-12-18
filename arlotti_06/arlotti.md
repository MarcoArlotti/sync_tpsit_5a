# ESERCIZIO PER CASA, IMPARARE AD USARE _YAML_:
##### ___writted by Arlotti Marco___

## Creazione del file _YAML_:
> I file YAML __non sono eseguibili__ quindi
si possono creare utilizzando qualunque _editor di testo_[^1]

Come consegna bisogna creare una __rubrica__ di alunni che contenga:
- il nome
- il voto pratico
- il voto teorico
- calcolare la media
- un commento del prof sul voto

> analizzando i dati si deduce che __il voto teorico e pratico si ripetano__ più volte,
e visto che si hanno più voti e più alunni __bisogna aggiungere__:
> - __"ID"__ -> Per ogni alunno e voto
> - __"DATA"__ -> Per ogni voto (___opzionale___)

>questa informazione servirà __successivamente per _HTML_ e _XSD___.

[^1]:Programma che permette la modifica di testi semplici
## Il codice del file _YAML_:
``` yaml
rubrica_classe:
  alunno:
    id: !!int 1
    nome: !!str Fabio
    voto_pratico: 
      id: !!int 1
      data: !!str 2025-12-16T14:40:00+01:00
      voto: !!float 6.5
    voto_teorico: 
      id: !!int 1
      data: !!str 2025-12-16T10:40:00+01:00
      voto: !!float 5.0
    media: !!float 5.75
    commento: !!str >
      Fabio ha bisogno di studiare di più
      perchè è una pippa.
```
## Validazione del file _YAML_
>Prima di iniziare a fare il file _XML_ e _XSD_ bisogna controllare che il file _YAML_ sia
scritto __correttamente__[^2]

Per controllare che la __sintassi__ sia corretta si apre il sito: [CodeBeautify](https://codebeautify.org/yaml-editor-online).

 ### Passagi da fare nel sito:
1. Upload del file _YAML_ sul sito tramite file o copia e incolla nella casella _YAML EDITOR._
2. Premere il __tasto__ _PREVIEW YAML_.
3. Controllare che nella __casella di destra__ non ci siano errori.

[^2]: I file _XML_ e _XSD_ non sono eseguibili, perciò vanno controlati esternamente dall'editor di testo visto che non si ha modo di identificare errori altrimenti
## Il codice del file _XML_:
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="arlotti.xsd" type="xsd"?>
<rubrica_classe>
    <alunno>
        <id>1</id>
        <nome>Fabio</nome>
        <voto_pratico>
            <id>1</id>
            <data>2025-12-16T14:40:00+01:00</data>
            <voto>6.5</voto>
        </voto_pratico>
        <voto_teorico>
            <id>1</id>
            <data>2025-12-16T10:40:00+01:00</data>
            <voto>5</voto>
        </voto_teorico>
        <media>5.75</media>
        <commento><![CDATA[Fabio ha bisogno di studiare di più
        perchè è una pippa.]]></commento>
    </alunno>
</rubrica_classe>
```
## Il codice del file _XSD_:
``` xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="rubrica_classe">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="alunno" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="id" type="xs:integer"/>
                            <xs:element name="nome" type="xs:string"/>
                            <xs:element name="voto_pratico" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="id" type="xs:integer"/>
                                        <xs:element name="data" type="xs:string"/>
                                        <xs:element name="voto" type="xs:float"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="voto_teorico" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="id" type="xs:integer"/>
                                        <xs:element name="data" type="xs:string"/>
                                        <xs:element name="voto" type="xs:float"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="media" type="xs:float"/>
                            <xs:element name="commento" type="xs:string"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
```
## Validazione del file _XML_ e _XSD_
Per controllare che la __sintassi__ sia corretta si apre il sito: [FreeFormatter nella sezione XML](https://www.freeformatter.com/xml-validator-xsd.html).

### Passagi da fare nel sito:
1. Nella _"opzione 1"_ inserire il __documento__ _XML_
2. Nella _"opzione 2"_ inserire il __documento__ _XSD_
3. Premere su ___"VALIDATE"___ in __blu__ e controllare se __in cima__ sono stampati __errori__

>Apparirà una __casella__:
>+ ___se è rossa:___ indica che ci sono degli errori.
>+ ___se la casella è verde:___ significa che i documenti sono scritti bene.

## RESOCONTO FINALE TRAMITE TEST:

> ### Una volta finito il programma _YAML_:
 - [ ] Eseguo il programma per vedere se funziona.
 - [ ] Eseguo il programma per vedere se funziona mettendolo facendolo partire tramite un browser web.
 - [x] Non si possono eseguire i file YAML.

>### Il tag complesso "alunni" contiene il tag semplice "cognome":
 - [ ] si.
 - [x] no.

>### Il "voto_teorico" è un tag semplice:
 - [ ] si.
 - [x] no.