from numbers import Number
def tinh_s(x,n):
    s = (pow(x,2)+1)*n
    return s
a = float(input("nhập x:"))
b = float(input("nhập n:"))
print("biểu thức có giá trị là:", tinh_s(a,b))