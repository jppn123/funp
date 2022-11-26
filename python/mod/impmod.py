from modulo import sub,sum

m1 = [[1,2],[3,4]]  
m2 = [[4,4],[4,4]]
m3 = sum(m1,m2)
m4 = []

tam = len(m1)
for y in range(tam):
    m4 = m4 + [[] * tam]
for y in range(tam):
    for x in range(tam):
        m4[y].append(m3[y][x] * 2)  

m5 = sub(m4,m2)   
print("matriz final: ")
for x in range(tam):
    for y in range(tam):
        print(f'{m5[x][y]:5}', end = " ")
    print()