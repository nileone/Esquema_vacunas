productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
'8475HD': [387990,10], 
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], 
'123FHD': [290890,32], 
'342FHD': [444990,7],
'GF75HD': [749990,2], 
'UWU131HD': [349990,1], 
'FS1230HD': [249990,0], 
}


#funcion para opcion 1
def stock_marca(marca):
    encontrado = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            encontrado= True
            if modelo in stock:
                print(f"{modelo}:{stock[modelo][1]} notebooks de esa marca")
    if not encontrado:
        print("Lo sentimos. No hay stock para esa marca")   
        
        
# funcion para opcion 2
def busqueda_precio(p_min, p_max):
    resultados =  [0]
    for codigo in stock:
        precio= stock[codigo][0]
        stock_disponible = stock[codigo][1]
        if p_min <= precio <= p_max and stock_disponible > 0:
            resultados.append((productos[codigo][1],codigo))
    if not resultados:
        print("No hay notebooks en ese rango de precio")
    else:
        resultados.sort()
        for producto in resultados:
            print(producto)
        
                         
def menu_inicial():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca: ")
        print("2. Busqueda por precio: ")
        print("3. Actualizar precio: ")
        print("4. Salir: ")
        
        opcion= input("Ingresa una opcion: ")
        

        
        match opcion:
            case "1":
                marca= input("ingresa la marca que busca: ").lower()
                stock_marca(marca) 
            case "2":
                while True:
                    try:
                        p_min = int(input("Ingresa precio minimo: "))
                        p_max= int(input("Ingresa precio maximo: "))
                        if p_min> p_max:
                            print("El valor minimo no puede exceder el precio maximo! tonto")
                        else:
                            busqueda_precio(p_min, p_max)
                            break
                    except:
                        print("Ingresa un valor valido por favor")
                    
            case "4":
            
                print("Programa finalizado")
                break
                
menu_inicial()
            
                