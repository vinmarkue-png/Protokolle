#include <iostream>
#include <cstdlib>  // Für rand() und srand()
#include <ctime>    // Für time()

using namespace std;

int main() {
    // 1. Zufallsgenerator initialisieren
    // time(0) liefert die aktuelle Zeit, damit ist der "Startwert" immer anders.
    srand(time(0));

    int maxZahl;
    cout << "Bis zu welcher Zahl soll gewuerfelt werden? (Maximum): ";
    cin >> maxZahl;

    // 2. Zufallszahl generieren (Modulo-Operator % begrenzt den Bereich)
    // +1 sorgt dafür, dass der Bereich 1 bis Max ist (statt 0 bis Max-1)
    int zufallsZahl = rand() % maxZahl + 1;

    int eingabe = 0;    // Variable für die Benutzereingabe
    int versuche = 0;   // Zähler für die Versuche

    cout << "Ich habe mir eine Zahl zwischen 1 und " << maxZahl << " ausgedacht." << endl;

    // 3. While-Schleife für die Eingabe
    // Die Schleife läuft, solange die Eingabe NICHT der Zufallszahl entspricht.
    while (eingabe != zufallsZahl) {
        cout << "Bitte rate die Zahl: ";
        cin >> eingabe;

        // Versuch zählen
        versuche++;

        // Logik: Prüfen ob größer, kleiner oder Treffer
        if (eingabe > zufallsZahl) {
            cout << "Die gesuchte Zahl ist KLEINER als " << eingabe << "." << endl;
        }
        else if (eingabe < zufallsZahl) {
            cout << "Die gesuchte Zahl ist GROESSER als " << eingabe << "." << endl;
        }
        else {
            cout << "Glueckwunsch! Du hast die Zahl erraten." << endl;
            // Hier endet die Schleife automatisch, da eingabe == zufallsZahl ist
        }
    }

    // 4. Ausgabe der Versuche am Ende
    cout << "Du hast " << versuche << " Versuche gebraucht." << endl;

    return 0;
}