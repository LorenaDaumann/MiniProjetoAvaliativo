arquivo = open('teste.txt', 'w')

arquivo.write('Testando a barraa n')

arquivo.close()

#ler

arquivo_leitura = open('teste.txt', 'r')
texto = arquivo_leitura.read()
print(texto)

arquivo.close()

with open('text.txt', 'r') as arquivo_teste:
    texto_completo = arquivo_teste.read()
    print(texto_completo)
    
    