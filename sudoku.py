from pysat.solvers import Glucose3
import numpy as np

def S(n,r,c,num):
    return int(num+(r-1)*n**2+(c-1)*n)

def initial_state(grid):
    clause=[]
    n=len(grid)

    for r in range(n):
        for c in range(n):
            if grid[r][c]!=0:
                number=[]
                number.append(S(n,r+1,c+1,grid[r][c]))
                clause.append(number)
    return clause

def R_1(n): # 每一行包含了每一个数
    clause1=[]
    for r in range(1,n+1):
        for num in range(1,n+1):
            number1=[]
            for c in range(1,n+1):
                number1.append(S(n,r,c,num))
            clause1.append(number1)
    return clause1

def R_2(n):   # 每一列包含了每一个数
    clause2=[]
    for c in range(1,n+1):
        for num in range(1,n+1):
            number2=[]
            for r in range(1,n+1):
                number2.append(S(n,r,c,num))
            clause2.append(number2)
    return clause2

def R_3(n):
    clause3=[]
    sub_n=int(n**0.5)
    for x in range(1,n+1):
        for v in range(1,n+1):
            number3=[]
            sub_r=((x-1)//sub_n)*sub_n+1
            sub_c=((x-1)%sub_n)*sub_n+1
            for i in range(sub_n):
                for j in range(sub_n):
                    number3.append(S(n,sub_r+i,sub_c+j,v))
            clause3.append(number3)
    return clause3

def R_4(n):
    clause4=[]
    for r in range(1,n+1):
        for c in range(1,n+1):
            for u in range(1,n):
                for num in range(u+1,n+1):
                    number4=[]
                    number4.append(0-S(n, r, c, u))
                    number4.append(0-S(n, r, c, num))
                    clause4.append(number4)
    return clause4

def S_reverse(n,v):
    v0=v%n
    if v0==0:
        v0=n
    nv=int((v-v0)/n)
    c=nv%n
    r=nv//n
    return (r+1,c+1,v0)

def final_sudoku(n,model,grid):
    for i in model:
        if i>0:
            r,c,v=S_reverse(n,i)
            grid[r-1][c-1]=v
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end=' ')
        print(end='\n')



def input_order():
    n=int(input('please input the order of your sudoku'))
    return n**2

def receiver(n):
    a=np.empty([n,n],dtype=int)
    for i in range(n):
        original_grid=input()
        b=original_grid.split()
        for j in range(n):
            a[i][j]=int(b[j])
    grid=[]
    for x in range(n):
        list1=[]
        for y in range(n):
            list1.append(a[x][y])
        grid.append(list1)
    return grid

n=input_order()
grid=receiver(n)
g=Glucose3()
clause_initial=initial_state(grid)
for clause in clause_initial:
    g.add_clause(clause)
r_1=R_1(n)
for cl1 in r_1:
    g.add_clause(cl1)

r_2=R_2(n)
for cl2 in r_2:
    g.add_clause(cl2)
r_3=R_3(n)
for cl3 in r_3:
    g.add_clause(cl3)
r_4=R_4(n)
for cl4 in r_4:
    g.add_clause(cl4)

print(g.get_model())
print(g.solve())
if g.solve():
    a=0
    for case in g.enum_models():
        final_sudoku(n,case,grid)
        a+=1
        if a==2:
            break
    model=g.get_model()
else:
    print(-1)









