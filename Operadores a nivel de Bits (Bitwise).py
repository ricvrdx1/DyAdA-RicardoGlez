x = 22

#Imprime el valor en binario
print ("1. x       =       {: >6b}". format ( x ) )
#AND
print ("2. x & 10   = {: >3d} = {: >6b}". format ( x & 10 , x & 10) )
#OR
print ("3. x | 1   = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )
#XOR
print ("4. x ^ 4   = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )
#NOT
print ("5. ~x      = {: >3d} = {: >6b}". format (~ x , ~ x ) )
#Desplaza los bit una posicion izquierda = multiplicar por 2
print ("6. x << 1  = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )
#Desplaza los bit dos pocisiones a la derecha = dividir entre 4
print ("7. x >> 2  = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )