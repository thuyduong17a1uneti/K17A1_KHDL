x=int(input('Nhập giá trị x:'))
def dien_so(x):
    if x<0:
        print('-1')
    elif x>0:
        print('1')
    else:
        print('0')

dien_so(x)