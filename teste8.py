#Exercício 8

idade = float(input("Digite aqui sua idade: "))
if idade >=18 and idade <65: 
    print("Eleitor obrigatório!")
else:
    if idade ==16 and idade <18 or idade >=65:
        print("Eleitor facultativo")
    if idade <16:
        print("Não eleitor")