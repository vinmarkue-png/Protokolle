import pandas as pd
import matplotlib.pyplot as plt
import pathlib
from scipy.interpolate import interp1d
import numpy as np 
import os

# =======================================================
# 1. DATENEINGABE UND PFADKONSTRUKTION
# =======================================================

base_dir = pathlib.Path(r"C:\Studium\5. Semester\AC II lab\Protokolle")
messdaten_dir = base_dir / "AC2" / "Cobalteisenstein" / "Messdaten"

# Korrigierte Dateinamen mit BINDENSTRICHEN (wahrscheinlich Originale)
file_paths = {
    "Cobalteisenstein": messdaten_dir / "A05-CoFe2O4.csv",
    "Literatur Cobalteisenstein": messdaten_dir / "CoFe2O4-Spinell_CollCode109044_R01.csv",
    "Eisenoxid": messdaten_dir / "Fe2O3_Korund_CollCode40142_R01_shifted-0.3.csv"
}

X_COL = r'$2 \theta$'
Y_COL = 'relative Intensität / %' 
PLOT_Y_COL_NAME = 'Normierte Intensität / %'

# =======================================================

def load_and_clean_single_file(path_str, names):
    """Lädt eine einzelne Datei, erzwingt numerische Typen und entfernt NaN-Werte."""
    try:
        # Check if file exists to give a clearer error than pandas
        if not os.path.exists(path_str):
             raise FileNotFoundError(f"File not found at: {path_str}")

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
    colors = ['#1f77b4', "#ff0e0e", '#2ca02c']
    
    loaded_data = {}
    for label, path in file_paths.items():
        df = load_and_clean_single_file(str(path), [X_COL, Y_COL])
        if not df.empty:
            loaded_data[label] = df
            
    if not all(k in loaded_data for k in ["Cobalteisenstein", "Eisenoxid"]):
        print("\n❌ Cobalteisenstein und Eisenoxid Datenreihen sind zum Skalieren erforderlich und fehlen.")
        return

    # --- 2. Referenzwerte bestimmen ---
    cobalteisenstein_df = loaded_data["Cobalteisenstein"]
    eisenoxid_df = loaded_data["Eisenoxid"]
    
    # Finde den Peak mit der GRÖSSTEN ABSOLUTEN INTENSITÄT in der Eisenoxid-Reihe
    idx_fe_extreme = eisenoxid_df[Y_COL].abs().idxmax()
    I_Fe_at_extreme = eisenoxid_df.loc[idx_fe_extreme, Y_COL]
    theta_Fe_extreme = eisenoxid_df.loc[idx_fe_extreme, X_COL]
    
    # Finde das absolute Maximum der Cobalteisenstein-Daten (unsere 100%-Referenz)
    I_CoFe_max_absolute = cobalteisenstein_df[Y_COL].max()
    
    if I_CoFe_max_absolute <= 0:
        print("⚠️ Cobalteisenstein Maximalwert ist <= 0. Cobalteisenstein kann nicht auf 100% normiert werden.")
        return

    print(f"Eisenoxid Extremwert (Max Magnitude) bei 2\u03B8 = {theta_Fe_extreme:.3f} ° mit Intensität {I_Fe_at_extreme:.0f}")
    
    # --- 3. Intensität von CoFe an der Peak-Position von Fe2O3 interpolieren (Zielwert) ---
    
    f_cobalteisenstein = interp1d(cobalteisenstein_df[X_COL], cobalteisenstein_df[Y_COL], kind='linear', fill_value='extrapolate')
    I_CoFe_interp_absolute = float(f_cobalteisenstein(theta_Fe_extreme))
    
    print(f"Ziel-Intensität CoFe bei {theta_Fe_extreme:.3f}°: {I_CoFe_interp_absolute:.0f}")

   # --- 4. Skalierung anwenden (Angepasste Reihenfolge für Normierungsziel) ---
    
    # a) Normierung der Referenz (CoFe) auf 100% an ihrem höchsten Peak
    # Dies muss zuerst geschehen, da es die Zielskala für Eisenoxid liefert.
    I_CoFe_max_absolute = cobalteisenstein_df[Y_COL].max()
    
    if I_CoFe_max_absolute <= 0:
        print("⚠️ Cobalteisenstein Maximalwert ist <= 0. Cobalteisenstein kann nicht auf 100% normiert werden.")
        return
        
    cobalteisenstein_df[PLOT_Y_COL_NAME] = (cobalteisenstein_df[Y_COL] / I_CoFe_max_absolute) * 100
    
    # Erstelle eine Interpolationsfunktion FÜR DIE NEU NORMIERTE COBALTEISENSTEIN-REIHE
    f_cobalteisenstein_normiert = interp1d(cobalteisenstein_df[X_COL], cobalteisenstein_df[PLOT_Y_COL_NAME], kind='linear', fill_value='extrapolate')
    
    # Interpoliere den Zielwert (schon normiert) am Ort des extremen Fe2O3-Peaks
    # Das Ergebnis ist der Wert der blauen Kurve an der gewünschten Stelle (z.B. 25%)
    Target_Value_Normiert = float(f_cobalteisenstein_normiert(theta_Fe_extreme))
    
    print(f"Ziel-Intensität (NORMIERT) CoFe bei {theta_Fe_extreme:.3f}°: {Target_Value_Normiert:.2f} %")

    # Fe2O3 Peak mit der größten Magnitude
    I_Fe_at_extreme = eisenoxid_df.loc[idx_fe_extreme, Y_COL]
    
    if I_Fe_at_extreme == 0:
         print("⚠️ Eisenoxid Extremwert ist 0. Skalierung nicht möglich.")
         return
         
    # Skalierungsfaktor F: Der Fe-Extremwert (I_Fe_at_extreme) soll zum Normierten Zielwert werden (Target_Value_Normiert).
    # Da wir spiegeln wollen, multiplizieren wir den Faktor mit -1.
    scaling_factor_fe = (Target_Value_Normiert / I_Fe_at_extreme) * -1
    
    # b) Skalierung der Eisenoxid-Reihe: Multiplikation mit dem Faktor F (mit Spiegelung).
    eisenoxid_df[PLOT_Y_COL_NAME] = (eisenoxid_df[Y_COL] * scaling_factor_fe)
    
    print(f"Eisenoxid-Reihe an den normierten Cobalteisenstein-Wert skaliert und gespiegelt.")
    
    # c) Skalierung der Literatur-Reihe auf eigenen 100% Wert (visuelle Referenz)
    if "Literatur Cobalteisenstein" in loaded_data:
        lit_df = loaded_data["Literatur Cobalteisenstein"]
        lit_max_intensity = lit_df[Y_COL].abs().max()
        
        if lit_max_intensity > 0:
            lit_df[PLOT_Y_COL_NAME] = (lit_df[Y_COL] / lit_max_intensity) * 100
        else:
            lit_df[PLOT_Y_COL_NAME] = lit_df[Y_COL]

    # 5. Plotten der skalierten Daten
    for i, label in enumerate(file_paths.keys()):
        if label in loaded_data:
            df = loaded_data[label]
            color = colors[i % len(colors)]
            y_to_plot = df.get(PLOT_Y_COL_NAME, df[Y_COL]) 

            plt.plot(
                df[X_COL], 
                y_to_plot, 
                label=label, 
                color=color, 
                linestyle='-',
                linewidth=1,
                marker='.',
                markersize=0 
            )
            
    # 6. PLOT-GESTALTUNG
   # plt.title('Vergleich von drei Messreihen (Fe2O3 an CoFe Intensität skaliert)')
    plt.xlabel(r'$2\theta\ / \ ^\circ$')
    plt.ylabel(Y_COL)
    
    #plt.legend(loc='upper right')
    #plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.ylim(top=100)
    plt.ylim(bottom=-100)
    plt.xlim(left=11)
    plt.xlim(right=80) 
    
    plot_filename = 'messreihen_inter_reihen_skalierung.png'
    plt.savefig(plot_filename)
    print(f"\n✨ Plot wurde unter dem Namen '{plot_filename}' gespeichert.")

# Programm starten
if __name__ == "__main__":
    load_and_plot_data()
