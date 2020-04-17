def es_un_alien(edad, continente, confesion_alien, es_capitan_america):
    if((confesion_alien == "si")
       or (continente != 'america' and continente != 'europa' and continente != 'africa' and continente != 'asia' and continente != 'onceania')
       or  ((edad < 0 or edad > 150) and not es_capitan_america)):
        return True
    else:
        return False

def main():
    edad = int(input("Dime tu eadad: "))
    continente = input("Dime, en que que continente vives (america, europa, africa, asia u oceania)?: ")
    confesion_alien = input("Eres un alien? (si, no): ")
    es_capitan_america = (input("Eres el capitan america? :O (True, False): ")) == "True"
    
    # Operadores logicos ORDEN:
    # (), ==, !=, >, >=, <, <=, is, is not, in, not in
    # not, and, or
    # True and True = True
    # True or False = False
    
    if(es_un_alien(edad, continente, confesion_alien, es_capitan_america)):
        print("Es un alien!")
    else:
        print("Es un humano")
        return

    
    print("Queremos saber mas de ti!: ")
    naves_tie, naves_millenium_falcon, naves_raddus = 0, 0, 0
    n = int(input("Cuantas naves tienes?: "))
    
    while(naves_tie + naves_millenium_falcon + naves_raddus < n):
        tipo = int(input("Que tipo de nave es? 1) tie, 2) milennium falcon, 3) raddus? "))
        cantidad = int(input("Cuantas tienes de ese tipo? :O :"))
        if tipo == 1:
            naves_tie += cantidad
        elif tipo == 2:
            naves_millenium_falcon += cantidad
        else:
            naves_raddus += cantidad
            
    print("las naves tie son: ", naves_tie)
    print("las naves millenium falcon son: ", naves_millenium_falcon)
    print("las naves raddus son: ", naves_raddus)
    
if __name__ == '__main__':
    main()