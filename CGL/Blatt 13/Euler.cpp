#include <iostream>
#include <iomanip>
// 1. for-Schleife zur Berechnung der Fakultaet k!
long fakultaet(int k) {
    long result = 1; // long, da mit 64-Bit mehr Platz fuer groessere Zahlen
    for (int i = 1; i <= k; ++i) {
        result *= i;}
    return result;
}
// Funktion zur Annaeherung von e durch n Terme
double approximate_e(int n) {
    double summe = 0.0; // double, da Bruchzahlen mit bis zu 16 Nachkommastellen
    for (int k = 0; k < n; ++k) {
        // 2. Berechnung: 1 / k!
        summe += 1.0 / fakultaet(k);}
    return summe;
}
int main() {
    int iterationen = 12;
    // Berechne e
    double e_approx = approximate_e(iterationen);

    // 4. Ausgabe des Ergebnisses
    std::cout << "Annaeherung von e nach " << iterationen << " Iterationen:" << std::endl;
    std::cout << std::fixed << std::setprecision(8) << e_approx << std::endl;
    return 0;
}