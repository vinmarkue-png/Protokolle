import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import os

# =======================================================
# 1. DATENEINGABE UND PFADKONSTRUKTION
# =======================================================

base_dir = pathlib.Path(r"C:\Studium\5. Semester\AC II lab\Protokolle")
messdaten_dir = base_dir / "AC2" / "Tetrazin-Re-Komplex" / "Plots" / "UV_Vis"

# Dateipfade
file_paths = {
    "Tetrazin": messdaten_dir / "Re-Tz_MeCN.csv",
    "Pyridazin": messdaten_dir / "Re-Pyridazine_MeCN.csv"
}

# Spaltennamen (müssen exakt mit den CSV-Daten übereinstimmen oder angepasst werden)
# Wenn die CSV keine Header hat, werden diese Namen zugewiesen.
X_COL = r'Wellenlänge $\lambda$ [nm]'
Y_COL = 'Absorption' 

# =======================================================

def load_and_clean_single_file(path_str, names):
    """Lädt eine einzelne Datei, erzwingt numerische Typen und sortiert nach X."""
    try:
        if not os.path.exists(path_str):
             raise FileNotFoundError(f"File not found at: {path_str}")

        # Annahme: CSV hat keinen Header. Falls doch, ändern Sie header=None zu header=0
        df = pd.read_csv(
            path_str, 
            header=None, 
            names=names
        )
        
        df[names[0]] = pd.to_numeric(df[names[0]], errors='coerce')
        df[names[1]] = pd.to_numeric(df[names[1]], errors='coerce')
        df.dropna(inplace=True) 
        df.sort_values(by=names[0], inplace=True)
        
        return df
    except FileNotFoundError:
        print(f"❌ FEHLER: Datei '{path_str}' nicht gefunden.")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ FEHLER beim Verarbeiten von '{path_str}': {e}")
        return pd.DataFrame()

def load_and_plot_data():
    
    plt.figure(figsize=(10, 6))
    colors = ['#1f77b4', "#ff0e0e"] # Blau und Rot
    
    # Schleife über alle Dateien zum Laden und direkten Plotten
    for i, (label, path) in enumerate(file_paths.items()):
        df = load_and_clean_single_file(str(path), [X_COL, Y_COL])
        
        if not df.empty:
            color = colors[i % len(colors)]
            
            plt.plot(
                df[X_COL], 
                df[Y_COL], 
                label=label, 
                color=color, 
                linestyle='-',
                linewidth=1
            )
            print(f"✅ Messreihe '{label}' erfolgreich geplottet.")
            
    # Einfache Achsenbeschriftung
    plt.xlabel(X_COL)
    plt.ylabel(Y_COL)
    
    # Legende anzeigen
    #plt.legend(loc='upper right')
    plt.xlim(left=200)
    plt.xlim(right=800)
    
    # Speichern

    # Beispiel: Zielordner
    folder = r"C:\Studium\5. Semester\AC II lab\Protokolle\AC2\Tetrazin-Re-Komplex\Bilder"  # Windows
    # folder = '/home/deinbenutzername/Bilder/Plots'  # Linux/Mac

    # Sicherstellen, dass der Ordner existiert
    os.makedirs(folder, exist_ok=True)

    # Dateiname inklusive Pfad
    plot_filename = os.path.join(folder, 'UV_Vis.png')
    plt.savefig(plot_filename)
    print(f"\n✨ Plot wurde unter dem Namen '{plot_filename}' gespeichert.")

# Programm starten
if __name__ == "__main__":
    load_and_plot_data()