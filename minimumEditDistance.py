source="execution"
target="intention"

mat=[[0 for i in range(len(source)+1)] for j in range (len(target)+1)]

temp=0

for col in range(len(source)+1):
    mat[0][col]=temp
    temp=temp+1
temp=0
for row in range(len(target)+1):
    mat[row][0]=temp
    temp=temp+1

sub=0

for row in range(1,len(source)+1):
    for col in range(1,len(target)+1):
        print(source[col-1]," ",target[row-1])
        if source[col-1]==target[row-1]:
            sub=0
        else:
            sub=2

        mat[row][col]=min((mat[row-1][col]+1),(mat[row][col-1]+1),(mat[row-1][col-1]+sub))



print("AND THE ANSWER IS :",mat[len(target)][len(source)])
