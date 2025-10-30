

class Matrices:
    def __init__(self, data):
        if len(data)==0:
            raise ValueError("matrix cannot be zero\n")

        no_of_col= len(data[0])
        for rows in data:
            if(len(rows)!=no_of_col):
                raise ValueError("invalid data")

        print("valid\n")
        self.data=data
        self.rows=len(data)
        self.cols=no_of_col
        self.shape=[self.rows,self.cols]

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
        if(isinstance(index,tuple)):
            row,col=index
            self.data[row][col]=element
        else:
            if len(element)!=self.cols or is_instance(list,element):
                raise ValueError("no of coloumns is not correct")
            else:
                self.data[index]=element

    def __eq__(self, other):
        if not isinstance(other, Matrices):
            return False
        else:
            if(self.rows!=other.rows and self.cols!=other.cols):
                return False
            else:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.data[i][j]!=other.data[i][j]:
                            return False

                return True


    def __add__(self, other):
        if not isinstance(other, Matrices):
           raise TypeError("invalid data")
        if self.rows!=other.rows or self.cols!=other.cols:
            raise ValueError("addition not possible")

        add=[]
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                result=self.data[i][j]+other.data[i][j]
                row.append(result)
            add.append(row)
        return Matrices(add)

    def __sub__(self, other):
        if not isinstance(other, Matrices):
            raise ValueError("invalid data")

        if (self.rows!=other.rows and self.cols!=other.cols):
            raise ValueError("subtraction not possible")

        sub=[]
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                result=self.data[i][j]-other.data[i][j]
                row.append(result)
            sub.append(row)
        return Matrices(sub)
#scalor multiplication
    def __mul__(self, scalor):
        result=[]
        new_row=[]
        for row in self.data:
            new_row=[]
            for value in row:
                new_row.append(value*scalor)
            result.append(new_row)

        return Matrices(result)


    def __rmul__(self,others):
        return self.__mul__(others)


    def __matmul__(self, other):
        if not isinstance(other, Matrices):
            raise ValueError("invalid data")
        if self.cols!=other.rows:
            raise ValueError("multiplication not possible")

        result=[]
        for i in range(self.rows):
            rows=[]
            for j in range(other.cols):
                add=0
                for k in range(self.cols):
                    add+=self[i][k]*other[k][j]
                rows.append(add)
            result.append(rows)

        return Matrices(result)

    def transpose(self):
        trans=[]
        for i in range(self.cols):
            row=[]
            for j in range(self.rows):
                value=self.data[j][i]
                row.append(value)
            trans.append(row)

        return matrices(trans)

    @classmethod
    def identity(cls,order):
        identity_matrix=[]
        for i in range(order):
            row=[]
            for j in range(order):
                if i==j:
                    row.append(1)
                else:
                    row.append(0)
            identity_matrix.append(row)
        return matrices(identity_matrix)
    @classmethod
    def zeros(cls,rows,col):
        if  isinstance(rows<=0 or col<=0):
            raise ValueError("invalid entery")
        result=[]
        for i in range(rows):
            row=[]
            for j in range(col):
                row.append(0)
            result.append(row)
        return cls(result)


mat1_data=[[1 ,2 ,3 ],
           [4 ,5 ,6]]
mat2_data=[[4, 5 ],
           [4 , 9],
           [4, 7 ]]

matrixA=Matrices(mat1_data)
matrixB=Matrices(mat2_data)

#display matrices


print("matrixA\n")
matrixA.display_matrix()
print("matrixB\n")
matrixB.display_matrix()
print(f"order_of_matrixA is {matrixA.rows} x {matrixA.cols}\n")
print(f"order_of_matrixB is {matrixB.rows} x {matrixB.cols}")


print("addition of matrices gives\n")
#result= matrixA+matrixB
# result.display_matrix()
print("subtraction of matrices give\n")
#subtract=matrixA-matrixB
#subtract.display_matrix()

print("scalor multiplication\n")
result=matrixA*3
result.display_matrix()

print("multiplication of matrices\n")
result=matrixA @ matrixB
result.display_matrix()
