#include <iostream>
#include <vector>

double sum_below_limit(const std::vector<double>& vector, double limit) {
    double sum = 0.0;
    for (double element : vector) {
        if (element < limit) {
            sum += element;
        }
    }
    return   sum;
}

int main()
{
    std::vector<double> v = { 1.0, 2.0, 3.0, 4.0, 5.0, 42.0, 100.00, 300.00 };
    std::cout << sum_below_limit(v, 4.0) << "\n";
    return 0;
}