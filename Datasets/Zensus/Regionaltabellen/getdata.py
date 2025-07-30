import os
import sqlite3
import pandas as pd



# Verbindung zur SQLite-Datenbank erstellen
conn = sqlite3.connect('regionale_datenbank.db')
cursor = conn.cursor()

# CSV-Dateien und ihre Zieltabellen
csv_dateien = {
    "Datasets/Zensus/Regionaltabellen/Regionaltabelle_Bevoelkerung_final.csv": "Bevoelkerung",
    "Datasets/Zensus/Regionaltabellen/Regionaltabelle_Bildung_Erwerbstaetigkeit_final.csv": "Bildung_Erwerbstaetigkeit",
    "Datasets/Zensus/Regionaltabellen/Regionaltabelle_Demografie_final.csv": "Demografie",
    "Datasets/Zensus/Regionaltabellen/Regionaltabelle_Gebaeude_Wohnungen_final.csv": "Gebaeude_Wohnungen",
    "Datasets/Zensus/Regionaltabellen/Regionaltabelle_Haushalte_final.csv": "Haushalte"
}

# Jede CSV-Datei verarbeiten
for csv_datei, tabelle in csv_dateien.items():
    # CSV-Datei laden
    df = pd.read_csv(csv_datei)
    
    # Tabelle in der Datenbank erstellen und Daten einfügen
    df.to_sql(tabelle, conn, if_exists='replace', index=False)

    # Optional: Index für PLZ hinzufügen
#    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{tabelle}_plz ON {tabelle} (PLZ)")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank wurde erfolgreich erstellt und CSV-Dateien wurden importiert.")


