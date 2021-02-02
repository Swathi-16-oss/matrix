#for first matrix:
print("for first matrix")
m=int(input("enter m order"))
n=int(input("enter n order"))
matrix1=[]
for i in range(m):#for row
    a=[]
    for j in range(n):#for column
        a.append(int(input("enter [{}{}] element".format(i,j))))
    matrix1.append(a)#to add elements to matrix
#for printing first matrix
for i in range(m):
    for j in range(n):
        print([matrix1[i][j]],end=" ")
    print()
#for second matrix:
print("for second matrix")
k=int(input("enter m order"))
l=int(input("enter n order"))
matrix2=[]
for i in range(k):#for row
    a=[]
    for j in range(l):#for column
        a.append(int(input("enter [{}{}] element".format(i,j))))
    matrix2.append(a)#to add elements to matrix
#for printing first matrix
for i in range(k):
    for j in range(l):
        print([matrix2[i][j]],end=" ")
    print()

if(m==k and n==l):
    print("addition of two matrix")
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            print([matrix1[i][j]+matrix2[i][j]],end=" ")
        print()
else:
    print("please check the order")
    
'''o/p:
for first matrix
enter m order3
enter n order2
enter [00] element1
enter [01] element2
enter [10] element3
enter [11] element4
enter [20] element5
enter [21] element6
[1] [2] 
[3] [4] 
[5] [6] 
for second matrix
enter m order3
enter n order2
enter [00] element4
enter [01] element5
enter [10] element6
enter [11] element3
enter [20] element2
enter [21] element1
[4] [5] 
[6] [3] 
[2] [1] 
addition of two matrix
[-3] [-3] 
[-3] [1] 
[3] [5] 
>>> 

