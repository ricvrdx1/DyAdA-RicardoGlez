lado1 = int(input("Ingresa el lado de tu figura: "))
lado2 = int(input("Ingresa el lado de tu figura: "))
lado3 = int(input("Ingresa el lado de tu figura: "))
lado4 = int(input("Ingresa el lado de tu figura: "))

if lado1 == lado2 == lado3 == lado4:
    print("Tu figura es un cuadrado")
elif (lado1 == lado2 and lado3 == lado4) or (lado1 == lado3 and lado2 == lado4) or (lado1 == lado4 and lado3 == lado2):
    print("Tu figura es un rectángulo")
else:
    print("Tu figura es algun otro cuadrilatero")