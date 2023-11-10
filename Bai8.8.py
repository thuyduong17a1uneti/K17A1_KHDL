def tinh_tien_thue_phong(loai_phong, so_dem):
    gia_phong = {
        1: 1260000,   
        2: 1550000,   
        3: 1830000,   
        4: 1830000,   
        5: 2120000,
        6: 2120000,  
        7: 2540000,  
        8: 4800000   
    }

    if so_dem >= 4:
        ti_le_giam = 0.3
    else:
        ti_le_giam = 0.25

    gia_phong_giam = gia_phong[loai_phong] - gia_phong[loai_phong] * ti_le_giam
    thanh_tien = gia_phong_giam * so_dem

    return thanh_tien

loai_phong = int(input("Nhập loại phòng (từ 1-8): "))
so_dem = int(input("Nhập số đêm: "))

thanh_tien = tinh_tien_thue_phong(loai_phong, so_dem)

print("Thành tiền =", thanh_tien, "VNĐ")