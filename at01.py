#Soma
numero01 = float(input('Digite seu primeiro número:'))
numero02 = float(input('Digite seu segundo número:'))
soma = numero01 + numero02
print('A soma dos dois números é:', soma)

#Subtração
numero01 = float(input('Digite o primeiro número:'))
numero02 = float(input('Digite o segundo número:'))
subtracao = numero02 - numero01
print('A subtração dos dois números é:', subtracao)

#Multiplicação
numero01 = float(input('Digite seu primeiro número:'))
numero02 = float(input('Digite seu segundo número:'))
multiplicao = numero01 * numero02
print('A multiplicação dos dois números é:', multiplicao)

#Divisão
numero01 = float(input('Digite seu primeiro número:'))
numero02 = float(input('Digite seu segundo número:'))
if numero02 == 0:
   print('Não é possível dividir por zero')
else:
   divisao = numero01 / numero02
print('A divisão dos dois números é:', divisao)
