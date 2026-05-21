
# try:
#     with engine.begin() as conn:
#         df.to_sql('titanic', conn, if_exists='replace', index=False)

#         query = 'SELECT "Sex", AVG("Survived") AS taxa FROM titanic GROUP BY "Sex";'
#         df_sql = pd.read_sql(query, conn)

#     print(df_sql)
# except SQLAlchemyError as err:
#     print("Erro ao acessar o banco de dados PostgreSQL:", err)
#     raise

# compreender o comportamento geral das vendas, identificar padrões, relações entre
# variáveis e características do desempenho comercial da empresa. A partir desse processo,
# espera-se a geração de insights relevantes, como distribuição de vendas e lucro por
# categoria, impacto dos descontos na rentabilidade, desempenho por segmento de cliente e
# tendências ao longo do tempo.


#IMPORTANDO AS BIBLIOTECAS
import pandas as pd
import matplotlib.pyplot as plt


#carregando o conjunto de dados
df = pd.read_csv(
    "/home/lorena/Documentos/ATIVIDADES-SCTEC/DesafioExtra2/SampleSuperstore.csv",
    encoding="latin1"
)


# VISUALIZAÇÃO INICIAL DOS DADOS
print("=" * 60)
print("DADOS DE VENDAS (CABEÇALHO)")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("INFORMAÇÕES DO DATAFRAME")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print("ESTATÍSTICAS DESCRITIVAS ")
print("=" * 60)
print(df.describe())




# ORGANIZAÇÃO E LIMPEZA DOS DADOS
print("\n" + "=" * 60)
print("VALORES NULOS")
print("=" * 60)
print(df.isnull().sum())

print("\n" + "=" * 60)
print("TOTAL DE LINHAS DUPLICADAS")
print("=" * 60)
print(df.duplicated().sum())#identificar quantas linhas estão duplicadas no dataframe

# removendo duplicatas
df = df.drop_duplicates()

# Convertendo datas
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=False) #dayfirst=False para interpretar o formato MM/DD/YYYY
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=False)

#crriando coluna de ano
df['Ano Pedido'] = df['Order Date'].dt.year #dt.year para extrair o ano da data de pedido
df['Ano Envio'] = df['Ship Date'].dt.year





# ANÁLISE EXPLORATÓRIA DE DADOS

print("\n" + "=" * 60)
print("QUANTIDADE DE TICKETS (PEDIDOS)")
print("=" * 60)

quant_tickets = df['Order ID'].nunique()
print(f"Quantidade total de tickets/pedidos: {quant_tickets}")

####################################################

print("\n" + "=" * 60)
print("QUANTIDADE DE TICKETS POR CLIENTE")
print("=" * 60)

tickets_por_cliente = df.groupby('Customer Name')['Order ID'].nunique()
print(tickets_por_cliente.sort_values(ascending=False).head(20













































































































































































)) #ascending=False para mostrar os clientes com mais pedidos no topo

####################################################

print("\n" + "=" * 60)
print("QUANTIDADE DE CLIENTES POR SEGMENTO")
print("=" * 60)

segmentos = df['Segment'].value_counts()
print(segmentos)

####################################################

print("\n" + "=" * 60)
print("ANO COM MAIOR QUANTIDADE DE VENDAS")
print("=" * 60)

vendas_ano = df.groupby('Ano Pedido')['Sales'].sum()

ano_maior_venda = vendas_ano.idxmax() #retorna o índice (neste caso, o ano) do valor máximo encontrado na série vendas_ano
valor_maior_venda = vendas_ano.max()#retorna o valor máximo encontrado na série vendas_ano, ou seja, o total de vendas do ano com maior volume de vendas

print(f"Ano com maior volume de vendas: {ano_maior_venda}")
print(f"Total vendido: ${valor_maior_venda:.2f}")

####################################################

