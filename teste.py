resp = int(input('Escolha uma das opções:\n 1.Somar dois números \n 2.Número ao Cubo\n'))
if resp == 1:
    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))
    resultado = n1 + n2
    print(f'O Resultado da soma de {n1} + {n2} é: {resultado}')
elif resp == 2:
    n1 = int(input("Digite um número:"))
    resultado = n1**3
    print(f'O resultado do {n1} ao Cubo é: {resultado}')
else:
    print('OPÇÃO INVÁLIDA.')
 
