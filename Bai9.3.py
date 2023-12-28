can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
def tinh_BMI(can_nang, chieu_cao):
    if can_nang>0 and chieu_cao>0:
        bmi = can_nang / (chieu_cao ** 2)
        print('Chỉ số BMI:',bmi)
        if bmi<18.5:
            print('THẤP')
        elif bmi>18.5 and bmi<24.99:
            print('BÌNH THƯỜNG')
        else:
            print('CAO')
    else:
        print('Nhập thông số không chính xác')
    return can_nang,chieu_cao
tinh_BMI(can_nang, chieu_cao)