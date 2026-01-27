#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
class Person {
public:
	std::string name;
	int age;
};

bool is_younger(const Person& a, const Person& b) {
return a.age < b.age; // Ausgabe true, wenn a jünger ist als b
}
int main() {
std::vector<Person> people{
{"Alice", 30},
{"Bob", 24},
{"Clara", 41}
};
// std::sort mit der Funktion is_younger aufrufen
std::sort(people.begin(), people.end(), is_younger);
// Ausgabe zur Überprüfung
for (const auto& person : people) {
std::cout << person.name << ": " << person.age << " Jahre" << std::endl;
}
}