import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# --- KONFIGURATION ---
molecules = ["CHCl3", "CH2Cl2", "CH2Br2", "C2Cl4", "CDCl3", "CCl4"]
folder = r"C:\Studium\5. Semester\AC II lab\Protokolle\PC2\IR-Raman\Raman"

def generate_latex_table(mol_name, peaks_df):
    latex_str = "\\begin{table}[H]\n    \\centering\n"
    latex_str += f"    \\caption{{Listed are the measured Raman shifts and intensities of the signals of \\ch{{{mol_name}}}.}}\n"
    latex_str += "    \\begin{tabular}{c|c|c}\n"
    latex_str += "    signal & Raman Shift $\\Delta \\tilde{\\nu}$ / cm$^{-1}$ & intensity / a.u. \\\\\n    \\hline\n"
    
    num_rows = len(peaks_df)
    for i, row in peaks_df.iterrows():
        label = f"{i + 1}"
        wavenumber = f"{row['wavenumber']:.2f}"
        intensity = f"{row['intensity']:.2f}"
        if i == num_rows - 1:
            latex_str += f"    {label} & {wavenumber} & ~{intensity} \n"
        else:
            latex_str += f"    {label} & {wavenumber} & {intensity} \\\\\n"
    
    latex_str += f"    \\label{{tab: raman_{mol_name}}}\n"
    latex_str += "    \\end{tabular}\n\\end{table}\n"
    return latex_str

def find_header_row_index(filepath):
    """Sucht die Zeilennummer (0-basiert), die 'Processed' enthält."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            if "Processed" in line and "Wavenumber" in line:
                return i
    return None

# --- HAUPTSCHLEIFE ---
for mol in molecules:
    plt.figure(figsize=(7, 5))
    
    filename = f"{mol}.csv"
    filepath = os.path.join(folder, filename)
    
    if not os.path.exists(filepath):
        print(f"WARNUNG: Datei {filename} nicht gefunden.")
        continue
        
    print(f"Bearbeite {filename}...")

    # 1. Header-Zeile suchen
    header_idx = find_header_row_index(filepath)
    
    if header_idx is None:
        print(f"  -> FEHLER: Konnte Header-Zeile in {filename} nicht finden.")
        continue

    # 2. Einlesen
    try:
        # Wir nutzen skiprows, um alles vor dem Header zu überspringen.
        # header=0 bedeutet dann: Die erste Zeile NACH dem Überspringen ist der Header.
        data_raw = pd.read_csv(filepath, sep=',', decimal='.', skiprows=header_idx, header=0, engine='python')
        
        # Leerzeichen in Spaltennamen entfernen
        data_raw.columns = data_raw.columns.str.strip()

        # 3. Daten zuweisen (Mit Fallback-Strategie)
        if 'Wavenumber' in data_raw.columns and 'Processed' in data_raw.columns:
            # Weg A: Spaltennamen wurden erkannt
            x_col = data_raw['Wavenumber']
            y_col = data_raw['Processed']
        else:
            # Weg B: Fallback auf Index (3. Spalte = x, 4. Spalte = y)
            # Das greift, wenn die Namen komisch formatiert sind
            print(f"  -> Warnung: Spaltennamen nicht exakt. Nutze Spalte 3 und 4 (Index 2/3).")
            # iloc[:, 2] ist die 3. Spalte, iloc[:, 3] ist die 4. Spalte
            x_col = data_raw.iloc[:, 2]
            y_col = data_raw.iloc[:, 3]

        data = pd.DataFrame({'wavenumber': x_col, 'intensity': y_col})

    except Exception as e:
        print(f"  -> KRITISCHER FEHLER: {e}")
        continue

    # Sortieren
    data = data.sort_values(by='wavenumber', ascending=True)

    # Plotten
    plt.plot(data['wavenumber'], data['intensity'], linewidth=1.5)
    
    # Peak-Suche
    # Prominence angepasst an deine Werte (~1700 a.u.)
    peaks, _ = find_peaks(data['intensity'], prominence=250) 
    peak_data = data.iloc[peaks].sort_values('wavenumber').reset_index(drop=True)
    
    # plt.plot(peak_data['wavenumber'], peak_data['intensity'], "rx")

    # Output
    print(f"% --- LaTeX Tabelle für {mol} ---")
    print(generate_latex_table(mol, peak_data))
    print("\n")

    plt.xlabel(r"Raman Shift $\Delta \tilde{\nu}$ / cm$^{-1}$")
    plt.ylabel("Intensity / a.u.")
    # plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()

    save_path = os.path.join(folder, f"{mol}_raman_spectrum.pdf")
    plt.savefig(save_path, dpi=300)
    plt.close()

print("Fertig.")