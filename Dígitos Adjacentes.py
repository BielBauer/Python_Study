valor = int(input("Entre com um número inteiro que eu direi se há dois dígitos adjacentes iguais: "))
DigitoAdjDif = True
Digito = 0
ProxDigito = 1

if valor > 9:
    while Digito != ProxDigito and DigitoAdjDif and valor > 9:
        Digito = valor % 10
        ProxDigito = (valor // 10) % 10
    print("Há dois dígitos adjacentes iguais!")
else:
    print("Não há dígitos adjacentes iguais!")
