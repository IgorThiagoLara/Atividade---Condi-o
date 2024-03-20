#Exercício 4

media = float(input("informe a sua média: "))
if media >=7:
    print("Estudante aprovado")
elif media >=4 and media < 7 :
    print("Exame final")
    diferenca = 7-media
    print(f"Estudante em recuperação por {diferenca:.2f} pontos.")
else:
    print("Estudante reprovado")