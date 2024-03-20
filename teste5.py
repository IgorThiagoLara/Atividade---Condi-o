#Exercício 5

sexo = (input("Qual é o seu sexo? Masculino(M) ou feminino(F): "))
altura = float(input("informe a sua altura: "))
masculino = (72.7*altura)-58
feminino = (62.1*altura)-44.7

if sexo == "M":
    print(f"O seu peso ideal é: {masculino}")
elif sexo == "F":
    print(f"o seu peso ideal é {feminino}: ")
else:
    print("Erro de digitação de sexo")  