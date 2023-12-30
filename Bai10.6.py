import math
def giai_phuong_trinh_bac_2(a,b,c):
    delta = math.sqrt(b**2-4*a*c)
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    return x1,x2
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
nghiem_x1,nghiem_x2 = giai_phuong_trinh_bac_2(a,b,c)
print(f"Nghiệm x1 = {nghiem_x1}")
print(f"Nghiệm x2 = {nghiem_x2}")