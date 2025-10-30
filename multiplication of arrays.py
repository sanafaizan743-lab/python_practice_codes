mat1=[[1,2 ,3],
      [3,4,5]]
mat2=[[5,6],[7,8],[1,2]]
def no_of_rows(mat1):
    return len(mat1)
def no_of_cols(mat1):
    return len(mat1[0])

r1=no_of_rows(mat1)
r2=no_of_rows(mat2)
c1=no_of_cols(mat1)
c2=no_of_cols(mat2)

def display_matrix(mat):
    for rows in mat:
        print(rows)

print("first matrix= \n")
display_matrix(mat1)
print("second matrix= \n")
display_matrix(mat2)

print("operations")
sum=0
result=[]
for i in range(r1):
    row=[]
    for j in range(c2):
        sum=0
        for k in range(c1):
            sum=sum+mat1[i][k]*mat2[k][j]
        row.append(sum)
    result.append(row)

display_matrix(result)

