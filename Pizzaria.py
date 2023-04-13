acumulador = 0#variavel criada para guardar e somar os valoresdentro do laço

print(' Bem-vindo a pizzaria da Francielle Alves Sousa!!!')
print('            **********************OPÇÕES**********************')
print('| Código |    Descrição    |    Pizza Média-M  | Pizza Grande-G(30% mais cara|')
print('|  21    |    Napolitana   |      R$ 20,00     |        R$ 26,00             |')
print('|  22    |    Margherita   |      R$ 20,00     |        R$ 26,00             |')
print('|  23    |    Calabresa    |      R$ 25,00     |        R$ 32,50             |')
print('|  24    |    Toscana      |      R$ 30,00     |        R$ 39,00             |')
print('|  25    |    Portuguesa   |      R$ 30,00     |        R$ 39,00             |')


while True:#laço de repetição
    codigo = int(input('Digite o codigo: '))
    tamanho = input('Digite o tamanho M/G: ')
    if (codigo == 21) and (tamanho == 'M'):#se o usuario digitar o  codigo e o tamanho que esta dentro do if retornará o valor que esta de acordo com a tabela mostrada
         acumulador = acumulador + 20
         print('Você escolheu sabor Napolitana, Tamanho {}'.format(tamanho))#como no if os elifs tbm retornarão o valor da tabela
    elif(codigo == 21) and (tamanho == 'G'):
         acumulador = acumulador + 26
         print('Você escolheu sabor Napolitana, Tamanho {}'.format(tamanho))
    elif (codigo == 22) and (tamanho == 'M'):
         acumulador = acumulador + 20
         print('Você escolheu sabor Margherita, Tamanho {}'.format(tamanho))
    elif (codigo == 22) and (tamanho == 'G'):
         acumulador = acumulador + 26
         print('Você escolheu sabor Margherita, Tamanho {}'.format(tamanho))
    elif (codigo == 23) and (tamanho == 'M'):
         print('Você escolheu sabor Calabresa, Tamanho {}'.format(tamanho))
         acumulador = acumulador + 25
    elif (codigo == 23) and (tamanho == 'G'):
         acumulador = acumulador + 32.50
         print('Você escolheu sabor Calabresa, Tamanho {}'.format(tamanho))
    elif (codigo == 24) and (tamanho == 'M'):
         acumulador = acumulador + 30
         print('Você escolheu sabor Toscana, Tamanho {}'.format(tamanho))
    elif (codigo == 24) and (tamanho == 'G'):
         acumulador = acumulador + 39
         print('Você escolheu sabor Toscana, Tamanho {}'.format(tamanho))
    elif (codigo == 25) and (tamanho == 'M'):
         acumulador = acumulador + 30
         print('Você escolheu sabor Portuguesa, Tamanho {}'.format(tamanho))
    elif (codigo == 25) and (tamanho == 'G'):
         acumulador = acumulador + 39
         print('Você escolheu sabor Portuguesa, Tamanho {}'.format(tamanho))
    else:
        print('Opção Inválida')#caso o usuario digite algo que nao esta dentro das condicionais
        continue
    resposta = int(input('Deseja escolher outra pizza? S/N \n1- SIM\n0- NÃO\n>>'))#o usuario responde se a resposta for 1 o programa retorna para o começo do laço
    if resposta == 1:
        continue
    else:
        print('O Total a pagar é R$ {:.2f}'.format(acumulador))#se a resposta nao for 1 o programa é encerrado e retorna a mensagem com o valor total a ser pago
        print('Obrigado por comprar conosco!!!')
        break
