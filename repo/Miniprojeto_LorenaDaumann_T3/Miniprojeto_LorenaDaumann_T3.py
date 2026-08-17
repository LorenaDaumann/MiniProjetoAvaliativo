"""
==============================================================================
MINI-PROJETO AVALIATIVO - MÓDULO 1 - SEMANA 07
Visualização de Dados e Business Intelligence [T3]

Análise Exploratória de Dados (AED) da base "Varejo"
Aluna: Lorena Daumann | Turma: T3

Como executar:
- VSCode: instale as extensões "Jupyter" e "Python", coloque o arquivo
  Varejo.csv na mesma pasta deste script e rode "python Miniprojeto_LorenaDaumann_T3.py"
- Google Colab: faça upload deste script (ou copie o conteúdo para células),
  faça upload do Varejo.csv e execute todas as células.
==============================================================================
"""

# =============================================================================
# 0. IMPORTAÇÃO DAS BIBLIOTECAS
# =============================================================================
import pandas as pd
import numpy as np
import unicodedata

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)


def titulo(texto):
    """Imprime um cabeçalho padronizado para organizar a saída no terminal."""
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


# =============================================================================
# 1. CONFIGURAÇÃO DE COLUNAS
# -----------------------------------------------------------------------------
# A base "Varejo" do Kaggle pode vir com nomes de coluna ligeiramente
# diferentes (com/sem acento, maiúsculas, espaços, etc.). Em vez de "chutar"
# um nome fixo e quebrar o script, criamos uma função que PROCURA a coluna
# certa entre alguns nomes candidatos (ignorando acentos e caixa).
#
# Se, ao rodar, algum campo aparecer como "NÃO ENCONTRADA", basta abrir o
# Varejo.csv, ver o nome exato da coluna e adicioná-lo na lista de
# candidatos correspondente logo abaixo (ou digitar o nome direto entre
# aspas na variável, substituindo a chamada da função).
# =============================================================================

def normalizar(texto):
    """Remove acentos e deixa em minúsculo, para comparar nomes de coluna."""
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("utf-8")
    return texto


def encontrar_coluna(df, candidatos, obrigatoria=True):
    """Procura, entre os candidatos, o nome de coluna que existe no df."""
    colunas_normalizadas = {normalizar(c): c for c in df.columns}
    for candidato in candidatos:
        chave = normalizar(candidato)
        if chave in colunas_normalizadas:
            return colunas_normalizadas[chave]
        # também aceita coluna que CONTENHA o candidato (ex.: "numero_filhos_2023")
        for chave_real, nome_real in colunas_normalizadas.items():
            if chave in chave_real:
                return nome_real
    if obrigatoria:
        print(f"[ATENÇÃO] Nenhuma coluna encontrada para: {candidatos}. "
              f"Ajuste manualmente a variável correspondente na CONFIGURAÇÃO DE COLUNAS.")
    return None


# Nomes candidatos para cada campo lógico usado na análise.
# ADICIONE aqui outras variações se o Varejo.csv usar nomes diferentes.
CANDIDATOS = {
    "data": ["Data", "Data_Compra", "Data da Compra", "DataCompra", "Date"],
    "numero_compra": ["Numero_Compra", "Numero da Compra", "Nº Compra", "ID_Compra",
                       "Codigo_Compra", "Order ID", "Nota_Fiscal", "Numero_Pedido"],
    "cliente": ["Cliente", "ID_Cliente", "Nome_Cliente", "Nome", "Customer"],
    "genero": ["Genero", "Sexo"],
    "num_filhos": ["Numero_Filhos", "Numero de Filhos do Cliente", "Numero de Filhos",
                    "Qtd_Filhos", "N_Filhos", "Filhos", "Quantidade_Filhos"],
    "categoria": ["Categoria", "Category"],
    "produto": ["Produto", "Nome_Produto", "Product"],
    "valor": ["Valor", "Valor_Total", "Valor da Compra", "Preco", "Valor_Compra", "Total"],
    "quantidade": ["Quantidade", "Qtd", "Quantity"],
}


# =============================================================================
# 2. CARREGAMENTO DA BASE
# =============================================================================
titulo("ETAPA 1 - CARREGAMENTO DA BASE VAREJO")

CAMINHO_ARQUIVO = "Varejo.csv"

