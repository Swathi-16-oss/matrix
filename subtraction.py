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
    print("subtraction of two matrix")
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            print([matrix1[i][j]-matrix2[i][j]],end=" ")
        print()
else:
    print("please check the order")


'''o/p:
for first matrix
enter m order2
enter n order3
enter [00] element2
enter [01] element3
enter [02] element4
enter [10] element5
enter [11] element1
enter [12] element2
[2] [3] [4] 
[5] [1] [2] 
for second matrix
enter m order2
enter n order3
enter [00] element1
enter [01] element2
enter [02] element3
enter [10] element5
enter [11] element5
enter [12] element1
[1] [2] [3] 
[5] [5] [1] 
addition of two matrix
[1] [1] [1] 
[0] [-4] [1] 
