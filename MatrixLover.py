import random

class Matrix:
    
    def __init__(self, r, c):                                               #initial function, creates an array of zeros with given dimensions
        try:
            self.r = r                                                      #rows
            self.c = c                                                      #columns
            self.mat1 = [[0 for j in range(c)] for i in range(r)]           #for loops that create array of 0
        except:                                                             #debugger except
            print("unable to make matrix")                              

    def print(self):                                                        #prints array in array format
        try:
            for i in range(self.r):
                for j in range(self.c):
                    print(self.mat1[i][j], end="\t")
                print()
        except:                                                             #debugger except
            print("not printable array")
                
    def set(self, r, c, new):                                               #set function, sets specific element of an array to a new value (new)
        self.mat1[r][c] = new
    
    def randomize(self,num1,num2):                                          #randomize function, randomizes numbers in an array to a number between num1 and
        for i in range(self.c):
            for j in range(self.r):
                self.set(j,i,random.randint(num1,num2))

    def plus(self, mat2):                                                   #plus function, adds two arrays together                                         
        if self.r == mat2.r and self.c == mat2.c:                           #checking if the dimensions of the ray make this function possible
            newmat = Matrix(self.r, self.c)                                 #creating an array with the same dimensions as self that will hold the sums
            for i in range(self.r):
                for j in range(self.c):
                    newmat.set (i,j,(self.mat1[i][j] + mat2.mat1[i][j]))    #setting the elements of the new array with sums
            return newmat
        else:
            print("Matrices are not able to be added")
            return self
    
    def times(self, mat2):                                                  #times function, multiplies two arrays together
        newmat = Matrix(self.r, mat2.c)                                     #newmat will hold all products
        if self.c == mat2.r:                                                #in order to multiply, the # of columns of the first matrix must equal the # of rows in the second matrix
            for i in range(self.r):
                for j in range(mat2.c):
                    answer = 0
                    for k in range(self.c):
                        answer += self.mat1[i][k] * mat2.mat1[k][j]         #answer holds new value for each element
                    newmat.set(i,j, answer)                                 #setting newmat with new values
            return newmat                                                   
        else:                                                               #debugger else
            print("matrices with these dimensions cannot be multiplied")
            return self

    def scalarTimesRow(self,rownum,num):                                    #scalarTimesRow function, multiples a chosen row by a num
        for i in range(self.c):
            new = (num * self.mat1[rownum][i])                              #new becomes new element value
            self.set(rownum,i,new)                                          #setting self with new values
    
    def switchRows(self, rownum1, rownum2):                                 #switchRows function, switches two desired rows
        row1 = []                                                           #array that holds first chosen row
        row2 = []                                                           #array that holds second chosen row
        for i in range(self.c):                                             #appending row1 with original first chosen row
            row1.append(self.mat1[rownum1][i])
        for i in range(self.c):                                             #appending row2 with original second chosen row
            row2.append(self.mat1[rownum2][i])
        for i in range(self.c):                                             #inputs contents of the row1 array into the second chosen row
            self.set(rownum2,i,(row1[i]))                           
        for i in range(self.c):                                             #inputs contents of the row2 array into the first chosen row
            self.set(rownum1,i,(row2[i]))
    
    def linearCombRows(self, num,rownum1,rownum2):                          #linearCombRows function, multiples a row by a number then adds it to another row
        row = []                                                            #this array will how the multiplied row
        for i in range(self.c):
            row.append(((self.mat1[rownum1][i])*num))                       #multiplying chosen row (rownum1) and appending it to row[]

        for i in range(self.c):                                             #setting second chosen row of self to the sum of the elements in row and the second chosen row
            self.set (rownum2,i,(self.mat1[rownum2][i] + row[i]))    

    def rowreduce(self):                                                    #rowreduce function, turns matrix into reduced row echelon form
        for i in range(self.c):
            if self.mat1[i][i]!=0:                                          #reduce the row to 1, except if that row starts with a 0
                divider1 = 1 / self.mat1[i][i]                              #divider1 is a fraction that will turn any element into 1 when mutlplied
                self.scalarTimesRow(i,divider1)                             #multiples each row by a divider that will turn self.mat[i][i] into 1
            for j in range(self.r):
                if j==i and self.mat1[i][i]==0:                             #if the row starts with a 0, it will swap it with the next row that doesn't start with a 0
                    k=j
                    while k < self.r:
                        if self.mat1[k][i]==0:                              #if the next row has a 0, skip to the next one
                            k=k+1
                        else:                                               #if the next row has a non zero, swap with next row
                            self.switchRows(j,k)
                            k = self.r
                elif j>i:
                    if self.mat1[j][i] != 0:                                #for each row, simplifies so the leading columns are 0
                        divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1   #divider become a multiple that will cancel out a leading element in a row once linearCombRows is applied
                        self.linearCombRows(divider2,i,j)                   #turns self.mat1[j][0] into 0
            if i == (self.r-1):
                break
        
        for i in range(self.r):                                             #this converts all numbers above the echelon into zero
            k=0
            if i > 0:
                while k<i:
                    num = self.mat1[k][i]*(-1)
                    self.linearCombRows(num,i,k)                            
                    k=k+1
        
        for i in range(self.r):                                             #makes sure no negative zeros exist in the final answer
            for j in range(self.c):
                if self.mat1[i][j] == -0.0:
                    self.mat1[i][j] = 0.0
    
    def invert(self):                                                       #invert function, inverts given matrix
        if self.r != self.c:                                                #if the matrix is not square, function cannot be performed
            print("this is not a square matrix, it cannot be inverted")
            return self
        else: 
            inverted = Matrix(self.r,self.c)                                #this matrix will hold final answer
            x = 0
            while x < self.c:
                inverted.set(x,x,1)                                         #inputing the 1s in echelon form
                x = x + 1

            for i in range(self.c):
                if self.mat1[i][i]!=0:                                      #reduce the row to 1, except if that row starts with a 0
                    divider1 = 1 / self.mat1[i][i]                          #divider1 is a fraction that will turn any element into 1 when mutlplied
                    self.scalarTimesRow(i,divider1)                         #multiples each row by a divider that will turn self.mat[i][i] into 1
                    inverted.scalarTimesRow(i,divider1)                     #any function performed on self is performed on the inverted matrix
                for j in range(self.r):
                    if j==i and self.mat1[i][i]==0:                         #if the row starts with a 0, swap it with the next row that doesn't start with a 0
                        k=j
                        while k < self.r:
                            if self.mat1[k][i]==0:                          #if the next row has a 0, skip to the next one
                                k=k+1
                            else:                                           #if the next row has a non zero, swap it on both matrices
                                self.switchRows(j,k)
                                inverted.switchRows(j,k)
                                k = self.r
                    elif j>i:
                        if self.mat1[j][i] != 0:                            #for each row, need to simplify so the leading columns are 0 on both matrices
                            divider2 = (self.mat1[j][i] / self.mat1[i][i])*-1   #divider become a multiple that will cancel out a leading element in a row once linearCombRows is applied
                            self.linearCombRows(divider2,i,j)               #turns self.mat1[j][0] into 0
                            inverted.linearCombRows(divider2,i,j)           #turns inverted.mat1[j][0] into 0
                if i == (self.r-1):
                    break

            for i in range(self.r):                                         #this converts all numbers above the echelon into zero for both matrices
                k=0
                if i > 0:
                    while k<i:
                        num = self.mat1[k][i]*(-1)                     
                        self.linearCombRows(num,i,k)
                        inverted.linearCombRows(num,i,k)
                        k=k+1
            
            for i in range(self.r):                                         #makes sure no negative zeros exist in the final answer
                for j in range(self.c):
                    if self.mat1[i][j] == -0.0:
                        self.mat1[i][j] = 0.0
    
            return inverted                                                 #return final answer