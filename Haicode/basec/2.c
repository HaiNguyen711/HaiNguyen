#include <stdio.h>
#include <math.h>
#include<conio.h>


int main()
{
	float n;
	printf("Moi nhap mot so nguyen duong: ");
		scanf("%f", &n);
    while (1)
	{
		if(n != (int)n){
			printf("Moi nhap lai so nguyen duong: ");
			scanf("%f", &n);
		}
		else{
			break;
		}
	}
	int dem = 0;
	int temp = n;
	while((int)temp % 2 == 0)
	{
		++dem;
		temp/=2;
	}
	printf("co %d thua so 2 trong %d", dem, (int)n);
	getch();
}