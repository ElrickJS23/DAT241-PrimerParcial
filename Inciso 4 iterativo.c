#include <stdio.h> 
 
void leibniz_iterativa(int n, double *pi){ 
    double sum = 0.0; 
    for(int i = 0; i < n; i++){ 
        sum += ((i % 2 == 0 ? 1.0 : -1.0) / (2 * i + 1)); 
    } 
    *pi = sum * 4; 
} 
 
int main(){ 
    int n = 1000000;  // Número de términos 
    double pi; 
 
    leibniz_iterativa(n, &pi); 
 
    printf("Valor de PI calculado iterativamente con %d términos: %.15f\n", n, pi); 
 
    return 0; 
}
