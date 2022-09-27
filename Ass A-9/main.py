mat1=[[1,2,1],[2,0,1],[3,6,1]]
mat2=[[2,3,1],[3,1,1],[2,1,0]]

add=[[0,0,0],[0,0,0],[0,0,0]]
sub=[[0,0,0],[0,0,0],[0,0,0]]
mul=[[0,0,0],[0,0,0],[0,0,0]]
tran1=[[0,0,0],[0,0,0],[0,0,0]]
tran2=[[0,0,0],[0,0,0],[0,0,0]]

#_________Subtraction_____#

for i in range (len(mat1)):
    for j in range (len(mat1[i])):
        add[i][j]=mat1[i][j]+mat2[i][j]     # Addition
        sub[i][j]=mat1[i][j]-mat2[i][j]     # Subtraction

 #______Multiplication____#
        
for i in range(len(mat1)):
    for j in range (len(mat1[i])):
        for k in range (len(mat1[i])):
            mul[i][j]+= mat1[i][k]*mat2[k][j]

#________Transpose________#

for i in range (len(mat1)):
    for j in range(len(mat1[i])):
        tran1[i][j]=mat1[j][i]
        tran2[i][j]=mat2[j][i]




print(" Matrix 1 \t  Matrix2\t  Addition\tMultiplication \t transpose1 \t transpose 2")

for i in range (3):
    print(mat1[i],"\t",mat2[i],"\t",add[i],"\t",mul[i],"\t",tran1[i],"\t",tran2[i])

