#ex6
#Digite um número e imprima se ele é primo ou não
num = int(input("Digite um número: "))

if num >= 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é número é primo")
            break
    else:
        print(f"{num} é primo")

else:
    print('Você digitou 0 ou um número negativo')