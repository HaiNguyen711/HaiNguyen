#include <stdio.h>
#include <math.h>
#include<conio.h>

int mu(int coso, int somu){
    if(somu  == 0 ){
        return 1;
    }else{
        return mu(coso,somu -1)*coso;
    } 
}

void NhapMang(int a[500], int n){
    for(int i = 0;i < n; ++i){
        printf("\nNhap phan tu a[%d] = ", i);
        scanf("%d", &a[i]);
    }
}

void XuatGiaTriLonNhatvaNhoNhatTrongMang(int a[500], int n){
    int max = a[0];
    int min = a[0];
    for(int i = 0;i < n; ++i){
        if(max < a[i]){
            max = a[i];
        }
    }
    printf("\n Gia  tri lon nhat trong mang la: %d", max);
    for(int i = 0;i < n; ++i){
        if(min > a[i]){
            min = a[i];
        }
    }
    printf("\n Gia tri nho nhat trong mang la: %d", min);
}

float TinhGiaTriBieuThuc(int a[500], int n){
    float sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += (float)mu(-1,i+1)*(float)mu(a[i-1],i)/(float)(i*(i+1)/2);
    }
    return sum;   
}


int main()
{
    int a[500];
    int n = 4;
    NhapMang(a, n);
    XuatGiaTriLonNhatvaNhoNhatTrongMang(a, n);
    printf("\n Gia tri cua bieu thuc la: %f", TinhGiaTriBieuThuc(a,n));
	getch();
}