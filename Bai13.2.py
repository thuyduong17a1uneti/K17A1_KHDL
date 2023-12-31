a = input("Nhập tên tập tin:")
with open('D:/Bài Tập Tin học cơ sở/bài tập chương 13/c13.1/HumptyDumpty.txt', 'r', encoding='utf-8') as file:
    #Đếm số dòng
    dong = file.readlines()
    so_dong = len(dong)
    
    #Đọc từ đầu
    file.seek(0)
    
    #Đếm số từ
    a = file.read()
    tu = a.split()
    so_tu = len(tu)
    
    #Đọc từ đầu
    file.seek(0)
    
    #Đếm số chữ
    chu = len(file.read())
print(a)
print("----Report:Lines/ Words/ Chars----\n")
print("Lines:", so_dong, "Words:", so_tu, "Chars", chu)