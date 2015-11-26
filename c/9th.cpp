#include<stdio.h>
#include<stdlib.h>
#include<math.h>
typedef int BOOL;
#define TRUE 1;
#define FALSE 0;
BOOL pyta(int a, int b, int c){
	int m = (a*a)+(b*b);
	if(m == (c*c))
		return 1;
	return 0;
}
void main(){
	int a,b,c;
	for(a=1; a<=333; a++){
		for(b=a; b<=500; b++){
			for(c=b; c<=1000; c++){
				if((a+b+c)==1000){
					if(pyta(a,b,c)){
						printf("%d,%d,%d, answer = %d\n",a,b,c,a*b*c);
						break;
					}
				}
			}
		}
	}
}