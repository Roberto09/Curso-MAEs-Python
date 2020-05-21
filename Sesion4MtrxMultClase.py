def escribir_en_archivo(archivo, matriz):
    for fila in matriz:
        for elemento in fila:
            archivo.write(str(elemento) + ', ')
        archivo.write('\n')

def matmul(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if cols_a != rows_b:
        print('No se pueden multiplicar!')
        return
    
    # res es una matriz de rows_a X cols_b
    res = [[0 for i in range(cols_b)] for j in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += a[i][k] * b[k][j]
                
    return res
    

def main():
    m1 = [[1, 2, 8],
          [2, 5, 3],
          [1, 10, 9]]
    
    m2 = [[7, 5, 9],
          [2, 2, 2],
          [8, 1, 6]]
    
    res = matmul(m1, m2)
    
    archivo = open('archivito.txt', 'a')
    archivo.write('\n')
    escribir_en_archivo(archivo, res)
    archivo.close()
    
    print(res)
    
    
if __name__ == '__main__':
    main()