num = int(input('Digite um número: '))
print('''Escolha a opção de converção: 
[1] Converter em binário:
[2] Converter em hexadecimal:
[3] Convertes em octal: ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Seu número convertido para binário é {}' .format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Seu número convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
elif opção == 3:
    print('{} Seu número convertido para occtal é {}'.format(num, oct(num)[2:]))
else:
    print('Opção Inválida. Tente Novamente. ')

