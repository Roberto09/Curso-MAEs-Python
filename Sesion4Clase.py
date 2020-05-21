import os

def main():
    # 7.1.2 Matrices.
    # Repaso de matrices
    
    # Matriz -> lista de listas
    # Creacion de matrices:
    mi_matriz = [[2, 2, 1, 4],
                 [1, 5, 8, 9],
                 [2, 1, 3, 4]]
    
    """
    # Esa matriz tiene 3 filas y 4 columnas. Es de tamaño 3 x 4
    print(mi_matriz)
    

    
    # Usando len para los tamaños
    rows = len(mi_matriz) # 3
    cols = len(mi_matriz[0]) # 4
    
    
    # Indexing
    print(mi_matriz[1][2]) # indexing especifico
    print(mi_matriz[1]) # indexing por lista
    
    
    # Iterando por elemento
    for fila in mi_matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print('')
    
   
    rows = len(mi_matriz) # 3
    cols = len(mi_matriz[0]) # 4
    
    # Iterando por index
    for i in range(rows):
        for j in range(cols):
            print(mi_matriz[i][j], end=' ')
        print('')
            
    """
    
    # Strings
    # Metodos : find, lower, upper, replace, split
    # len -> tamño
    
    mi_string = 'este es un string este'
    """
    #len
    print(len(mi_string))
    
    
    # find
    pos = mi_string.find('ST')
    print(pos)
    
    
    # lower
    mi_string = mi_string.lower()
    print(mi_string)
    
    
    # upper
    mi_string = mi_string.upper()
    print(mi_string)
    
    
    # replace
    mi_string = mi_string.replace('este', 'AQUEL')
    print(mi_string)
    
    #split
    mi_string = 'Roberto Garcia A'
    #[start, end)
    print( mi_string[8:14] )
    
    
    mi_string = "hola " + " como estas" + " abc"
    print(mi_string)
    

    # Iterar sobre string metodo 1
    for char in mi_string:
        print(char)
           
        
    # Iterar sobre string metodo 2
    for i in range(len(mi_string)):
        print(mi_string[i])
    """
    
    
    # Archivos
    """
    # Modos de archivos : r : read, a : append, w : write, x : create
    archivo = open('archivito.txt', 'r')
    
    # Iterar sobre archivo
    for linea in archivo:
        print(linea)
        
    archivo.close()
       
    archivo2 = open('archivito2.txt', 'w')
    mis_oraciones = ['hola como', 'estas este es', 'un grupo de palabras']
    """

    for oracion in mis_oraciones:
        archivo2.write(oracion+'\n')
    
    archvio2.close()
    
    # revisar existencia de un archivo   debemos importar os -> import os)
    
    if os.path.exists('Sesion3.py'):
        print('si existe!')
    else:
        print('no existe!')
        
    
    
if __name__ == '__main__':
    main()