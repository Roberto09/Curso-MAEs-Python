def main():
    # For loops
    n = 10
    
    # range(start, end, increment)  donde se itera en el rango [start, end)
    # valores por default: range(start = 0, end, increment = 1)
    """
    for i in range(0, n, 1):
        print(i)
        
    # Se simplifica a:
    for i in range(n):
        print(i)

    for i in range(5, n, 1):
        print(i)
        

    for i in range(n, -1, -1):
        print(i)
       
    """
       
    # Listas
    # Creacion de listas
    mi_lista = []
    mi_lista2 = [1.5, 10.2, 4.8, -5.3]
    mi_lista3 = ["hola", "esto es", "una lista"]
    mi_lista4 = [1.5, "prueba", True, 123]
    #print(mi_lista4)
    
    mi_lista5 = [i for i in range(1, 11)]
    #print(mi_lista5)
    
    # Indexing
    numero = mi_lista2[2]
    #print(numero)
    
    # Metodos comunes: append, insert, pop, reverse, sort, []
    # len -> nos dice el tamaño de una lista
    
    # append
    #print(mi_lista2)
    mi_lista2.append(5.9)
    #print(mi_lista2)
    
    # insert
    #print(mi_lista3)
    #mi_lista3.insert(2, "prueba")
    #print(mi_lista3)
    
    # []
    #print(mi_lista3)
    #mi_lista3[2] = "prueba"
    # print(mi_lista3)
    
    # pop
    #print(mi_lista4)
    #mi_lista4.pop(2)
    #print(mi_lista4)
    #print(mi_lista4[2])
    
    # reverse
    # print(mi_lista5)
    # mi_lista5.reverse()
    # print(mi_lista5)
    
    # sort
    #print(mi_lista2)
    #mi_lista2.sort()
    #print(mi_lista2)

    # len
    # print(len(mi_lista4))

    # Iterando sobre listas
    #for num in mi_lista2:
    #    print('El numero es: ', num)

    #for i in range(0, len(mi_lista2)):
    #    print ('El numero en la posicion ', i , ' es: ', mi_lista2[i])
    
    # Matrices
    # matriz de 4 x 3
    mi_matriz=[[2, 2, 1],
               [3, 2, 8],
               [1, 2, 3],
               [4, 3, 2]]
    
    #print(len(mi_matriz[0]))
    #print(len(mi_matriz), ' x ', len(mi_matriz[0]))
    
    """
    # Iterando sobre matriz
    for row_list in mi_matriz:
        print(row_list)
        for num in row_list:
            print("num: ", num)
    
    for row in range(len(mi_matriz)):
        for col in range(len(mi_matriz[row])):
            print(mi_matriz[row][col], end = ' ')
        print('')
            
    """
    
    """
    for row in range(len(mi_matriz)):
        for col in range(len(mi_matriz[row])):
            print(mi_matriz[row][col], end = ' ')
        print('')
    
    print('-------------')
    mi_matriz[1].reverse()
    
    for row in range(len(mi_matriz)):
        for col in range(len(mi_matriz[row])):
            print(mi_matriz[row][col], end = ' ')
        print('')
    """
    
    
if __name__ == '__main__':
    main()