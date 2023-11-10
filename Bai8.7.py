def tinh_tien_dien(kwh):
    gia_ban_dien = {
        1: 1678,
        2: 1734, 
        3: 2014, 
        4: 2536,
        5: 2834 
    }
    tong_tien = 0
    for b, gia in gia_ban_dien.items():
        if kwh <= 0:
            break
        elif kwh <= 50:
            tong_tien += kwh * gia
            break
        else:
            tong_tien += 50 * gia
            kwh -= 50
    
    return tong_tien

kwh = float(input("Nhập số Kwh tiêu thụ: "))

tong_tien = tinh_tien_dien(kwh)

print("Tổng số tiền điện là:", tong_tien, "đồng")