df = None
for enc in ("utf-8", "latin1", "cp1252"):
    try:
        df = pd.read_csv(CAMINHO_ARQUIVO, encoding=enc)
        # se o csv usar ";" como separador, o pandas lê tudo como 1 coluna só
        if df.shape[1] == 1:
            df = pd.read_csv(CAMINHO_ARQUIVO, encoding=enc, sep=";")
        print(f"Arquivo carregado com sucesso (encoding='{enc}').")
        break
    except UnicodeDecodeError:
        continue
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Não encontrei '{CAMINHO_ARQUIVO}'. Baixe a base em "
            "https://www.kaggle.com/datasets/namespaiva/base-varejo/data e coloque "
            "o arquivo Varejo.csv na mesma pasta deste script."
        )

# mapeia os nomes reais das colunas usando a configuração acima
COL_DATA = encontrar_coluna(df, CANDIDATOS["data"])
COL_NUM_COMPRA = encontrar_coluna(df, CANDIDATOS["numero_compra"], obrigatoria=False)
COL_CLIENTE = encontrar_coluna(df, CANDIDATOS["cliente"], obrigatoria=False)
COL_GENERO = encontrar_coluna(df, CANDIDATOS["genero"])
COL_FILHOS = encontrar_coluna(df, CANDIDATOS["num_filhos"])
COL_CATEGORIA = encontrar_coluna(df, CANDIDATOS["categoria"])
COL_PRODUTO = encontrar_coluna(df, CANDIDATOS["produto"], obrigatoria=False)
COL_VALOR = encontrar_coluna(df, CANDIDATOS["valor"])
COL_QUANTIDADE = encontrar_coluna(df, CANDIDATOS["quantidade"], obrigatoria=False)

print(f"\nColuna de data identificada........: {COL_DATA}")
print(f"Coluna de número da compra.........: {COL_NUM_COMPRA}")
print(f"Coluna de cliente...................: {COL_CLIENTE}")
print(f"Coluna de gênero.....................: {COL_GENERO}")
print(f"Coluna de número de filhos...........: {COL_FILHOS}")
print(f"Coluna de categoria..................: {COL_CATEGORIA}")
print(f"Coluna de produto....................: {COL_PRODUTO}")
print(f"Coluna de valor.......................: {COL_VALOR}")
print(f"Coluna de quantidade..................: {COL_QUANTIDADE}")

