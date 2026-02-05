let libri = []
const fs = require("fs");
const dati_json = JSON.parse(
fs.readFileSync("dati.json", "utf8")
);
        
const form = document.getElementById("form1");
const dati = new FormData(form);
const oggetto = Object.fromEntries(dati.entries());

dati_json.push(oggetto);

fs.writeFileSync(
    "dati.json",
    JSON.stringify(dati, null, 2)
);