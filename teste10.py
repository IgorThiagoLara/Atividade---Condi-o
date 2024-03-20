#Exercício 10
univ = float(input("Qual o código da sua universidade? PUCPR(1) ou UniCamp(2):  "))
nota1 = float(input("Qual a sua nota no primeiro bimestre? "))
nota2 = float(input("Qual a sua nota no segundo bimestre? "))
media = (nota1+nota2)/2

if univ ==1 and media >=7:
    print("Aprovado na PUCPR!")
elif univ ==1 and media >=4 and media <7:
    print("Em exame na PUCPR!")
else:
    if univ ==1 and media <4:
        print("Reprovado na PUCPR!")
    if univ ==2 and media >=5:
        print("Aprovado na UniCamp!")
    if univ ==2 and media <5:
        print("Reprovado na UniCamp!")
