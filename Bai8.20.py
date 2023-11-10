import math
def approximate_exp(x, n):
  """Tính gần đúng giá trị hàm e^x với sai số 10^-4 nhờ công thức truy hồi."""
  if n <= 0:
    raise ValueError("n phải là số nguyên dương lớn hơn 0")
  # Tính giá trị gần đúng của e^x
  e_x = 1
  for i in range(1, n + 1):
    e_x += x**i / math.factorial(i)
  # Kiểm tra sai số
  error = abs(math.exp(x) - e_x)
  if error > 1e-4:
    print("Sai số lớn hơn 10^-4")
    return None
  return e_x
x = 1
n = 10
e_x = approximate_exp(x, n)
print(e_x)