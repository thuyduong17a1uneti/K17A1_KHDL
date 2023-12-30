height_inch =[74,74,72,72,73,69,69,71,76,71]
# chiều cao trung bình 
a = sum(height_inch)/len(height_inch)
# chiều cao nhất
b = max(height_inch)
c = min(height_inch)
# in ra 3 chiều cao đầu cuối
d  = height_inch[:3]
e = height_inch[-3:]
# sắp xếp tăng dần , nhỏ dần
f = sorted(height_inch)
g = height_inch
h =g.reverse()

print("Chiều cao trung bình là:",a)
print("chiều cao lớn nhất là: ",b)
print("chiều cao nhỏ nhất là: ",c)
print("3 chiều cao đầu:",d)
print("3 chiều cao cuối:", e)
print("Xắp xếp list theo giá trị tăng dần là:",f)
print("Xắp xếp list theo thứ tự giảm dần là:",g)
print("đổi đơn vị sang inch: ",h)


