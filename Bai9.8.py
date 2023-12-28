def kiem_tra_so_hoan_hao(a):
    b=0
    if a<=0:
        return False
    for i in range(1,a):
        b+=i
        return a
b=0
a=int(input("Nhập số:"))
if kiem_tra_so_hoan_hao(a):
    print(a,"là số hoàn hảo")
else:
    print(a,"không là số hoàn hảo")