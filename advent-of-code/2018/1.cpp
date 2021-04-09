#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;

auto start = chrono::high_resolution_clock::now();
int a;
int sum;
int main() {

    ifstream input("1.in");
    
    while( input >> a ) {
        sum += a; 
    }

    cout << "Total: " << sum << endl;

    auto finish = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = finish - start;

    cout << "Time elapsed: " << elapsed.count() << endl;
    return 0;
}
