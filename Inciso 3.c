#include <stdio.h> 
void suma(int c,int *a){ 
    *a=*a+c; 
} 
void main(){ 
  int a,c,b; 
  a=0; 
  c=8; 
  b=2; 
  for(int i=0;i<c;i++){ 
     suma(b,&a); 
  } 
  printf("multiplicacion de %d por %d es %d\n",b,c,a); 
  a=7; 
  c=0; 
  b=4; 
  for(int i=b;i<a;i=i+b){ 
     suma(1,&c);  
  } 
  //resta(&c,b,&a); 
  printf("Division de %d entre %d es %d el resto es %d\n",a,b,c,a-b*c); 
   
}
