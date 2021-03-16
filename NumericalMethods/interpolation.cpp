//Функция в форме Лагранжа для функции - e^((1/x)*sinx);
#include <iostream>

using namespace std;
            
const int N = 10;           //кол-во точек.

float Lagrange(float x, float *pointsX, float *pointsY) {
    
    float summa = 0;
    float rec = 1.0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (j != i) {
                rec *= (x - pointsX[j]);
                rec *= 1.0 / (pointsX[i] - pointsX[j]);
            }
        }
        summa += pointsY[i]*rec;
        rec = 1.0;
    }
    
    return summa;
};

int main() {
    float pointsX[N] = {1.0,  2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0,  10.0}; 
    float pointsY[N] = {2.319,1.575,1.048,0.827,0.825,0.954,1.098,1.131,1.046,0.947};
    
    float a;
    cin >> a;
    cout << Lagrange(a, pointsX, pointsY) << endl;;
 
 
 
    return 0;   
}
