#include <iostream>
#include <cmath>
#define e 1.0e-3      //Определение погрешности измерения для нахождения суммы ряда.

using namespace std;

void f(float x) {
    cout << "e = "<< e << endl;
    
    float rec = 1.0;              //начальное значение для рекуретного соотношения.
    float summa = 1.0;            //значение полученной суммы.
    for (int k = 1; fabs(rec) >= e; ++k) {
        
        rec *= -1.0;        /*Числитель*/
        rec *= x;
        
        rec *= 1.0/3.0;     /*Знаменатель*/
        rec *= 1.0/k;
        
        printf ("[f] : k = %d, rec = %.4f, summa = %.3f\n", k, rec, summa);
        summa += rec;
    }
    cout << summa << endl;
    
}



void F(float x) {
    cout << "e = "<< e << endl;
    
    float rec = x;              //начальное значение для рекуретного соотношения.
    float summa = x;            //значение полученной суммы.
    for (int k = 1; fabs(rec) >= e; ++k) {
        
        rec *= -1.0;        /*Числитель*/
        rec *= x;
        
        rec *= 1.0/3.0;     /*Знаменатель*/
        rec *= 1.0/k;
        
        printf ("[f`] : k = %d, rec = %.4f, summa = %.3f\n", k, rec, summa);
        summa += rec;
    }
    cout << summa << endl;
    
}

int main() {
    
    float a;
    cin >> a;
    f(a);
    F(a);
    
    
    return 0;
}
