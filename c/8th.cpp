#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main(){
	char input[2000] = {NULL};
	FILE *fp;
	fp = fopen("8.txt","r");
	int i,j;
	for(i=0; i<=1000; i++){
		input[i] = fgetc(fp);
	}
	fcloseall();
	int prod[1000];
	for(i=0; i<=999; i++)
		prod[i] = 1;
	for(i=0; i<=995; i++){
		prod[i] *= (input[i]-'0');
		prod[i] *= (input[i+1]-'0');
		prod[i] *= (input[i+2]-'0');
		prod[i] *= (input[i+3]-'0');
		prod[i] *= (input[i+4]-'0');
	}
	for(i=0; i<=999; i++){
		for(j=i; j<=999; j++){
			if(prod[i]>prod[j]){
				int m = prod[i];
				prod[i] = prod[j];
				prod[j] = m;
			}
		}
	}
	printf("%d\n",prod[999]);
}