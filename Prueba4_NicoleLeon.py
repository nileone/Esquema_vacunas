def menu_inicial():
    while True:
        print("\n****Menú de inicio****")
        print("1.- ”Reservar zapatillas")
        print("2.-Buscar zapatillas reservadas")
        print("3.-Ver stock de reservas")
        print("4.- Salir.")
        opcion=input("Ingrese su opcion: ")

        match opcion:
            case "1":
                reservacion_zapatillas()
            case "2":
                busqueda_zapatillas()
            case "3":
                stock_zapatillas()
            case "4":
                print("Programa terminado")
            case "_":
                print("Ingresa una opcion valida.")
            
def validacion_nombre():
     while True:
        nombre_valido=True
        nombre=input("Ingrese su nombre: ")
        
        for idx in nombre_reserva:
            if nombre == idx["nombre"]:
                print("Este nombre ya esta registrado")
                nombre_valido = False
                break

        if nombre_valido:
            break
        
def ingresar_clave():
    frase_correcta= "EstoyEnListaDeReserva"
    frase_ingresada= input("Ingrese la frase secreta: ")
    if frase_ingresada == frase_correcta:
        print("La frase secreta ingresada es correcta")
    else:
        print("La frase secreta ingresada es incorrecta")

def numero_stock():
    
        
menu_inicial()
    


    
    