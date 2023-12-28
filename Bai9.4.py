import math
def tinh_S(x, n):
    S=math.pow(math.pow(x,2)+1,n)
    return S
x=float(input("nhập số x:"))
n=float(input("nhập số n:"))
print("Giá trị S trả về là:",tinh_S(x, n))