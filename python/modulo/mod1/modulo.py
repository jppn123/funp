def sum(m, n):
    matriz = []
    if len(m) == len(n):
        tam = len(m)   
        for y in range(tam):
            matriz = matriz + [[] * tam]
        for y in range(tam):
            for x in range(tam):
                matriz[y].append(m[y][x] + n[y][x])  
        
        return matriz
    else:
        return "tamanho diferente entre as matrizes"
    
def sub(m,n):
    matriz = []
    if len(m) == len(n):
        tam = len(m)   
        for y in range(tam):
            matriz = matriz + [[] * tam]
        for y in range(tam):
            for x in range(tam):
                matriz[y].append(m[y][x] - n[y][x])  
        
        return matriz
    else:
        return "tamanho diferente entre as matrizes"
    
        
    
  
