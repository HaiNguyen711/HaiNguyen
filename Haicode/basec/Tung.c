#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<conio.h>

struct nhasach	{
    unsigned int masach;
    char ten[500];
    char tentacgia[50];
    unsigned int so_luong;
    unsigned int gia;
    unsigned int thanhtien;
};
typedef struct nhasach NHASACH;

void nhap_danh_sach(int *n, NHASACH h[]){
	printf("Nhap so luong cac loai hang: ");
    scanf("%d", &*n);
    for(int i = 0; i < *n; ++i){
        printf("\n");
        printf("Nhap ma sach: ");
        scanf("%d", &h[i].masach);fflush(stdin);
        printf("Nhap ten sach: ");
        gets(h[i].ten);
        printf("Nhap so luong: ");
        scanf("%d", &h[i].so_luong);fflush(stdin);
        printf("Nhap gia: ");
        scanf("%d", &h[i].gia);fflush(stdin);
    }
}

void xuat_thong_tin_loai_hang(NHASACH h){
	if(h.so_luong >= 100 && h.so_luong <= 200){
        h.thanhtien = (h.so_luong * h.gia)*0.95 ;
    }
    else if(h.so_luong > 200){
        h.thanhtien = (h.so_luong * h.gia)*0.9;
    }
    else{
        h.thanhtien = h.so_luong * h.gia;
    }
    printf("\n%d\t%s\t\t\t%d\t%d\t%d", h.masach, h.ten, h.so_luong, h.gia, h.thanhtien);
}

void xuat_danh_sach(int n, NHASACH h[]){
	printf("\nMasach\tTen \t\t\tSo luong\tGia \tTien tra");
    for(int i = 0; i < n; ++i){
        xuat_thong_tin_loai_hang(h[i]);
    }
}

int xoa(NHASACH h[], int n) {
    int masachcanxoa;
    printf("Nhap ma sach can xoa: ");
    scanf("%d", &masachcanxoa);
    int found = 0;
    for(int i = 0; i < n; i++) {
        if (h[i].masach == masachcanxoa) {
            found = 1;
            for (int j = i; j < n; j++) {
                h[j] = h[j+1];
            }
            break;
        }
    }
    if (found == 0) {
        printf("\n Ma sach %d khong ton tai.", masachcanxoa);
        return 0;
    } else {
        return 1;
    }
}


void swap_hang(NHASACH *a, NHASACH *b){
    NHASACH temp = *a;
    *a = *b;
    *b = temp;
}

void sap_xep_ten_hang_tang_dan(int n, NHASACH h[]){
		for(int i = 0; i < n; ++i){
        for(int j = i  + 1; j < n; ++j){
            if(strlen(h[i].ten) > strlen(h[j].ten)){
                    swap_hang	(&h[i], &h[j]);
            }
        }
    }
    xuat_danh_sach(n, h);
}

int main()
{
    int n;
    NHASACH h[50];
    printf("\nCAU 1:\n");
	 nhap_danh_sach(&n, h);
    printf("\nCAU 2:\n");
	 xuat_danh_sach(n, h);
    printf("\nCAU 3:\n");
    xoa(h,n);
    xuat_danh_sach(n, h);
    printf("\nCAU 4:\n");
	 sap_xep_ten_hang_tang_dan(n, h);
     getch();
    return 0;
}