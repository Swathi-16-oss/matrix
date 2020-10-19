m=2
n=2
matrix1=[]
print("for 2*2 matrix")
for i in range(2):#for row
    a=[]
    for j in range(2):#for column
        a.append(int(input("enter [{}{}] element".format(i,j))))
    matrix1.append(a)#to add elements to matrix
#for printing first matrix
for i in range(2):
    for j in range(2):
        print([matrix1[i][j]],end=" ")
    print()
det=0

det=matrix1[0][0]*matrix1[1][1]-matrix1[0][1]*matrix1[1][0]
print(det)
'''o/p:
for 2*2 matrix
enter [00] element3
enter [01] element2
enter [10] element1
enter [11] element3
[3] [2] 
[1] [3] 
7'''
