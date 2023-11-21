m = int(input("Nhap mot so tu nhien m: "))
n = int(input("Nhap mot so tu nhien n (lon hon m): "))

if m >= 0 and n >= 0 and m < n:
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)
else:
    print("Vui long nhap hai so tu nhien m va n (m < n).")