def kiem_tra_so_nguyen_to(x):
 if x<2:
    return False
 else:
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
         return False
    return True
 
x=float(input("nhập số x:"))
if kiem_tra_so_nguyen_to(x):
  print(x,'là số nguyên tố')
else:
  print(x,'không là số nguyên tố')