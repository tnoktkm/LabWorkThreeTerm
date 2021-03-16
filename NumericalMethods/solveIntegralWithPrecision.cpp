#include <iostream>
#include <cmath>
#define e 1e-4

using namespace std;


float f(float x) {
    return (cos(x)/pow(9+x*x, 2));       
}

float integral(float l,float r,float &n) {
    float h = (r - l) / n;
    float res = 0;
    for (float i = l; i < r; i += h) {
        res += h * f(i);    
    }
    return res;
}



float ruleRunge(float l, float r, float &n) {
    float ep = e / 3.0;
    float current = integral(l, r, n);
    n *= 2;
    float next = integral(l, r, (n));
    while ( (fabs(current - next) / 3.0) >= ep ) {
        n *= 2;
        current = next;
        next = integral(l, r, n);
    }
    return next;
}


int main() {
    
    float gamma = 22;
    float n = 4; 
    float res = ruleRunge(0.0, gamma, n);
    printf("Gamma = %3.0f, res = %8.9f, n = %5.0f",gamma, res, n);
    
    
    
    return 0;
}