numero = int(input('Digite um número para a análise: '))
print('''Escolha uma das bases para conversão
  [ 1 ] converter para BINÁRIO 
  [ 2 ] converter para OCTAL
  [ 3 ] converter para HEXADECIMAL ''')
opcao = int(input('Qual sua opcao: '))

if opcao == 1:
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida')
    