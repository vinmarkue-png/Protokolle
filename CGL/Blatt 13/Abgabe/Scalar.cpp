#include <iostream>
#include <vector>

double scalar_product(const std::vector<double>& vector1,
    const std::vector<double>& vector2) {
    double sum = 0.0;

    for (size_t i = 0; i < vector1.size(); ++i) {
        sum += vector1[i] * vector2[i];
    }

    return sum;
}

int main()
{
    std::vector<double> v1 = { 1.0, 2.0, 3.0, 4.0 };
    std::vector<double> v2 = { 1.0, -1.0, -1.0, 1.0 };
    std::cout << scalar_product(v1, v2) << "\n";
    return 0;
}