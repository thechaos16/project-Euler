#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
typedef int BOOL;
#define FALSE 0;
#define TRUE 1;
BOOL palin(int val){
	char p[10];
	itoa(val,p,10);
	int i;
	int length = strlen(p);
	for(i=0; i<length/2; i++){
		if(p[i]!=p[length-i-1])
			return 0;
	}
	return 1;
}
void main(){
	int answer[10000];
	int cnt=0;
	int i,j;
	for(i=999; i>=100; i--){
		for(j=999; j>=100; j--){
			if(palin(i*j)){
				answer[cnt] = i*j;
				cnt++;
			}
		}
	}
	for(i=0; i<=cnt; i++){
		for(j=i; j<=cnt; j++){
			if(answer[i]>answer[j]){
				int m = answer[i];
				answer[i] = answer[j];
				answer[j] = m;
			}
		}
	}
	printf("%d\n",answer[cnt]);
}