print("\n" + "=" * 60)
print("ANO COM MAIS ENTREGAS/EMBARCAÇÕES")
print("=" * 60)

entregas_ano = df.groupby('Ano Envio')['Order ID'].count()

ano_maior_entrega = entregas_ano.idxmax()
qtd_entregas = entregas_ano.max()

print(f"Ano com mais entregas: {ano_maior_entrega}")
print(f"Quantidade de entregas: {qtd_entregas}")


####################################################

print("\n" + "=" * 60)
print("TIPO DE SHIP MODE MAIS UTILIZADO")
print("=" * 60)

ship_mode = df['Ship Mode'].value_counts()
print(ship_mode)

print(f"\nMais utilizado: {ship_mode.idxmax()}")#idxmax() para retornar o tipo de ship mode mais utilizado (o índice do valor máximo encontrado na série shipmode)

####################################################

print("\n" + "=" * 60)
print("REGIÃO COM MAIOR QUANTIDADE DE CLIENTES")
print("=" * 60)

clientes_regiao = df.groupby('Region')['Customer ID'].nunique()

print(clientes_regiao)

print(f"\nRegião com mais clientes: {clientes_regiao.idxmax()}")#idxmax() para retornar a região com maior quantidade de clientes (o índice do valor máximo encontrado na série clientes_regiao)
####################################################

print("\n" + "=" * 60)
print("PORCENTAGEM DE CADA CATEGORIA VENDIDA")
print("=" * 60)

categoria_pct = df['Category'].value_counts(normalize=True) * 100 #value_counts(normalize=True) para calcular a porcentagem de cada categoria em relação ao total de vendas, multiplicando por 100 para obter o valor em porcentagem

print(categoria_pct)

####################################################

print("\n" + "=" * 60)
print("PORCENTAGEM DE CADA SUB-CATEGORIA VENDIDA")
print("=" * 60)

subcategoria_pct = df['Sub-Category'].value_counts(normalize=True) * 100 #value_counts(normalize=True) para calcular a porcentagem de cada sub-categoria em relação ao total de vendas, multiplicando por 100 para obter o valor em porcentagem

print(subcategoria_pct)

####################################################

print("\n" + "=" * 60)
print("QUANTIDADE TOTAL DE ITENS VENDIDOS")
print("=" * 60)

total_itens = df['Quantity'].sum()

print(f"Quantidade total de itens vendidos: {total_itens}")

####################################################

print("\n" + "=" * 60)
print("QUANTIDADE DE ITENS VENDIDOS POR CATEGORIA")
print("=" * 60)

itens_categoria = df.groupby('Category')['Quantity'].sum()

print(itens_categoria)

####################################################

print("\n" + "=" * 60)
print("QUANTIDADE DE ITENS VENDIDOS POR SUB-CATEGORIA")
print("=" * 60)

itens_subcategoria = df.groupby('Sub-Category')['Quantity'].sum()

print(itens_subcategoria.sort_values(ascending=False)) #sort_values(ascending=False) para ordenar as sub-categorias pela quantidade de itens vendidos, do maior para o menor


####################################################


print("\n" + "=" * 60)
print("DESCONTOS TOTAIS")
print("=" * 60)

desconto_total = df['Discount'].sum()

print(f"Soma dos descontos aplicados: {desconto_total:.2f}")

####################################################

print("\n" + "=" * 60)
print("LUCRO BRUTO X LUCRO LÍQUIDO")
print("=" * 60)

lucro_bruto = df['Sales'].sum()
lucro_liquido = df['Profit'].sum()

print(f"Lucro Bruto (vendas totais): ${lucro_bruto:.2f}")
print(f"Lucro Líquido: ${lucro_liquido:.2f}")

####################################################

print("\n" + "=" * 60)
print("LUCRO LÍQUIDO COM DESCONTOS APLICADOS")
print("=" * 60)

# estimativa simples de valor descontado
valor_descontos = (df['Sales'] * df['Discount']).sum()

