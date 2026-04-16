import os
os.system("clear")

# “Tienda Pokémon”
# Eres el encargado de desarrollar un programa para una tienda Pokémon llamada “PokéMarket”. En esta tienda, los entrenadores pueden comprar distintos objetos para sus aventuras.
# Objetivo
# Crear un programa en Python que permita simular el proceso de compra de un entrenador Pokémon, aplicando descuentos según ciertas condiciones y validando correctamente los datos ingresados.
 
# Requerimientos
# 1.	Mostrar menú de productos: 
# El programa debe mostrar el siguiente menú:
# 1. Pokébola → $1000
# 2. Poción → $1500
# 3. Revivir → $3000
# 4. Baya → $500
# 5. Finalizar compra

print("\n" "Tienda Pokemon ⚈ ․̫ ⚈\n")
contador_revivir = 0
total_revivir=0
descuento = 0
contador_productos = 0
acumulador_precio = 0
flag = True

while flag:

    print("1. Pokébola → $1000")
    print("2. Poción → $1500")
    print("3. Revivir → $3000")
    print("4. Baya → $500")
    print("5. Finalizar compra")


    try:
        opcion = int(input("Ingrese el producto que quiere comprar:"))

        if opcion == 1:
            cantidad = int(input("Ingrese cantidad:"))
            acumulador_precio = 1000 * cantidad
            contador_productos = contador_productos + cantidad
            print("Has comprado Pokebola ;)")
        elif opcion ==2:
            cantidad = int(input("Ingrese cantidad:"))
            acumulador_precio = 1500 * cantidad
            contador_productos = contador_productos + cantidad
        elif opcion == 3:
            cantidad = int(input("Ingrese cantidad:"))
            acumulador_precio = 3000 * cantidad
            contador_productos = contador_productos + cantidad
            contador_revivir = contador_revivir + cantidad
            total_revivir = 3000 * cantidad 
        elif opcion == 4:
            cantidad = int(input("Ingrese cantidad:"))
            acumulador_precio = 500 * cantidad
            contador_productos = contador_productos + cantidad
        elif opcion == 5:
            flag = False
        else:
            print("Ingrese opción valida")
        
        continuar = int(input("¿Desea seguir comprando?\n 1. Si 2. No\n"))
        if continuar == 2 :
            flag = False
    except:
        print("Elige una opción existente")

descuento1=0
descuento2=0
descuento3=0


if acumulador_precio > 5000:
    descuento1 = 0.1
if contador_productos > 10:
    descuento2 = 0.05
if contador_revivir >= 3:
   descuento3= 0.15


valor_descuento1 = acumulador_precio * descuento1
valor_descuento2 = acumulador_precio  * descuento2
valor_descuento3 = total_revivir * descuento3

total_descuento = valor_descuento1 + valor_descuento2 + valor_descuento3

precio_descuento = acumulador_precio - total_descuento

print(f"Cantidad de productos vendidos: {contador_productos}")
print(f"Valor bruto: ${acumulador_precio}")
print(f"Total de descuento:{total_descuento}")
print(f"Valor con descuento: ${precio_descuento}")







# 2.	Ingreso de productos: 
# •	El usuario debe poder seleccionar productos ingresando el número correspondiente. 
# •	Validar que la opción ingresada sea correcta (entre 0 y 4). 
# •	Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 
# compra = 0
# pokebola = 1000
# pocion = 15000
# revivir = 3000
# pocion = 500

# try:
#     compra = int(input("Selecione los productos que quiere comprar (ejmp: 1):"))
#     if compra == 1:
#         compra = pokebola
    
#     elif compra == 2:
#         compra = pocion
    
#     elif compra == 3:
#         compra = revivir


        
#     cantidad = int(input("Ingrese cantidad a comparar:"))



# except:
#     print("Elije una producto")