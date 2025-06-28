def menu_inicial():
    while True:
        print("\n****TOTEM DE AUTOATENCION RESERVA STRIKE****")
        print("1.- ”Reservar zapatillas")
        print("2.-Buscar zapatillas reservadas")
        print("3.-Ver stock de reservas")
        print("4.- Salir.")
        opcion=input("Ingrese su opcion: ")

        match opcion:
            case "1":
                reserva()
            case "2":
                buscar_reservas()
            case "3":
                stock_disponible()
            case "4":
                print("Programa terminado")
                break
            case "_":
                print("Ingresa una opcion valida.")
            
def validacion_nombre():
    while True:
        nombre_valido=True
        nombre=input("Ingrese su nombre: ")
        
        for idx in stock:
            if nombre == idx["nombre"]:
                print("Este nombre ya esta registrado")
                nombre_valido = False
                break

        if nombre_valido:
            break
        
    frase_correcta= "EstoyEnListaDeReserva"
    frase_ingresada= input("Ingrese la frase secreta: ")
    if frase_ingresada == frase_correcta:
        print("La frase secreta ingresada es correcta.Reserva ingresada.")
        return nombre
    else:
        print("La frase secreta ingresada es incorrecta")
        
def reserva():
    if stock_y_reservas[0]>0:

        nombre= validacion_nombre()
        categoria="standar"
        cantidad_reservas= 1
        persona_registrada={
            "nombre": nombre, 
            "categoria":categoria, 
            "cantidad_reservas": cantidad_reservas
        }
        stock.append(persona_registrada)
        stock_y_reservas[0]-=1
        stock_y_reservas[1]+=1
    else:
        print("No queda stock disponible")

# Reserva encontrada: Laura Mendez - 1 par(es) (estándar)
# .¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): si 
# Manteniendo reserva actual.

def buscar_reservas():
    persona_buscada=input("Ingresa el nombre de la reserva:")
    for idx in stock:
        if idx["nombre"]== persona_buscada:
            print(f"Reserva encontrada :{persona_buscada}- {idx['cantidad_reservas']} par(es) {idx['categoria']}")
            if idx['cantidad_reservas']<2:
                while True: 
                    VIP= input("Desea pagar adicional para VIP y reservar 2 pares? (si-no): ")
                    if VIP == "si": 
                        idx["categoria"]= "VIP"
                        idx["cantidad_reservas"]= 2
                        stock_y_reservas[0]-=1
                        stock_y_reservas[1]+=1
                        print("Cambio de categoria exitoso")
                        break    

                    elif VIP == "no":
                        print("Mantendiendo reserva actual") 
                        break    
                    else:
                        print("Ingresa una opcion valida")  
            else: 
                print("Este usuario alcanzo el max de resevas") 
                break
        else:
            print("El usuario ingresado no se encontró")

def stock_disponible():
    print(f"El stock actual es: {stock_y_reservas[0]}")
    print(f"Las reservas actuales son: {stock_y_reservas[1]}")
                            

stock=[]    
stock_y_reservas=[20,0]
menu_inicial()
        
menu_inicial()
    


    
    
