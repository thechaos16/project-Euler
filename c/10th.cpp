#include<stdio.h>
#include<stdlib.h>
#include<math.h>
typedef int BOOL;
#define FALSE 0;
#define TRUE 1;
BOOL prime(int val){
	double root = sqrt(val);
	for(int i=(int)root; i>1; i--){
		if(val%i==0)
			return 0;
	}
	return 1;
}
void main(){
	int i;
	double sum=0;
	for(i=2; i<=2000000; i++){
		if(prime(i))
			sum+=(double)i;
	}
	printf("%.0lf\n",sum);
}