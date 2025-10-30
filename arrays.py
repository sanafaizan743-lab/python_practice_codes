mat1=[[1,  8],
      [9,  4]]
mat2=[[5, 6, 7],
      [7, 8, 10]]
print(mat1)
print(mat2)

print("no of rows of a matrix mat1 is" , len(mat1))
print("no of coloumns of mat1 is", len(mat1[0]))
print("order of matric is ", len(mat1) ,"x" , len(mat1[0]))

print("no of rows of a matrix mat2 is" , len(mat2))
print("no of coloumns of mat2 is", len(mat2[0]))
print("order of matric is ", len(mat2) ,"x" , len(mat2[0]))

print("addition of matrices")
sum= [[0,0],[0,0]]

R1= len(mat1)
R2= len(mat2)
C1= len(mat1[0])
C2= len(mat2[0])
if(R1==R2 and C1==C2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            sum[i][j] = mat1[i][j] + mat2[i][j]
    print("addition of two matrices give \n", sum)
else:
    print("Addition is not possible")

for row in mat1:
    print(row)

for row in mat2:
    print(row)
result=[]
print("scalor multiplication")
for row in mat1:
    for value in row:
        result=2 * value

print(result)
result2=[]
for i in range(len(mat1)):
    row=[]
    for j in range(len(mat1[0])):
        row.append(2* mat1[i][j])
    result2.append(row)
print(result2)
for row in result2:
    print(row)
trans=[]
for i in range(len(mat1[0])):
    row=[]
    for j in range(len(mat1)):
        row.append(mat1[j][i])
    trans.append(row)

print(trans)
