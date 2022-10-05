# Solicitar que el usuario ingrese Nombre y DNI, guardarlo en distintas variables e imprimir
# por pantalla “El nombre del usuario es XXXXXX y su DNI es YYYYYY”

def main():
    nombre= input("Ingrese su nombre")
    dni= input("Ingrese su DNI")

    # estoy imprimiendo los valores de la siguiente forma
    print(f'El nombre del usuario es {nombre}')
    print(f'El DNI es {dni}')

if __name__ =='__main__':
    main()