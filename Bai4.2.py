N = int(input("Nhap mot so tu nhien N: "))

# Kiểm tra xem N có là số tự nhiên không âm hay không
if N >= 0:
    # In ra các số nguyên từ 1 đến N
    for i in range(1, N + 1):
        print(i)
else:
    print("Vui long nhap mot so tu nhien khong am.")