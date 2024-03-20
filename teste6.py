#Exercício 6 - Como eu não sabia o que fazer para armazenar os números digitados em pares e ímpares, busquei a solução no google e o adaptei para essa atividade. 
#O código que eu havia feito primeiramente é esse que está com #.
#numero = float(input("Digite um número inteiro: "))
#resultado = (numero % 2)

#if resultado == 0:
    #print(f"O número {numero} é par!")
#else:
    #if resultado == 1:
        #print(f"O número {numero} é ímpar!")

NUMEROS = 5
pares = []
impares = []

for i in range(NUMEROS):
    numero = float(input("Digite um número inteiro: "))
    resultado = (numero % 2)
    if resultado == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nPares")
for numero in pares:
    print(f"{numero}", end=" ")

print("\nImpares")
for numero in impares:
    print(f"{numero}", end=" ")