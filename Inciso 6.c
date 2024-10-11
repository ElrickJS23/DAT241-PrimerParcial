#include <stdio.h>
#include <omp.h>

int main() {
    int n, i;

    printf("Ingrese la cantidad de términos de la serie Fibonacci: ");
    scanf("%d", &n);

    if (n < 2) {
        printf("La serie Fibonacci debe tener al menos 2 términos.\n");
        return 1;
    }

    int fibonacci[n];

    fibonacci[0] = 0;
    fibonacci[1] = 1;

    printf("Serie Fibonacci: %d %d ", fibonacci[0], fibonacci[1]);

    for (i = 2; i < n; i++) {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }

    #pragma omp parallel for shared(fibonacci, n) private(i)
    for (i = 2; i < n; i++) {
        #pragma omp critical
        {
            printf("%d ", fibonacci[i]);
        }
    }

    printf("\n");

    return 0;
}
