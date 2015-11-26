#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double fibo(int no){
	double value = 0;
	if(no==0 || no==1)
		return 1;
	value = fibo(no-1)+fibo(no-2);
	return value;
}
void main(){
	int i=1;
	double sum=0;
	while(1){
		double val = fibo(i);
		//printf("%lf\n",val);
		if(val>=4000000)
			break;
		if((int)val%2==0)
			sum+=val;
		i++;
	}
	printf("%lf\n",sum);
}