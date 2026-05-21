<!-- 
Seja bem-vindo(a)!

Este projeto corresponde ao desafio extra do curso Introdução ao Data Science (SCTEC). O objetivo principal foi realizar uma Análise Exploratória de Dados (AED) utilizando a base pública do Titanic, disponível em formato CSV. Abaixo estarão descritos passo a passo da formação do arquivo, para a documentação de tudo o que foi feito e melhor compreensão do usuário.

🔗 Dataset utilizado:
https://drive.google.com/file/d/11HptTxJbUMRG16xpC39fcliba_-Z_J9d/


OBJETIVO DA ANÁLISE
O propósito desta atividade foi importar, organizar e analisar os dados, buscando compreender padrões, relações entre variáveis e fatores que possam ter influenciado a sobrevivência dos passageiros.

ETAPAS DO DESENVOLVIMENTO
#1. Importação de bibliotecas
Foram utilizadas as bibliotecas:

pandas: manipulação e análise de dados
matplotlib.pyplot: visualização gráfica


#2. Carregamento dos dados
O dataset foi carregado.

#3. Exploração inicial dos dados

Foram utilizados os seguintes métodos:

df.head() → visualizar primeiras linhas
df.info() → tipos de dados e valores nulos
df.describe() → estatísticas descritivas

Também foi utilizada a função:

df.isnull().sum()

para identificar valores ausentes no dataset.


#4. Tratamento e organização dos dados
Nesta etapa foram realizadas:
-verificação de valores nulos;
-remoção de duplicatas;
-conversão de datas;
-criação de colunas auxiliares;
-preparação das variáveis para análise.

#5. Análise Exploratória de Dados (AED)
Foram realizadas diversas análises utilizando funções como groupby(), sum(), mean(), count() e value_counts(). As principais análises realizadas foram:
- padrões de vendas;
- desempenho financeiro;
- comportamento dos clientes;
- impacto dos descontos na lucratividade;
- distribuição de produtos vendidos;
- eficiência logística e de entregas.

Foram utilizados dois tipos principais de análise:

.size() → para contagem de indivíduos
.mean() → para cálculo de taxa de sobrevivência

Foram tambem geradas visualizações gráficas utilizando matplotlib, permitindo uma melhor interpretação dos dados e identificação de padrões.

A partir desse processo, foram gerados insights relevantes para auxiliar na interpretação do desempenho comercial da empresa.


#"Ins0ights obtidos

A partir das análises, foi possível identificar padrões importantes, como:

determinados anos apresentaram crescimento significativo nas vendas;
algumas categorias concentram grande parte do faturamento da empresa;
certos segmentos de clientes realizam mais pedidos que outros;
determinadas subcategorias possuem alta quantidade de vendas, mas baixa lucratividade;
descontos excessivos podem reduzir significativamente o lucro líquido;
alguns métodos de entrega são muito mais utilizados que outros;
certas regiões possuem maior concentração de clientes e pedidos.

CONCLUSÃO
A análise exploratória permitiu identificar padrões relevantes nos dados de vendas,.
Este projeto reforça a importância da organizacao, limpeza e exploração dos dados como etapas fundamentais no processo de Data Science.


ESTRUTURA DO PROJETO
O projeto inclui:

código-fonte em Python;
base de dados utilizada;
documentação (README);
gráficos gerados;
análises e insights;
integração com GitHub.
  -->
