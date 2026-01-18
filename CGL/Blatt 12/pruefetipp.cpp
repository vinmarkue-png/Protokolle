#include <iostream>

// Definition der Prüffunktion
bool pruefeTipp(int tipp, int loesung) {
    if (tipp == loesung) {
        std::cout << "Treffer! Gut gemacht." << std::endl;
        return true; // Rückgabe für True
    }
    else if (tipp > loesung) { // Tipp größer als die Lösung
        std::cout << "Zu hoch!" << std::endl;
    }
    else {
        std::cout << "Zu niedrig!" << std::endl;
    }
    return false; // Rückgabe für False
}

int main() {
    int guess;
    bool gefunden = false;

    std::cout << "Willkommen zum Zahlen-Raten!" << std::endl;

    while (!gefunden) {
        std::cout << "Dein Tipp: ";
        std::cin >> guess;

        gefunden = pruefeTipp(guess, secret);
    }

    return 0;
}