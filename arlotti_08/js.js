let datiJson = [];

// Leggi il file JSON caricato
const fileInput = document.getElementById("fileInput");
fileInput.addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const text = await file.text();
  try {
    datiJson = JSON.parse(text);
    alert("File JSON caricato!");
  } catch (error) {
    alert("Errore: il file non è un JSON valido");
    console.error(error);
  }
});

// Gestione del form
const form = document.getElementById("form1");
form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (!Array.isArray(datiJson)) {
    alert("Per favore carica prima un file JSON valido.");
    return;
  }

  const formData = new FormData(form);
  const nuovoDato = Object.fromEntries(formData.entries());

  datiJson.push(nuovoDato);

  // Genera il nuovo JSON e lo scarica
  const nuovoJson = JSON.stringify(datiJson, null, 2);
  const blob = new Blob([nuovoJson], { type: "application/json" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "dati-aggiornati.json";
  a.click();

  URL.revokeObjectURL(url);

  form.reset();
});
