#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main(){
	int i=1;
	while(1){
		int j;
		for(j=1; j<=20; j++){
			if((20*i)%j!=0){
//				printf("%d,%d\n",i,j);
				goto retry;
			}
		}
		printf("%d\n",20*i);
		break;
retry:
		i++;
		printf("");
	}
}
