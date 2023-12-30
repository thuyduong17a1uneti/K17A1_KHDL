thresh=int(input('nhập số:'))
a=[]
def elementwice_greater_than(L,thresh):
     for i in L:
         if i <= thresh:
             b=False
             a.append(b)
         if i > thresh:    
             b=True
             a.append(b)
     return a
print(elementwice_greater_than(L,thresh))