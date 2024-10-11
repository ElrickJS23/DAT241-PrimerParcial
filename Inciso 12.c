#include <stdio.h> 
#include <omp.h> 
 
int main() { 
    int n, i; 
 
    printf("Ingrese la cantidad de términos de la serie Fibonacci: "); 
    scanf("%d", &n); 
 
    int fibonacci[n]; 
 
    fibonacci[0] = 0; 
    fibonacci[1] = 1; 
 
    printf("Serie Fibonacci: %d %d ", fibonacci[0], fibonacci[1]); 
 
    #pragma omp parallel shared(fibonacci, n) private(i) 
    { 
        #pragma omp for 
        for (i = 2; i < n; i++) { 
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]; 
        } 
    } 
 
    for (i = 2; i < n; i++) { 
        printf("%d ", fibonacci[i]); 
    } 
    printf("\n"); 
 
    return 0; 
}
