print("Olá, Mundo!")

import csv

dados = [
    ['Produto', 'Preco', 'Estoque'],
    ['Notebook', '4500.00', '10'],
    ['Mouse Wireless', '120.00', '50'],
    ['Teclado Mecanico', '350.00', '25']
]

# CRIAR O ARQUIVO
with open('produtos.csv','w') as arquivo_produtos: # crio a conexao com open
    escritor = csv.writer(arquivo_produtos) # criei um escritor
    escritor.writerows(dados) # usei o escritor - realmente escrevi o arquivo


# LER O ARQUIVO - INTERPRETAR QUE É CSV
print("PRINT COM CSV READER")
with open('produtos.csv','r') as arquivo_produtos:
    escritor = csv.reader(arquivo_produtos) # recebe uma lista

    cabecalho = next(escritor)

    for linha in escritor:
        if linha[0] == 'Mouse Wireless':
            print(float(linha[1]) * 10/100)
        #print(type(linha)) # LISTA - BOM PARA PERCORRER E MANIPULAR


# LER COM OPEN - STR PURA
print("\nPRINT COM OPEN READ()")
with open('produtos.csv','r') as arquivo_produtos:
    escritor = arquivo_produtos.read()
    #print(type(escritor)) # STR - NÃO É IDEAL PARA MANIPULAÇÕES COMPLEXAS