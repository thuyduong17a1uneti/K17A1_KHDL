nam_duong = int(input("Nhập năm dương lịch: "))
def tinh_am_lich(nam_duong):
    can = (nam_duong + 6) % 10
    chi = (nam_duong + 8) % 12
# Tính
    if can == 0:
        nam_can = "Giáp"
    elif can == 1:
        nam_can = "Ất"
    elif can == 2:
        nam_can = "Bính"
    elif can == 3:
        nam_can = "Đinh"
    elif can == 4:
        nam_can = "Mậu"
    elif can == 5:
        nam_can = "Kỷ"
    elif can == 6:
        nam_can = "Canh"
    elif can == 7:
        nam_can = "Tân"
    elif can == 8:
        nam_can = "Nhâm"
    else:
        nam_can = "Quý"

    if chi == 0:
        nam_chi = "Tý"
    elif chi == 1:
        nam_chi = "Sửu"
    elif chi == 2:
        nam_chi = "Dần"
    elif chi == 3:
        nam_chi = "Mão"
    elif chi == 4:
        nam_chi = "Thìn"
    elif chi == 5:
        nam_chi = "Tỵ"
    elif chi == 6:
        nam_chi = "Ngọ"
    elif chi == 7:
        nam_chi = "Mùi"
    elif chi == 8:
        nam_chi = "Thân"
    elif chi == 9:
        nam_chi = "Dậu"
    elif chi == 10:
        nam_chi = "Tuất"
    else:
        nam_chi = "Hợi"

    return f"{nam_can} {nam_chi}"
if nam_duong >=0:
    nam_am=tinh_am_lich(nam_duong)
    print("Năm",nam_duong, "lịch âm là" ,nam_am)
else:
    print("Vui lòng nhập một năm hợp lệ.")
