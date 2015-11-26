#include<stdio.h>
#include<stdlib.h>
#include<math.h>
typedef int BOOL;
#define FALSE 0;
#define TRUE 1;
BOOL prime(int val){
	double root = sqrt(val);
	for(int i=(int)root; i>=1; i--){
		if(val%i==0)
			break;
	}
	if(i==1)
		return 1;
	else
		return 0;
}
void main(){
	int no = 600851475143;
	int i;
	for(i=no-1; i>=1; i--){
		if(no%i==0){
			if(prime(i)){
				printf("%d\n",i);
				break;
			}
		}
	}
}