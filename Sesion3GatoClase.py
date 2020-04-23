
def gano_horizontal(mtrx, simb):

    rows, columns = 3, 3
    
    for r in range(rows):
        hay_ganador = True
        for c in range(columns):
            if mtrx[r][c] != simb:
                hay_ganador = False
                break
        if hay_ganador:
            return True
        
    return False

def gano_horizontal(mtrx, simb):
    rows, columns = 3, 3
    for c in range(columns):
        hay_ganador = True
        for r in range(rows):
            if mtrx[r][c] != simb:
                hay_ganador = False
                break
        if hay_ganador:
            return True
    return False

def gano_diag_principal(mtrx, simb):
    print('a')
    
def gano_diag_inv(mtrx, simb):
    print('a')
    
    
def jugar_gato():
    mtrx = [['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']]
    
    # loop para pedir inputs

def main():
    jugar_gato()

    
if __name__ == '__main__':
    main()