lucro_com_desconto = lucro_bruto - valor_descontos

print(f"Valor estimado perdido em descontos: ${valor_descontos:.2f}")
print(f"Lucro após descontos: ${lucro_com_desconto:.2f}")





# VISUALIZAÇÕES
# VENDAS POR ANO
plt.figure(figsize=(8, 5))

vendas_ano.plot(kind='bar')

plt.title("Vendas por Ano")
plt.xlabel("Ano")
plt.ylabel("Valor de Vendas")

plt.tight_layout()
plt.savefig("grafico_vendas_ano.png")

plt.show()
plt.close()


# SEGMENTOS DE CLIENTES
plt.figure(figsize=(8, 5))

segmentos.plot(kind='bar')

plt.title("Quantidade de Clientes por Segmento")
plt.xlabel("Segmento")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("grafico_segmentos.png")

plt.show()
plt.close()


# SHIP MODE
plt.figure(figsize=(8, 5))

ship_mode.plot(kind='bar')

plt.title("Tipos de Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Quantidade")

plt.tight_layout() #ajusta o layout para evitar sobreposição de elementos no gráfico
plt.savefig("grafico_shipmode.png")

plt.show()
plt.close()


# CATEGORIAS
plt.figure(figsize=(8, 5))

categoria_pct.plot(kind='pie', autopct='%1.1f%%') #kind='pie' para criar um gráfico de pizza, autopct='%1.1f%%' para mostrar a porcentagem de cada categoria no gráfico

plt.title("Porcentagem de Categorias Vendidas")
plt.ylabel("")

plt.tight_layout()
plt.savefig("grafico_categoria.png")

plt.show()
plt.close()


# SUBCATEGORIAS
plt.figure(figsize=(12, 6))

itens_subcategoria.sort_values(ascending=False).plot(kind='bar') #sort_values(ascending=False) para ordenar as subcategorias pela quantidade de itens vendidos, do maior para o menor, e kind='bar' para criar um gráfico de barras

plt.title("Itens Vendidos por Subcategoria")
plt.xlabel("Subcategoria")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.savefig("grafico_subcategoria.png")

plt.show()
plt.close()


# LUCRO X VENDAS
plt.figure(figsize=(8, 5))

valores = [lucro_bruto, lucro_liquido]
labels = ['Lucro Bruto', 'Lucro Líquido']

plt.bar(labels, valores)

plt.title("Lucro Bruto x Lucro Líquido")
plt.ylabel("Valor")

plt.tight_layout()
plt.savefig("grafico_lucro.png")

plt.show()
plt.close()





# INSIGHTS FINAIS

print("\n" + "=" * 60)
print("INSIGHTS PRINCIPAIS")
print("=" * 60)

print(f"""
1. Total de pedidos realizados: {quant_tickets}

2. Ano com maior volume de vendas:
   {ano_maior_venda} (${valor_maior_venda:.2f})

3. Ano com mais entregas:
   {ano_maior_entrega} ({qtd_entregas} entregas)

4. Método de entrega mais utilizado:
   {ship_mode.idxmax()}

5. Segmento com mais clientes:
   {segmentos.idxmax()}

6. Região com mais clientes:
   {clientes_regiao.idxmax()}

7. Categoria mais vendida:
   {categoria_pct.idxmax()}

8. Quantidade total de itens vendidos:
   {total_itens}

9. Lucro bruto total:
   ${lucro_bruto:.2f}

10. Lucro líquido total:
    ${lucro_liquido:.2f}

11. Valor estimado perdido em descontos:
    ${valor_descontos:.2f}
""")

print("\nGráficos salvos com sucesso!")
print("""
Arquivos gerados:
- grafico_vendas_ano.png
- grafico_segmentos.png
- grafico_shipmode.png
- grafico_categoria.png
- grafico_subcategoria.png
- grafico_lucro.png
""")