titulo("NÚMERO DE REGISTROS E COLUNAS")
print(f"Registros (linhas): {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

titulo("PRIMEIRAS LINHAS DA BASE")
print(df.head())

titulo("TIPOS DE DADOS DE CADA COLUNA")
print(df.dtypes)

titulo("INFORMAÇÕES GERAIS DO DATAFRAME")
print(df.info())


# =============================================================================
# 3. DIAGNÓSTICO DE PROBLEMAS NA BASE
# =============================================================================
titulo("ETAPA 2 - VALORES NULOS POR COLUNA")
nulos_por_coluna = df.isnull().sum()
print(nulos_por_coluna)

titulo("ETAPA 2 - LINHAS DUPLICADAS")
qtd_duplicadas = df.duplicated().sum()
print(f"Total de linhas duplicadas: {qtd_duplicadas}")

titulo("ETAPA 2 - CATEGORIAS VAZIAS/EM BRANCO")
if COL_CATEGORIA:
    categorias_vazias = df[COL_CATEGORIA].isna().sum() + (df[COL_CATEGORIA].astype(str).str.strip() == "").sum()
    print(f"Registros com categoria vazia ou nula: {categorias_vazias}")

titulo("ETAPA 2 - DATAS POTENCIALMENTE INVÁLIDAS")
if COL_DATA:
    datas_teste = pd.to_datetime(df[COL_DATA], errors="coerce", dayfirst=True)
    datas_invalidas = datas_teste.isna().sum() - df[COL_DATA].isna().sum()
    print(f"Datas com formato inválido (não nulas originalmente, mas não convertidas): {datas_invalidas}")

titulo("ETAPA 2 - IDENTIFICADOR DE COMPRA")
if COL_NUM_COMPRA:
    print(f"Número de registros: {df.shape[0]}")
    print(f"Número de compras (pedidos) distintas: {df[COL_NUM_COMPRA].nunique()}")
    print("Isso separa cada 'compra' (pedido) das linhas individuais, já que uma mesma "
          "compra pode ter mais de um produto/linha associado.")


# =============================================================================
# 4. LIMPEZA DOS DADOS
# =============================================================================
titulo("ETAPA 3 - LIMPEZA: TRATAMENTO DE CATEGORIAS VAZIAS (if/else)")

if COL_CATEGORIA:
    def preencher_categoria(valor):
        """Aplica uma regra condicional simples: se a categoria estiver vazia
        ou nula, marcamos como 'Sem Categoria' em vez de descartar a linha
        inteira (perderíamos informações de venda, cliente e valor)."""
        if pd.isna(valor) or str(valor).strip() == "":
            return "Sem Categoria"
        else:
            return valor

    df[COL_CATEGORIA] = df[COL_CATEGORIA].apply(preencher_categoria)
    print("Categorias vazias/nulas preenchidas com 'Sem Categoria'.")
    print(df[COL_CATEGORIA].value_counts().head(10))

titulo("ETAPA 3 - LIMPEZA: TRATAMENTO DE NULOS NUMÉRICOS")

# Para a coluna de número de filhos, optamos por IMPUTAR com a MEDIANA em vez
# de excluir as linhas: a coluna é central para a Etapa 4 (estatísticas
# descritivas) e descartar registros reduziria a amostra e enviesaria a
# análise. A mediana é preferida à média por ser mais robusta a valores
# extremos (ex.: clientes com número de filhos muito fora do padrão).
if COL_FILHOS:
    nulos_filhos_antes = df[COL_FILHOS].isnull().sum()
    mediana_filhos = df[COL_FILHOS].median()
    df[COL_FILHOS] = df[COL_FILHOS].fillna(mediana_filhos)
    print(f"'{COL_FILHOS}': {nulos_filhos_antes} valores nulos preenchidos com a mediana ({mediana_filhos}).")

# Para as demais colunas numéricas (ex.: dimensões físicas do produto, valor,
# quantidade), imputamos com a mediana da própria coluna pelo mesmo motivo:
# preservar o registro (que ainda tem cliente, categoria, data válidos) em
# vez de descartar a linha inteira.
colunas_numericas = df.select_dtypes(include=[np.number]).columns
for col in colunas_numericas:
    if col == COL_FILHOS:
        continue
    nulos_antes = df[col].isnull().sum()
    if nulos_antes > 0:
        mediana_col = df[col].median()
        df[col] = df[col].fillna(mediana_col)
        print(f"'{col}': {nulos_antes} valores nulos preenchidos com a mediana ({mediana_col:.2f}).")

# Para colunas de identificação (cliente, número da compra) um valor nulo
# compromete a rastreabilidade do registro, então essas linhas são removidas.
colunas_chave = [c for c in [COL_CLIENTE, COL_NUM_COMPRA] if c is not None]
if colunas_chave:
    linhas_antes = df.shape[0]
    df = df.dropna(subset=colunas_chave)
    print(f"Linhas removidas por falta de identificação (cliente/compra): {linhas_antes - df.shape[0]}")

titulo("ETAPA 3 - LIMPEZA: REMOÇÃO DE DUPLICATAS")
linhas_antes = df.shape[0]
df = df.drop_duplicates()
print(f"Linhas duplicadas removidas: {linhas_antes - df.shape[0]}")

titulo("ETAPA 3 - LIMPEZA: CONVERSÃO DE TIPOS (DATA -> datetime)")
if COL_DATA:
    df[COL_DATA] = pd.to_datetime(df[COL_DATA], errors="coerce", dayfirst=True)
    linhas_antes = df.shape[0]
    df = df.dropna(subset=[COL_DATA])
    print(f"Coluna '{COL_DATA}' convertida para datetime.")
    print(f"Linhas removidas por data inválida após conversão: {linhas_antes - df.shape[0]}")
    df["Ano"] = df[COL_DATA].dt.year
    df["Mes"] = df[COL_DATA].dt.month

print(df.dtypes)


# =============================================================================
# 5. ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS DO CLIENTE
# =============================================================================
titulo("ETAPA 4 - ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS DO CLIENTE")

if COL_FILHOS:
    media_filhos = df[COL_FILHOS].mean()
    mediana_filhos_final = df[COL_FILHOS].median()
    desvio_filhos = df[COL_FILHOS].std()
    moda_filhos = df[COL_FILHOS].mode().iloc[0]
    max_filhos = df[COL_FILHOS].max()
    min_filhos = df[COL_FILHOS].min()
    contagem_filhos = df[COL_FILHOS].count()

    print(f"Média..............: {media_filhos:.2f}")
    print(f"Mediana............: {mediana_filhos_final:.2f}")
    print(f"Desvio padrão......: {desvio_filhos:.2f}")
    print(f"Moda...............: {moda_filhos}")
    print(f"Máximo.............: {max_filhos}")
    print(f"Mínimo.............: {min_filhos}")
    print(f"Contagem...........: {contagem_filhos}")


# =============================================================================
# 6. PADRÕES DE AGRUPAMENTO (>= 2 AGRUPAMENTOS)
# =============================================================================
titulo("ETAPA 5 - AGRUPAMENTO 1: VENDAS TOTAIS POR GÊNERO")

vendas_por_genero = None
if COL_GENERO and COL_VALOR:
    vendas_por_genero = df.groupby(COL_GENERO)[COL_VALOR].sum().sort_values(ascending=False)
    print(vendas_por_genero)
    print(f"\nGênero com maior valor total em vendas: {vendas_por_genero.idxmax()}")

titulo("ETAPA 5 - AGRUPAMENTO 2: VENDAS TOTAIS E Nº DE COMPRAS POR CATEGORIA")

vendas_por_categoria = None
if COL_CATEGORIA and COL_VALOR:
    vendas_por_categoria = df.groupby(COL_CATEGORIA)[COL_VALOR].agg(["sum", "count"]).sort_values("sum", ascending=False)
    vendas_por_categoria.columns = ["Valor_Total", "Qtd_Compras"]
    print(vendas_por_categoria)
    print(f"\nCategoria com maior faturamento: {vendas_por_categoria['Valor_Total'].idxmax()}")

titulo("ETAPA 5 - AGRUPAMENTO 3 (EXTRA): TABELA DINÂMICA CATEGORIA x GÊNERO")

tabela_dinamica = None
if COL_CATEGORIA and COL_GENERO and COL_VALOR:
    tabela_dinamica = pd.pivot_table(
        df, values=COL_VALOR, index=COL_CATEGORIA, columns=COL_GENERO,
        aggfunc="sum", fill_value=0
    )
    print(tabela_dinamica)


# =============================================================================
# 7. EXPORTAÇÃO DA BASE LIMPA
# =============================================================================
titulo("ETAPA 6 - EXPORTANDO BASE LIMPA (df_limpo.csv)")
df.to_csv("df_limpo.csv", index=False, encoding="utf-8")
print("Arquivo 'df_limpo.csv' gerado com sucesso na pasta do projeto.")


# =============================================================================
# 8. CONCLUSÕES
# =============================================================================
titulo("CONCLUSÕES E PRINCIPAIS INSIGHTS")

conclusoes = []
conclusoes.append(f"1. A base final ficou com {df.shape[0]} registros após a limpeza "
                   f"(remoção de duplicatas, linhas sem identificação e datas inválidas).")

if COL_FILHOS:
    conclusoes.append(f"2. O número médio de filhos por cliente é {media_filhos:.2f}, com "
                       f"mediana {mediana_filhos_final:.2f} e moda {moda_filhos} — a proximidade entre "
                       f"média e mediana sugere uma distribuição sem muitos outliers extremos.")

if vendas_por_genero is not None:
    conclusoes.append(f"3. O gênero com maior volume de vendas foi '{vendas_por_genero.idxmax()}', "
                       f"totalizando {vendas_por_genero.max():.2f} em valor de compras.")

if vendas_por_categoria is not None:
    conclusoes.append(f"4. A categoria de maior faturamento foi "
                       f"'{vendas_por_categoria['Valor_Total'].idxmax()}', o que indica onde o "
                       f"varejo concentra a maior parte da receita.")

if COL_CATEGORIA:
    conclusoes.append(f"5. Havia registros sem categoria informada, tratados como 'Sem Categoria' "
                       f"em vez de descartados, preservando informações de venda e cliente.")

conclusoes.append("6. Como problema remanescente, recomenda-se validar a fonte dos valores nulos "
                   "originais (erro de coleta vs. ausência real de informação) antes de usar esta "
                   "base para decisões de negócio mais sensíveis.")

for c in conclusoes:
    print(c)

print("\nAnálise concluída. Utilize 'df_limpo.csv' para etapas seguintes (dashboards, etc.).")
