print("Calculadora")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
opcao = int(input("Digite a operação que deseja realizar."))

if(opcao == 1):
    print("Você escolheu a opção Soma")
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    resultado = num1+num2
    print("Resultado da soma: ",resultado)
elif (opcao == 2):
    print("Você escolheu a opção Subtração")
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    resultado = num1+num2
    print("Resultado da Subtração: ",resultado)
elif (opcao == 3):
    print("Você escolheu a opção Divisão")
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    resultado = num1+num2
    print("Resultado da Divisão: ",resultado)
elif (opcao == 4):
    print("Você escolheu a opção Multiplicação")
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    resultado = num1+num2
    print("Resultado da Multiplicação: ",resultado)
else:
    print("Resultado: Reprovado")    # Se não for nenhuma das opções acima (ou seja, menor que 5), entra aqui
   


    
    
    





















""" if(opcao == 1):
    print("Opção soma")
elif(opcao == 2):
    print("Opção subtração")
elif(opcao == 3):
    print("Opção divisão")
elif(opcao == 4):
    print("Opção multiplicação")
else:
    print("Opção inválida") """
