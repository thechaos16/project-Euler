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
	int pri[100000];
	int i=2;
	int j=0;
	while(1){
		if(j==10001)
			break;
		if(prime(i)){
			pri[j]=i;
			j++;
		}
		i++;
	}
	printf("%d\n",pri[10000]);
}