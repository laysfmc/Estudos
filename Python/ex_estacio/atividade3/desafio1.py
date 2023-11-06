"""
Desafio 1: Crie um programa que leia o nome completo de uma pessoa e mostre:
 *O nome com todas as letras maiúsculas e minúsculas.
 *Quantas letras ao todo (sem considerar espaços).
 *Quantas letras tem o primeiro nome."""

#inputs e variáveis 
nome = input('Informe seu nome completo: ')

maiusculo = format(nome.upper())
minusculo = format(nome.lower())
qtdTotal = format(len(nome) - nome.count(' ') )
qtdPrimeiro = format(nome.find(' ')) #conta até esncontrar o parametro (espaço)

#prints
print('Seu nome em maiúsculo é: ', maiusculo)
print('Seu nome em minúsculo é: ', minusculo)
print('A quantidade de letras do seu nome completo é de: ', qtdTotal, ' letras')
print('A quantidade de letras do seu primeiro nome é de: ', qtdPrimeiro, ' letras')