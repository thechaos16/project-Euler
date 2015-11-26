#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main(){
	int sumofsquare = 0;
	int squareofsum = 0;
	int i;
	for(i=1; i<=100; i++){
		sumofsquare += i*i;
		squareofsum += i;
	}
	squareofsum = squareofsum * squareofsum;
	printf("%d\n",squareofsum-sumofsquare);
}