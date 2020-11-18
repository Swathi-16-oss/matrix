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
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
#for traverse matrix
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        result[i][j]=matrix1[j][i]
for r in result:
    print(r)

'''o/p:
for first matrix
enter m order3
enter n order3
enter [00] element2
enter [01] element3
enter [02] element4
enter [10] element5
enter [11] element6
enter [12] element7
enter [20] element8
enter [21] element88
enter [22] element77
[2] [3] [4] 
[5] [6] [7] 
[8] [88] [77] 
[2, 5, 8]
[3, 6, 88]
[4, 7, 77]
>>> 
========
for first matrix
enter m order2
enter n order2
enter [00] element1
enter [01] element2
enter [10] element3
enter [11] element4
[1] [2] 
[3] [4] 
[1, 3, 0]
[2, 4, 0]
[0, 0, 0]'''
