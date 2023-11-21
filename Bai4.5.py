def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a

# Hàm tính BCNN
def BCNN(a, b):
    return abs(a * b) // UCLN(a, b)

# Nhập hai số từ bàn phím
so1 = int(input("Nhap so thu nhat: "))
so2 = int(input("Nhap so thu hai: "))

# Tính và in ra BCNN của hai số
bcnn = BCNN(so1, so2)
print(f"BCNN cua {so1} va {so2} la {bcnn}")