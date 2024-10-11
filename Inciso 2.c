#include <stdio.h>  
 
void suma(int c, int a){  
    a = a + c;  
}  
 
int main(){  
    int a, c, b;  
    a = 0;  
    c = 8;  
    b = 2;  
 
    for(int i = 0; i < c; i++){  
        a = a + b;  // ya no usamos punteros, sumamos directamente 
    }  
 
    printf("multiplicacion de %d por %d es %d\n", b, c, a);  
 
    a = 7;  
    c = 0;  
    b = 4;  
 
    for(int i = b; i < a; i = i + b){  
        c = c + 1;   
    }  
 
    printf("Division de %d entre %d es %d el resto es %d\n", a, b, c, a - b * c);  
 
    return 0;  
}
