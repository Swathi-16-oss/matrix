m=int(input("enter m order"))
n=int(input("enter n order"))
matrix1=[]
for i in range(m):
    a=[]
    for j in range(n):#for column
        a.append(int(input("enter [{}{}] element".format(i,j))))
    matrix1.append(a)#to add elements to matrix
#for printing first matrix
for i in range(m):
    for j in range(n):
        print([matrix1[i][j]],end=" ")
    print()

    
 '''o/p:
enter m order2
enter n order2
enter [00] element12
enter [01] element3
enter [10] element4
enter [11] element23
[12] [3] 
[4] [23] '''
