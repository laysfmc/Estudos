"""
Desafio2:Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex.: Digite um número: 1834
Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1.
    """

#inputs e variáveis 
num = (input('Informe um número inteiro de 0 a 99990035: '))
unidade = format(num[3])
dezena = format(num[2])
centena = format(num[1])
milhar = format(num[0])

#prints
print('unidade:', unidade)
print('dezena:', dezena)
print('centena:', centena)
print('milhar:', milhar)