<!-- 
Seja bem-vindo(a)!

Este projeto corresponde ao desafio extra do curso Introdução ao Data Science (SCTEC). O objetivo principal foi realizar uma Análise Exploratória de Dados (AED) utilizando a base pública do Titanic, disponível em formato CSV. Abaixo estarão descritos passo a passo da formação do arquivo, para a documentação de tudo o que foi feito e melhor compreensão do usuário.

🔗 Dataset utilizado:
https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download 


OBJETIVO DA ANÁLISE
O propósito desta atividade foi importar, organizar e analisar os dados, buscando compreender padrões, relações entre variáveis e fatores que possam ter influenciado a sobrevivência dos passageiros.

ETAPAS DO DESENVOLVIMENTO
#1. Importação de bibliotecas
Foram utilizadas as bibliotecas:

pandas: manipulação e análise de dados
matplotlib.pyplot: visualização gráfica


#2. Carregamento dos dados
O dataset foi carregado com:

df = pd.read_csv("titanic_dataset.csv")

#3. Exploração inicial dos dados

Foram utilizados os seguintes métodos:

df.head() → visualizar primeiras linhas
df.info() → tipos de dados e valores nulos
df.describe() → estatísticas descritivas

Também foi utilizada a função:

df.isnull().sum()

para identificar valores ausentes no dataset.






#4. Tratamento e organização dos dados
Nesta etapa, foi realizada a verificação de valores nulos e a preparação das variáveis para análise.

Foi criada uma nova coluna chamada AgeGroup com o seguinte código:

df['AgeGroup'] = pd.cut(df['Age'], bins=[0,12,18,35,60,100])

Essa linha utiliza a função pd.cut() para transformar a variável contínua idade em faixas etárias, facilitando a análise. Os intervalos definidos representam grupos como crianças, adolescentes, adultos e idosos.

Também foi criada a coluna:

df['HasCabin'] = df['Cabin'].notnull()

Essa variável indica se o passageiro possuía cabine ou não, permitindo análises relacionadas à condição socioeconômica.


#5. Análise Exploratória de Dados (AED)
Foram realizadas diversas análises com o uso de groupby, incluindo:
*Quantidade de sobreviventes e não sobreviventes
*Sobrevivência por classe (Pclass)
*Sobrevivência por sexo (Sex)
*Taxa média de sobrevivência por faixa etária (AgeGroup)
*Relação entre possuir cabine e sobrevivência

Foram utilizados dois tipos principais de análise:

.size() → para contagem de indivíduos
.mean() → para cálculo de taxa de sobrevivência


#6. Insights obtidos
A partir das análises, foi possível observar padrões importantes, como:

*Diferença na taxa de sobrevivência entre gêneros
*Influência da classe social na sobrevivência
*Impacto da idade nas chances de sobrevivência
*Possível relação entre possuir cabine e maior chance de sobreviver

Foram tambem geradas visualizações gráficas utilizando matplotlib, permitindo uma melhor interpretação dos dados e identificação de padrões de sobrevivência.

CONCLUSÃO
A análise exploratória permitiu identificar padrões relevantes nos dados do Titanic, demonstrando como fatores sociais e demográficos influenciaram as chances de sobrevivência. 
Este projeto reforça a importância da organizacao, limpeza e exploração dos dados como etapas fundamentais no processo de Data Science.


ESTRUTURA DO PROJETO
O projeto inclui:

Código-fonte em Python
Base de dados utilizada
Documentação (este arquivo README)
Resultados e análises realizadas
-->