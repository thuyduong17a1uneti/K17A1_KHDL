def tinh_tong_chu_so(N):
    sum = 0
    while N != 0:
        sum += N % 10
        N = N // 10
    return sum

N = 2022
tong = tinh_tong_chu_so(N)
print(f"Tổng các chữ số của {N} là: {tong}")