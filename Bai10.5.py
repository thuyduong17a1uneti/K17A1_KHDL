def kiem_tra_zip_code(chuoi):
    if len(chuoi) == 6 and chuoi.isdigit():
        return True
    else:
        return False
chuoi_kiem_tra = "215"
ket_qua = kiem_tra_zip_code(chuoi_kiem_tra)
if ket_qua:
    print(f"{chuoi_kiem_tra} là mã zip code hợp lệ của việt nam")
else:
     print(f"{chuoi_kiem_tra} không là mã zip code hợp lệ của việt nam")

