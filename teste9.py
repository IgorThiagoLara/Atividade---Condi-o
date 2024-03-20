#Exercício 9

idade = int(input("Digite aqui sua idade: "))
tempoDSer = int(input("Digite aqui o seu tempo de serviço: "))

if idade >=65 or tempoDSer >=30:
    print("Você pode se aposentar")
elif tempoDSer >=25 and idade >=60:
    print("Você pode se aposentar por conta da combinação de tempo de serviço e idade") 
else:
    print("Você não consegue se aposentar no momento")
