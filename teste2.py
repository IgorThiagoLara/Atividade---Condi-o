#Exercício 2

a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))
delta = b**2-4*a*c
x1 = (-b + delta)/2*a
x2 = (-b - delta)/2*a

if delta >=1:
    print(f"Como delta é {delta}, existem duas raízes distintas")
    print(f"o resultado 1 é: {x1}")
    print(f"o resultado 2 é: {x2}")
elif delta ==0:
    print(f"Como delta é {delta}, existem duas raízes reais iguais")
    print(f"o resultado 1 é: {x1}")
    print(f"o resultado 2 é: {x2}")
elif delta <0:
    print(f"Como delta é {delta}, existem duas raízes imaginárias")
    print(f"o resultado 1 é: {x1}")
    print(f"o resultado 2 é: {x2}")
