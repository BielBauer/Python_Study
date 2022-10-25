n = int(input("Digite um número inteiro positivo: "))
x = 1

if n > 0:
    while x % 2 != 0 and x <= n * 2:
        print(x)
        x = x + 2
else:
    print("O número digitado não é inteiro positivo.")
