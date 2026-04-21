import sqlite3
import os

# Definiamo dove creare il file del database (nella cartella instance)
if not os.path.exists('arlotti_15/instance'):
    os.makedirs('arlotti_15/instance')

db_path = os.path.join('arlotti_15/instance', 'comuni.db')

# Ci connettiamo (se il file non esiste, lo crea)
connection = sqlite3.connect(db_path)

# Leggiamo lo schema SQL
with open('arlotti_15/app/comuni.sql') as f:
    connection.executescript(f.read())

print("Database creato con successo in:", db_path)
connection.close()