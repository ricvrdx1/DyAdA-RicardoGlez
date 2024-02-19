def conversor(num):
    unidades = ["", "Un ", "Dos ", "Tres ", "Cuatro ", "Cinco ", "Seis ", "Siete ", "Ocho ", "Nueve "]
    especiales = ["", "Once ", "Doce ", "Trece ", "Catorce ", "Quince ", "Dieciseis ", "Diecisiete ", "Dieciocho ", "Diecinueve "]
    decenas = ["", "Diez ", "Veinte ", "Treinta ", "Cuarenta ", "Cincuenta ", "Sesenta ", "Setenta ", "Ochenta ", "Noventa "]
    centenas = ["", "Ciento ", "Doscientos ", "Trescientos ", "Cuatroscientos ", "Quinientos ", "Seiscientos ", "Setecientos ", "Ochocientos ", "Novecientos "]

    grupo = [[""], ["Mil "], ["Millon "], ["Millones "], ["Billon "], ["Billones "], ["Trillon "]]

    if num == 0:
        return "CERO"

    if 1 <= num <= 9:
        return unidades[num]

    elif 11 <= num <= 19:
        return especiales[num - 10]

    elif 10 <= num <= 99:
        return decenas[num // 10] + (" Y " + conversor(num % 10) if num % 10 != 0 else "")

    elif 100 <= num <= 999:
        return centenas[num // 100] + (" " + conversor(num % 100) if num % 100 != 0 else "")

    resultado_final = ""
    grupo_index = 0

    while num > 0:
        grupo_numero = num % 1000
        if grupo_numero > 0:
            resultado = conversor(grupo_numero)
            resultado_final = resultado + grupo[grupo_index][0] + resultado_final

        grupo_index += 1
        num //= 1000

    return resultado_final.strip()

num = int(input("Ingresa un número: "))
resultado = conversor(num)
print(resultado)
