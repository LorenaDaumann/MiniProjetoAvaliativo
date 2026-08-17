"""
==============================================================================
MINI-PROJETO AVALIATIVO - MÓDULO 1 - SEMANA 07
Visualização de Dados e Business Intelligence [T3]

Análise Exploratória de Dados (AED) da base "Varejo"
Aluna: Lorena Daumann | Turma: T3

Sobre a base:
A base Varejo é um recorte de compras de clientes de uma rede de
supermercados, no formato "1 linha = 1 item comprado dentro de uma compra".
Colunas (conforme documentação da base):
  DATA        - data da compra
  CO_ID       - identificação do número da compra (nota fiscal)
  CL_ID       - identificação do cliente
  CL_GENERO   - sexo biológico informado pelo cliente (M/F)
  CL_EC       - estado civil (1=Casado/União estável, 2=Divorciado,
                3=Separado, 4=Solteiro, 5=Viúvo)
  CL_FHL      - número de filhos do cliente
  CL_SEG      - segmentação econômica do cliente (classe A, B ou C)
  PR_ID       - código do produto (SKU)
  PR_CAT      - categoria do produto
  PR_NOME     - nome do produto

Como executar:
- VSCode: instale as extensões "Jupyter" e "Python", coloque o arquivo
  BaseVarejo.csv na mesma pasta deste script e rode:
      python Miniprojeto_LorenaDaumann_T3.py
- Google Colab: faça upload deste script (ou copie o conteúdo para células),
  faça upload da BaseVarejo.csv e execute todas as células.
==============================================================================
"""

# =============================================================================
# 0. IMPORTAÇÃO DAS BIBLIOTECAS
# =============================================================================
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)


def titulo(texto):
    """Imprime um cabeçalho padronizado para organizar a saída no terminal."""
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


# =============================================================================
# 1. CARREGAMENTO DA BASE
# =============================================================================
titulo("ETAPA 1 - CARREGAMENTO DA BASE VAREJO")

CAMINHO_ARQUIVO = "BaseVarejo.csv"  # a base usa ";" como separador de colunas

df = pd.read_csv(CAMINHO_ARQUIVO, sep=";", encoding="utf-8")

# O arquivo original tem ";;;;" sobrando no fim do cabeçalho, o que gera 4
# colunas fantasma ("Unnamed: 10" a "Unnamed: 13"), 100% vazias. Isso já é o
# primeiro problema de qualidade de dados encontrado na base: colunas sem
# nome e sem nenhum valor, artefato da exportação do arquivo original.
colunas_fantasma = [c for c in df.columns if c.startswith("Unnamed")]
print(f"Colunas fantasma encontradas (100% nulas, sem nome): {colunas_fantasma}")

