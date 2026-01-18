#include <iostream>
#include <cstdlib> // für rand() und srand()
#include <ctime>   // für time()

int main(int argc, char* argv[])
{
    // Zufallsgenerators mit der aktuellen Zeit
    std::srand(std::time(NULL));

    int maximum;
    int guess;
    int guess_count = 1;
    int random_number;

    std::cout << "Gib ein Maximum fuer die Zufallszahl ein: ";
    std::cin >> maximum;

    // Generiert eine Zahl zwischen 1 und dem Maximum
    random_number = (std::rand() % maximum) + 1;

    std::cout << "Rate die Zahl (1 bis " << maximum << "): ";
    std::cin >> guess;

    while (guess != random_number) {
        // Überprüfung der Eingegebenen Zahl
        if (guess > random_number) {
            std::cout << "Die Zahl ist kleiner als " << guess << ". Versuche es nochmal: ";
        }
        else {
            std::cout << "Die Zahl ist groesser als " << guess << ". Versuche es nochmal: ";
        }

        // Neue Eingabe innerhalb der Schleife
        std::cin >> guess;

        // Zähler erhöhen
        guess_count++;
    }

    // Erfolgsmeldung nach der Schleife
    std::cout << "Glueckwunsch! Du hast die Zahl " << random_number << " erraten." << std::endl;
    std::cout << "Du hast dafuer " << guess_count << " Versuche gebraucht." << std::endl;

    return 0;
}