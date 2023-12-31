def noi_dung():
    with open("Rain.txt", 'a') as file:
        file.write(nd + '\n')
    
    with open("Rain.txt", 'r') as file:
        f = file.read()
        print("Nội dung sau khi ghi vào tập tin Rain.txt:")
        print(f)
        
a = input("Nhập tên tập tin:")
nd = input("Nhập nội dung:")
noi_dung()