titulo("NÚMERO DE REGISTROS E COLUNAS (ANTES DA LIMPEZA)")
print(f"Registros (linhas): {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

titulo("PRIMEIRAS LINHAS DA BASE")
print(df.head())

titulo("TIPOS DE DADOS DE CADA COLUNA")
print(df.dtypes)

titulo("INFORMAÇÕES GERAIS DO DATAFRAME")
print(df.info())


# =============================================================================
# 2. DIAGNÓSTICO DE PROBLEMAS NA BASE
# =============================================================================
titulo("ETAPA 2 - VALORES NULOS POR COLUNA")
print(df.isnull().sum())
# As colunas de negócio (DATA, CO_ID, CL_ID, CL_GENERO, CL_EC, CL_FHL,
# CL_SEG, PR_ID, PR_CAT, PR_NOME) não têm valores nulos tradicionais (NaN).
# O problema de dado ausente aqui aparece de duas formas "disfarçadas":
# (1) as 4 colunas fantasma, 100% nulas; e (2) o marcador "#N/D" usado na
# coluna PR_CAT no lugar de uma categoria real (ver próxima seção).

titulo("ETAPA 2 - LINHAS DUPLICADAS")
qtd_duplicadas = df.duplicated().sum()
print(f"Total de linhas totalmente duplicadas: {qtd_duplicadas}")

titulo("ETAPA 2 - CATEGORIAS DE PRODUTO VAZIAS/INVÁLIDAS (marcador #N/D)")
qtd_categoria_invalida = (df["PR_CAT"] == "#N/D").sum()
print(f"Registros com categoria marcada como '#N/D': {qtd_categoria_invalida}")
print(df["PR_CAT"].value_counts())

titulo("ETAPA 2 - DATAS EM FORMATO INVÁLIDO")
datas_teste = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
print(f"Datas que não conseguiram ser convertidas (formato inválido): {datas_teste.isna().sum()}")

titulo("ETAPA 2 - VALIDAÇÃO DO IDENTIFICADOR DE COMPRA (CO_ID)")
print(f"Total de linhas (itens comprados): {df.shape[0]}")
print(f"Total de compras (notas fiscais) distintas: {df['CO_ID'].nunique()}")
print(f"Total de clientes distintos: {df['CL_ID'].nunique()}")
# regra de negócio: cada CO_ID deve pertencer a um único cliente
co_id_por_cliente = df.groupby("CO_ID")["CL_ID"].nunique()
print(f"Compras associadas a mais de um cliente (inconsistência): {(co_id_por_cliente > 1).sum()}")


# =============================================================================
# 3. LIMPEZA DOS DADOS
# =============================================================================
titulo("ETAPA 3 - LIMPEZA: REMOÇÃO DAS COLUNAS FANTASMA (100% nulas)")
# Optamos por REMOVER essas colunas (em vez de imputar) porque não carregam
# nenhuma informação: são apenas um artefato do arquivo CSV original.
df = df.drop(columns=colunas_fantasma)
print(f"Colunas restantes: {df.shape[1]}")

titulo("ETAPA 3 - LIMPEZA: CATEGORIA DE PRODUTO (if/else)")


def preencher_categoria(valor):
    """Regra condicional: quando a categoria do produto vem marcada como
    '#N/D' (ausência de informação), substituímos por 'Sem Categoria' em vez
    de descartar a linha inteira, preservando a compra, o cliente e o
    produto associados a esse registro."""
    if valor == "#N/D" or pd.isna(valor):
        return "Sem Categoria"
    else:
        return valor


df["PR_CAT"] = df["PR_CAT"].apply(preencher_categoria)
print("Categorias '#N/D' substituídas por 'Sem Categoria'.")
print(df["PR_CAT"].value_counts())

titulo("ETAPA 3 - LIMPEZA: REMOÇÃO DE DUPLICATAS")
# Cada linha representa um item comprado; como a base não tem uma coluna de
# "quantidade", uma linha idêntica repetida (mesma compra, mesmo cliente,
# mesmo produto, mesma data) é tratada como erro de duplicação no arquivo,
# e não como "comprou 2 unidades do mesmo item" — essa é uma limitação da
# base que fica registrada nas conclusões, ao final do script.
linhas_antes = df.shape[0]
df = df.drop_duplicates()
print(f"Linhas duplicadas removidas: {linhas_antes - df.shape[0]}")

titulo("ETAPA 3 - LIMPEZA: CONVERSÃO DE TIPOS (DATA -> datetime)")
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
linhas_antes = df.shape[0]
df = df.dropna(subset=["DATA"])
print(f"Linhas removidas por data inválida após conversão: {linhas_antes - df.shape[0]}")
df["ANO_COMPRA"] = df["DATA"].dt.year
print(df.dtypes)

titulo("NÚMERO DE REGISTROS APÓS A LIMPEZA")
print(f"Registros (linhas): {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")


# =============================================================================
# 4. ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS DO CLIENTE
# =============================================================================
titulo("ETAPA 4 - ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS DO CLIENTE")

# IMPORTANTE: CL_FHL é um atributo do CLIENTE, repetido em toda linha das
# compras daquele cliente. Calcular a estatística direto sobre as 830 mil
# linhas daria mais peso aos clientes que compraram mais vezes (viés).
# Por isso, resumimos a base para 1 linha por cliente antes de calcular.
clientes = df.drop_duplicates(subset="CL_ID")[["CL_ID", "CL_GENERO", "CL_EC", "CL_FHL", "CL_SEG"]]
print(f"Base reduzida a nível de cliente: {clientes.shape[0]} clientes únicos.")

media_filhos = clientes["CL_FHL"].mean()
mediana_filhos = clientes["CL_FHL"].median()
desvio_filhos = clientes["CL_FHL"].std()
moda_filhos = clientes["CL_FHL"].mode().iloc[0]
max_filhos = clientes["CL_FHL"].max()
min_filhos = clientes["CL_FHL"].min()
contagem_filhos = clientes["CL_FHL"].count()

print(f"Média..............: {media_filhos:.2f}")
print(f"Mediana............: {mediana_filhos:.2f}")
print(f"Desvio padrão......: {desvio_filhos:.2f}")
print(f"Moda...............: {moda_filhos}")
print(f"Máximo.............: {max_filhos}")
print(f"Mínimo.............: {min_filhos}")
print(f"Contagem (clientes): {contagem_filhos}")


# =============================================================================
# 5. PADRÕES DE AGRUPAMENTO (>= 2 AGRUPAMENTOS)
# =============================================================================
titulo("ETAPA 5 - AGRUPAMENTO 1: COMPRAS E ITENS POR GÊNERO")

compras_por_genero = df.groupby("CL_GENERO")["CO_ID"].nunique().sort_values(ascending=False)
itens_por_genero = df.groupby("CL_GENERO").size().sort_values(ascending=False)
print("Compras (notas fiscais) distintas por gênero:")
print(compras_por_genero)
print("\nItens comprados por gênero:")
print(itens_por_genero)
print(f"\nGênero com mais compras: {compras_por_genero.idxmax()}")

titulo("ETAPA 5 - AGRUPAMENTO 2: ITENS VENDIDOS POR CATEGORIA DE PRODUTO")

itens_por_categoria = df.groupby("PR_CAT").size().sort_values(ascending=False)
print(itens_por_categoria)
print(f"\nCategoria mais comprada: {itens_por_categoria.idxmax()}")

titulo("ETAPA 5 - AGRUPAMENTO 3: MÉDIA DE FILHOS POR SEGMENTO ECONÔMICO (pivot_table)")

media_filhos_segmento = pd.pivot_table(
    clientes, values="CL_FHL", index="CL_SEG", aggfunc="mean"
).sort_values("CL_FHL", ascending=False)
print(media_filhos_segmento)

titulo("ETAPA 5 - AGRUPAMENTO 4 (EXTRA): TABELA DINÂMICA CATEGORIA x GÊNERO")

tabela_dinamica = pd.pivot_table(
    df, values="PR_ID", index="PR_CAT", columns="CL_GENERO",
    aggfunc="count", fill_value=0
)
print(tabela_dinamica)


# =============================================================================
# 6. EXPORTAÇÃO DA BASE LIMPA
# =============================================================================
titulo("ETAPA 6 - EXPORTANDO BASE LIMPA (df_limpo.csv)")
df.to_csv("df_limpo.csv", index=False, encoding="utf-8")
print("Arquivo 'df_limpo.csv' gerado com sucesso na pasta do projeto.")


# =============================================================================
# 7. CONCLUSÕES
# =============================================================================
titulo("CONCLUSÕES E PRINCIPAIS INSIGHTS")

conclusoes = [
    f"1. A base final ficou com {df.shape[0]} itens comprados, de "
    f"{df['CO_ID'].nunique()} compras distintas e {clientes.shape[0]} clientes, "
    f"após remover colunas fantasma, duplicatas e datas inválidas.",

    f"2. O número médio de filhos por cliente é {media_filhos:.2f} (mediana "
    f"{mediana_filhos:.2f}, moda {moda_filhos}), variando de {min_filhos:.0f} a "
    f"{max_filhos:.0f} filhos.",

    f"3. O gênero '{compras_por_genero.idxmax()}' concentra o maior número de compras "
    f"({int(compras_por_genero.max())} notas fiscais distintas).",

    f"4. A categoria de produto mais comprada é '{itens_por_categoria.idxmax()}', com "
    f"{int(itens_por_categoria.max())} itens vendidos.",

    f"5. O segmento econômico '{media_filhos_segmento['CL_FHL'].idxmax()}' é o que tem, em "
    f"média, mais filhos por cliente ({media_filhos_segmento['CL_FHL'].max():.2f}), o que "
    "pode ajudar a direcionar campanhas por perfil de família.",

    "6. Como problema remanescente, ~11% das linhas originais eram duplicatas exatas; "
    "como a base não possui uma coluna de quantidade, não é possível garantir que todas "
    "essas linhas fossem erro de digitação e não uma segunda unidade do mesmo produto "
    "comprada na mesma nota — vale confirmar essa regra de negócio com a fonte dos dados.",
]

for c in conclusoes:
    print(c)

print("\nAnálise concluída. Utilize 'df_limpo.csv' para etapas seguintes (dashboards, etc.).")
