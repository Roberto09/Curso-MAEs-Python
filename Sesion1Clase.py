import math

def formula_cuadratica(x, y, z):
    
    p = (-y + math.sqrt(pow(y, 2) - 4 * x * z))/(2*x)
    r =  (-y - math.sqrt(pow(y, 2) - 4 * x * z))/(2*x)
    
    return p, r

def main():
    x = 10.1234
    print(round(x, 2))
    
    """
    # Esto es una constante
    NOMBRE_ENTRENADOR = input("Dime tu nombre entrenador! ")
    
    
    # Esto es una varible
    edad_entrenador = int(input("Dime tu edad: "))
    
    print("Hola ", NOMBRE_ENTRENADOR, " tienes: ", edad_entrenador, " años!")
   
    print("Es momento de ayudar a Pikachu!")

    #Formula cuadratica (-b +- sqrt(pow(b, 2) - 4 * a * c))) / (2*a)
    
    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
    
    x1, x2 = formula_cuadratica(a, b, c)
    
    print("Pikachu debe atacar en los tiempos: ", round(x1, 2), " y ", round(x2, 2), " !")
    """
    
if __name__ == "__main__":
    main()
    