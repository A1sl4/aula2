n1 = float(input("Digite o primeiro numero "))
n2 = float(input("Digite o segundo numero "))

operacao = int(input("Selecione a operação:1.Adição; 2.Subtração; 3.divisão; 4.multiplicação "))

if operacao == 1:
  adicao = n1 + n2
  print(f"O resultado é: {adicao}")
elif operacao == 2:
  subtracao = n1 - n2
  print(f"O resultado é: {subtracao}")
elif operacao == 3:  
  divisao = n1 / n2
  print(f"O resultado é: {divisao}")
elif operacao == 4:
  multiplicação = n1 * n2
  print(f"O resultado é: {multiplicação}")
