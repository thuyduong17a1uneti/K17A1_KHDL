#Giải hpt
def giai_he_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b / a
        return f"Nghiem cua phuong trinh la x = {x}"
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
ket_qua = giai_he_phuong_trinh_bac_nhat(a, b)
print(ket_qua)

#Tính số ngày
def tinh_so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        return "Thang khong hop le"
    
    ngay_trong_thang = 31  

    if thang == 4 or thang == 6 or thang == 9 or thang == 11:
        ngay_trong_thang = 30
    elif thang == 2:
        if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
            ngay_trong_thang = 29 
        else:
            ngay_trong_thang = 28 

    return f"Thang {thang} nam {nam} co {ngay_trong_thang} ngay"
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
ket_qua = tinh_so_ngay_trong_thang(thang, nam)
print(ket_qua)

#Tìm ước số chung
def tim_uoc_so_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
so1 = int(input("Nhap so thu nhat: "))
so2 = int(input("Nhap so thu hai: "))
uoc_so_chung_lon_nhat = tim_uoc_so_chung_lon_nhat(so1, so2)
print(f"Uoc so chung lon nhat cua {so1} va {so2} la {uoc_so_chung_lon_nhat}")
