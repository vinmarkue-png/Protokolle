import pandas as pd
import matplotlib.pyplot as plt
import pathlib

# =======================================================
# 1. DATENEINGABE UND PFADKONSTRUKTION (Robust)
# =======================================================

# Basisverzeichnis: Wird aus dem Pfad dieses Skripts abgeleitet. 
# Dies macht das Skript unabhängig davon, wo es ausgeführt wird (CWD).
# Annahme: Alle Daten liegen im selben Ordner wie dieses Skript.
# self_path = pathlib.Path(__file__).resolve()
# base_dir = self_path.parent 
# --- Da Sie den absoluten Pfad zur Protokollebene angegeben haben, verwenden wir diesen ---
base_dir = pathlib.Path(r"C:\Studium\5. Semester\AC II lab\Protokolle")

# Konstruktion der Pfade mit pathlib (plattformunabhängig und ohne Escape-Probleme)
file_paths = {
    "Cobalteisenstein": base_dir / "AC2" / "Cobalteisenstein" / "Messdaten" / "A05-CoFe2O4.csv",
    "Literatur Cobalteisenstein": base_dir / "AC2" / "Cobalteisenstein" / "Messdaten" / "CoFe2O4-Spinell_CollCode109044_R01.csv",
    "Eisenoxid": base_dir / "AC2" / "Cobalteisenstein" / "Messdaten" / "Fe2O3_Korund_CollCode40142_R01.csv"
}

# Standard-Spaltennamen (wie zuvor angenommen)
X_COL = '$2\theta$'
Y_COL = 'Relative Intensität / %' 

# =======================================================

def load_and_plot_data():
    """Lädt drei Datensätze und plottet sie, mit erzwungener numerischer Konvertierung."""
    
    plt.figure(figsize=(10, 6))
    colors = ['#1f77b4', "#ff0e0e", '#2ca02c']
    line_styles = ['-', '-', '-']
    
    data_loaded_successfully = False
    
    for i, (label, path) in enumerate(file_paths.items()):
        
        # Pfad-Objekt in String für pd.read_csv konvertieren
        path_str = str(path) 
        
        try:
            # 1. Daten laden und bereinigen (wie zuvor)
            df = pd.read_csv(
                path_str, 
                header=None, 
                names=[X_COL, Y_COL]
            )
            
            df[X_COL] = pd.to_numeric(df[X_COL], errors='coerce')
            df[Y_COL] = pd.to_numeric(df[Y_COL], errors='coerce')
            df.dropna(inplace=True) 
            
            if df.empty:
                 print(f"⚠️ Messreihe '{label}' wurde geladen, enthält aber nach der Bereinigung keine gültigen Daten mehr.")
                 continue

            # =======================================================
            # ✨ NEU: MAXIMA-NORMIEUNG (SKALIERUNG)
            # =======================================================
            # Finde den Maximalwert der Intensitätsspalte in dieser Messreihe
            max_intensity = df[Y_COL].max()
            
            # WICHTIG: Vermeide Division durch Null, falls max_intensity 0 oder NaN ist.
            if max_intensity > 0:
                # Normiere alle Intensitätswerte auf 1 (oder 100%, je nach Wunsch)
                # Hier normieren wir auf den Maximalwert, sodass das Maximum = 1 ist.
                df['Normierte Intensität'] = (df[Y_COL] / max_intensity) * 100
                
                # Wenn Sie auf 100 skalieren wollen:
                # df['Normierte Intensität'] = (df[Y_COL] / max_intensity) * 100
                
                # Der Y-COL Name im Plot muss geändert werden
                plot_y_col = 'Normierte Intensität' 
            else:
                # Falls keine Peaks gefunden wurden oder alle Werte 0 sind
                print(f"⚠️ Messreihe '{label}' kann nicht normiert werden (Maximalwert ist Null oder negativ).")
                plot_y_col = Y_COL # Verwende unnormierte Daten
            # =======================================================

            # 2. Plotten der normierten Daten
            plt.plot(
                df[X_COL], 
                df[plot_y_col], 
                # ... (restliche Plot-Parameter) ...
                label=label, 
                color=colors[i], 
                linestyle=line_styles[i],
                linewidth=1,
                marker='.',
                markersize=0 
            )
            data_loaded_successfully = True
            print(f"✅ Messreihe '{label}' erfolgreich geladen, normiert und geplottet.")

        # ... (restliche Fehlerbehandlung) ...

        except FileNotFoundError:
            print(f"❌ FEHLER: Datei '{path_str}' für Messreihe '{label}' nicht gefunden.")
        except Exception as e:
            print(f"❌ FEHLER beim Verarbeiten von '{path_str}': {e}")


    if data_loaded_successfully:
        # =======================================================
        # 2. PLOT-GESTALTUNG
        # =======================================================
        
        
        plt.xlabel(f'{X_COL} / °')
        plt.ylabel(Y_COL)
        
        plt.legend(loc='upper right')
        
        
        # Setze die X-Achse auf den numerischen Bereich der Daten (optional)
        # plt.xlim(df[X_COL].min(), df[X_COL].max()) 
        
        plot_filename = 'messreihen.png'
        plt.savefig(plot_filename)
        print(f"\n✨ Korrigierter Plot wurde unter dem Namen '{plot_filename}' gespeichert.")
        plt.show() # Zeigt den Plot zusätzlich an
    else:
        print("\nKeine Datenreihen konnten geladen werden. Plot-Erstellung abgebrochen.")

# Programm starten
if __name__ == "__main__":
    load_and_plot_data()