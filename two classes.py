class dim_mat():
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def order_of_matrix(self):
        print(f"order of matrix is {self.row} x {self.col}")

class Matrix():
    def __init__(self,data,dim_mat):
        self.data=data
        self.dim_mat=dim_mat

    def display_matrix(self):
        for rows in self.data:
                print(rows)

    def __getitem__(self,index):
        if isinstance(index,tuple):
            row,col=index
            return self.data[row][col]
        else:
            return self.data[index]

    def __setitem__(self, index, element):
        if isinstance(index,tuple):
            row,col=index
            self.data[row][col]=element
        else:
            if len(element)!=self.dim_mat.col or isinstance(list,element):
                raise ValueError("no of coloumns is not correct")
            else:
                self.data[index]=element

    def __add__(self, other):
        if not isinstance(other, Matrix):
           raise TypeError("invalid data")
        if self.dim_mat.row!=other.dim_mat.row or self.dim_mat.col!=other.dim_mat.col:
            raise ValueError("addition not possible")

        add=[]
        for i in range(self.dim_mat.row):
            row=[]
            for j in range(self.dim_mat.col):
                result=self.data[i][j]+other.data[i][j]
                row.append(result)
            add.append(row)
        return Matrix(add,self.dim_mat)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
           raise TypeError("invalid data")
        if self.dim_mat.row!=other.dim_mat.row or self.dim_mat.col!=other.dim_mat.col:
            raise ValueError("addition not possible")

        sub=[]
        for i in range(self.dim_mat.row):
            row=[]
            for j in range(self.dim_mat.col):
                result=self.data[i][j]-other.data[i][j]
                row.append(result)
            sub.append(row)
        return Matrix(sub,self.dim_mat)

    def __mul__(self, num):
        result=[]
        new_row=[]
        for row in self.data:
            new_row=[]
            for value in row:
                new_row.append(value*num)
            result.append(new_row)

        return Matrix(result,self.dim_mat)


    def __rmul__(self,others):
        return self.__mul__(others)


    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("invalid data")
        if self.dim_mat.col!=other.dim_mat.row:
            raise ValueError("multiplication not possible")

        result=[]
        for i in range(self.dim_mat.row):
            rows=[]
            for j in range(other.dim_mat.col):
                add=0
                for k in range(self.dim_mat.col):
                    add+=self[i][k]*other[k][j]
                rows.append(add)
            result.append(rows)
        dim_result=dim_mat(self.dim_mat.row,other.dim_mat.col)
        return Matrix(result,dim_result)

    def transpose(self):
        trans=[]
        for i in range(self.dim_mat.col):
            row=[]
            for j in range(self.dim_mat.row):
                value=self.data[j][i]
                row.append(value)
            trans.append(row)
        trans_dim=dim_mat(self.dim_mat.col,self.dim_mat.row)
        return Matrix(trans,trans_dim)

    @classmethod
    def identity(cls, dim_mat):
        identity_matrix = []
        for i in range(dim_mat.row):
            row = []
            for j in range(dim_mat.col):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            identity_matrix.append(row)
        return Matrix(identity_matrix,dim_mat)

    @classmethod
    def zeros(cls, dim_mat):
        if isinstance(dim_mat.row <= 0 or dim_mat.col <= 0):
            raise ValueError("invalid entry")
        result = []
        for i in range(dim_mat.row):
            row = []
            for j in range(dim_mat.col):
                row.append(0)
            result.append(row)
        return cls(result,dim_mat)

dataA=[[1, 2, 3],
       [3, 4, 5],
       [5, 6, 9]]
d1=dim_mat(len(dataA),len(dataA[0]))
matA=Matrix(dataA,d1)
matA.display_matrix()
d1.order_of_matrix()

dataB=[[2, 4, 7],
       [5, 7, 8],
       [3, 4, 7]]
d2=dim_mat(len(dataB),len(dataB[0]))
matB=Matrix(dataB,d2)
matB.display_matrix()
d2.order_of_matrix()
print("addition of matrices results in \n")
add_mat=matA+matB
add_mat.display_matrix()
print("subtraction of matrices gives\n")
sub_mat=matA-matB
sub_mat.display_matrix()
sub_mat.dim_mat.order_of_matrix()
print("scalor multiplication gives")
new_mat=matA*3
new_mat.display_matrix()
print("multiplication of matrices give\n")
mul_mat=matA@matB
mul_mat.display_matrix()
print("transpose of matrix A is\n")
transA=matA.transpose()
transA.display_matrix()
iden_dim=dim_mat(2,2)
