#include <stdio.h> 
 
void leibniz_recursiva(int n, int current, double *sum){ 
    if (current >= n) { 
        return; 
    } 
    *sum += ((current % 2 == 0 ? 1.0 : -1.0) / (2 * current + 1)); 
    leibniz_recursiva(n, current + 1, sum); 
} 
 
int main(){ 
    int n = 1000000;  // Número de términos 
    double pi = 0.0; 
 
    leibniz_recursiva(n, 0, &pi); 
    pi = pi * 4; 
 
    printf("Valor de PI calculado recursivamente con %d términos: %.15f\n", n, pi); 
 
    return 0; 
}
