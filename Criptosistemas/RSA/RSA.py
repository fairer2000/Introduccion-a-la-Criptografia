#RSA
#Equipo:
#Adolfo Armando Villegas Jiménez
#Alan Ignacio Delgado Alarcón

#El funcionamiento del programa es basico, se ingresa
#P y q, para que salga del loop los numeros tienen que ser primos.
#Una vez encontrados e y d se hace el cifrado y descifrado
#con un numero que ingrese el usuario.

def esNumeroPrimo(num):
  if num <= 1:
    return False
  for i in range(2,num):
    if num%i == 0:
      return False
  return True

def euclides(num_1, num_2):
  aux = 0
  while num_2 != 0:
    aux = num_1 % num_2
    num_1 = num_2
    num_2 = aux
  return num_1
  
def euclidesExtendido(num_1, num_2):
  
  d = 0
  x1 = 0
  x2 = 1
  y1 = 1
  
  aux_num_e = num_1
  aux_num_phi = num_2
  
  while aux_num_e > 0:
    aux_1 = aux_num_phi//aux_num_e
    aux_2 = aux_num_phi - (aux_1 * aux_num_e)
    aux_num_phi = aux_num_e
    aux_num_e = aux_2
    
    x = x2- aux_1 * x1
    y = d - aux_1 * y1
        
    x2 = x1
    x1 = x
    d = y1
    y1 = y
    
    if aux_num_phi == 1:
      result = d + num_2
      while(result > num_2):
        result = result - num_2
      
      return result

p = 0
q = 0
e = 0
d = 0

while(not esNumeroPrimo(p)):
  p = int(input("Ingresa un numero primo para P: "))

while(not esNumeroPrimo(q)):
  q = int(input("Ingresa un numero primo para q: "))

n = p*q
phi_n = (p-1)*(q-1)

for i in range(2,phi_n):
  if(euclides(i, phi_n) == 1):
    d = euclidesExtendido(i,phi_n)
    if(d != i):
      e = i
      if((d*e)%phi_n == 1):
        break

print("Llave publica: ", e)
print("Llave privada: ", d)

number = int(input("\n Ingrese un numero: "))

print("Cifrado: ")
cifrado = pow(number,e)%n
print(cifrado)

descifrado = pow(cifrado,d)%n
print("Descifrado: ")
print(descifrado)