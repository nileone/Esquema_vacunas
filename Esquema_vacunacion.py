esquema = 5
completos = 0
incompletos = 0

while True:
    try: 
        pacientes = int(input("Ingrese cuantos personas se verificarán: "))
        break
    except ValueError:
        print("Debe ingresar un número entero")
    
for i in range(pacientes): # contador = 1 while contador <= pacientes:
    dosis = 10
    while dosis > esquema or dosis < 0:
        try: 
            dosis = int(input(f"Ingrese cantidad de dosis recibidas por la persona {(i+1)} (el esquema completo es de {esquema} dosis): "))
        except ValueError:
            print("Debe ingresar un número entero")
            
    if dosis == esquema:
        print("Esquema Completo")
        completos += 1
    else:
        print("Esquema Incompleto")
        incompletos += 1
     
print(f"Cantidad de personas con esquema completo: {completos}")   
print(f"Cantidad de personas con esquema incompleto: {incompletos}")   
    
