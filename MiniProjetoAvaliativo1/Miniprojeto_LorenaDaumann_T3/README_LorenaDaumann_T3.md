# Mini-Projeto Avaliativo — Módulo 1 — Semana 07

**Disciplina:** Visualização de Dados e Business Intelligence [T3]
**Aluna:** Lorena Daumann
**Turma:** T3

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) sobre a base **Varejo**, um
recorte de compras de clientes de uma rede de supermercados, cobrindo
verificação de qualidade, limpeza, estatísticas descritivas e agrupamentos,
a fim de responder perguntas operacionais sobre o comportamento de compra
dos clientes.

## Sobre a base de dados

Cada linha da base `BaseVarejo.csv` representa **um item comprado dentro de
uma compra** (não uma compra inteira). As colunas são:

| Coluna | Descrição |
| `DATA` | Data da compra |
| `CO_ID` | Identificação da compra (nota fiscal) |
| `CL_ID` | Identificação do cliente |
| `CL_GENERO` | Sexo biológico informado pelo cliente (M/F) |
| `CL_EC` | Estado civil (1=Casado/União estável, 2=Divorciado, 3=Separado, 4=Solteiro, 5=Viúvo) |
| `CL_FHL` | Número de filhos do cliente |
| `CL_SEG` | Segmentação econômica do cliente (A, B ou C) |
| `PR_ID` | Código do produto (SKU) |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

## Como executar

1. Baixe a `BaseVarejo.csv` e coloque na mesma pasta deste script
   (`Miniprojeto_LorenaDaumann_T3.py`).
2. **VSCode:** instale as extensões *Python* e *Jupyter* e rode:
   ```
   python Miniprojeto_LorenaDaumann_T3.py
   ```
3. **Google Colab:** faça upload do script (ou copie o conteúdo em células)
   e da `BaseVarejo.csv`, depois execute todas as células.
4. Ao final da execução, o arquivo `df_limpo.csv` (base tratada) é gerado
   automaticamente na mesma pasta.

## Etapas de desenvolvimento

1. **Carregamento da base** — leitura da `BaseVarejo.csv` com `pandas`
   (separador `;`), exibindo número de registros, colunas e tipos de dados.
2. **Diagnóstico de problemas**:
   - 4 colunas totalmente vazias e sem nome (`Unnamed: 10` a `13`), artefato
     de `;;;;` sobrando no cabeçalho do arquivo original.
   - 96.553 linhas totalmente duplicadas.
   - 3.650 registros com a categoria do produto marcada como `"#N/D"`
     (ausência de informação) em vez de nula de fato.
   - Validação da coluna `CO_ID`: nenhuma compra apareceu associada a mais
     de um cliente, ou seja, o identificador de compra é consistente.
   - Nenhuma data em formato inválido após a conversão para `datetime`.
3. **Limpeza dos dados**:
   - As 4 colunas fantasma foram **removidas** (não imputadas), pois não
     carregam nenhuma informação — são apenas artefato do arquivo original.
   - Categorias marcadas como `"#N/D"` foram preenchidas com
     `"Sem Categoria"` através de uma regra condicional (if/else), em vez de
     descartar a linha — preservando o registro de compra, cliente e
     produto associados.
   - Linhas totalmente duplicadas foram removidas com `drop_duplicates()`.
     Como a base não tem uma coluna de quantidade, optamos por tratar linha
     idêntica repetida como erro de duplicação no arquivo (e não como
     "comprou 2 unidades do mesmo item") — essa é uma decisão documentada
     como problema remanescente nas conclusões.
   - A coluna `DATA` foi convertida para `datetime` com `pd.to_datetime()`.
4. **Estatísticas descritivas** da coluna `CL_FHL` (número de filhos do
   cliente): média, mediana, desvio padrão, moda, máximo, mínimo e
   contagem — calculadas **a nível de cliente** (1.000 clientes únicos),
   e não a nível de linha/item, já que `CL_FHL` é um atributo do cliente
   repetido em todas as suas compras; calcular direto sobre as ~800 mil
   linhas daria peso indevido aos clientes que compraram mais vezes.
5. **Agrupamentos** (via `groupby()` e `pivot_table()`):
   - Quantidade de compras e de itens por gênero.
   - Quantidade de itens vendidos por categoria de produto.
   - Média de número de filhos por segmento econômico (A/B/C).
   - Tabela dinâmica cruzando categoria de produto x gênero.
6. **Exportação** da base tratada (`df_limpo.csv`) e geração das conclusões.

## Reflexão teórica: ETL e qualidade de dados

O processo realizado neste mini-projeto segue a lógica de um pipeline
**ETL** (*Extract, Transform, Load*): os dados brutos foram **extraídos**
do arquivo `BaseVarejo.csv`; em seguida passaram por uma etapa de
**transformação**, na qual problemas de qualidade — colunas vazias sem
utilidade, duplicatas, marcadores de ausência disfarçados (`"#N/D"`) e tipo
de dado incorreto na coluna de data — foram identificados e corrigidos; por
fim, o resultado foi **carregado** em um novo arquivo (`df_limpo.csv`),
pronto para alimentar análises mais avançadas ou um dashboard de BI.

Esse projeto deixou claro que "dado ausente" nem sempre aparece como um
`NaN` explícito: aqui ele apareceu como colunas fantasma 100% vazias e como
um marcador de texto (`"#N/D"`) dentro de uma coluna categórica. Identificar
esse tipo de problema exige olhar além do `isnull().sum()` — é preciso
inspecionar os valores únicos de cada coluna. Da mesma forma, decidir como
tratar as duplicatas exigiu entender a granularidade da base (1 linha = 1
item, sem coluna de quantidade), o que reforça que qualidade de dados não é
só "rodar uma função de limpeza", mas entender o contexto de negócio por
trás de cada coluna antes de decidir remover ou transformar algo.

## Principais insights obtidos

1. A base final ficou com 733.447 itens comprados, de 18.471 compras
   distintas e 1.000 clientes, após remover colunas fantasma, duplicatas e
   validar as datas.
2. O número médio de filhos por cliente é 1,14 (mediana 0, moda 0),
   variando de 0 a 4 filhos — a maior parte dos clientes não tem filhos,
   mas uma parcela relevante puxa a média para cima.
3. O gênero feminino concentra o maior número de compras (9.615 notas
   fiscais distintas, contra 8.856 do masculino).
4. A categoria de produto mais comprada é "Alimentos", com 384.197 itens
   vendidos — bem à frente de Higiene e Limpeza, as próximas colocadas.
5. O segmento econômico C é o que tem, em média, mais filhos por cliente
   (1,19), o que pode ajudar a direcionar campanhas por perfil de família.
6. Como problema remanescente, ~11% das linhas originais eram duplicatas
   exatas; como a base não possui uma coluna de quantidade, não é possível
   garantir que todas essas linhas fossem erro de digitação e não uma
   segunda unidade do mesmo produto comprada na mesma nota — vale confirmar
   essa regra de negócio com a fonte dos dados.

## Estrutura de arquivos

```
Miniprojeto_LorenaDaumann_T3/
├── Miniprojeto_LorenaDaumann_T3.py   # script da análise
├── README_LorenaDaumann_T3.md        # este arquivo
├── BaseVarejo.csv                    # base de dados original (adicionar manualmente)
└── df_limpo.csv                      # gerado automaticamente ao rodar o script
```