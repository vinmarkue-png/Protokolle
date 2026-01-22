import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# Liste der Moleküle
molecules = ["CHCl3", "CH2Cl2", "CH2Br2", "C2Cl4"]

def generate_latex_table(mol_name, peaks_df):
    """Erzeugt die spezifische LaTeX-Tabelle."""
    latex_str = "\\begin{table}[H]\n    \\centering\n"
    # Nutzt \ch{} für die chemische Formel im Text
    latex_str += f"    \\caption{{Listed are the measured wavenumbers and intensities of the IR signals of \\ch{{{mol_name}}}.}}\n"
    latex_str += "    \\begin{tabular}{c|c|c}\n"
    latex_str += "    signal & wavenumber $\\tilde{\\nu}$ / cm$^{-1}$ & intensity / a.u. \\\\\n    \\hline\n"
    
    num_rows = len(peaks_df)
    
    for i, row in peaks_df.iterrows():
        # Signal-Nummerierung von 1 bis x
        label = f"{i + 1}"
        wavenumber = f"{row['wavenumber']:.2f}"
        intensity = f"{row['intensity']:.2f}"
        
        # Prüfen, ob es die letzte Zeile ist (kein \\ am Ende)
        if i == num_rows - 1:
            latex_str += f"    {label} & {wavenumber} & ~{intensity} \n"
        else:
            latex_str += f"    {label} & {wavenumber} & {intensity} \\\\\n"
    
    latex_str += f"    \\label{{tab: {mol_name}}}\n"
    latex_str += "    \\end{tabular}\n\\end{table}\n"
    return latex_str

# Pfad zu deinem Ordner
folder = r"C:\Users\vinma\Documents\Chemie Studium\5. Semester\Protokolle\PC2\IR-Raman\IR"

for mol in molecules:
    # Neues Figure-Objekt für jedes Molekül
    plt.figure(figsize=(7, 5))
    
    filename = f"{mol}.dpt"
    filepath = os.path.join(folder, filename)
    
    if not os.path.exists(filepath):
        print(f"Datei {filepath} wurde nicht gefunden.")
        continue
        
    # Einlesen der Daten
    data = pd.read_csv(filepath, header=None, names=['wavenumber', 'intensity'], sep=None, engine='python')
    
    # Plotten
    plt.plot(data['wavenumber'], data['intensity'], linewidth=2)
    
    # Peak-Suche
    max_intensity = data['intensity'].max()
    peaks, _ = find_peaks(data['intensity'], height=0.02, prominence=0.002)
    peak_data = data.iloc[peaks].sort_values('wavenumber').reset_index(drop=True)
    
    # Ausgabe der LaTeX-Tabelle in der Konsole
    print(f"% --- LaTeX Tabelle für {mol} ---")
    print(generate_latex_table(mol, peak_data))
    print("\n")

    plt.xlabel(r"Wavenumber $\tilde{\nu}$ / cm$^{-1}$")
    plt.ylabel("Intensity / a.u.")
    plt.grid(False)
    
    plt.tight_layout()

    save_path = os.path.join(folder, f"{mol}_spectrum.pdf")
    plt.savefig(save_path, dpi=300)