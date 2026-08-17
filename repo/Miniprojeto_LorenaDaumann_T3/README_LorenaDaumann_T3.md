# Mini-Projeto Avaliativo — Módulo 1 — Semana 07

**Disciplina:** Visualização de Dados e Business Intelligence [T3]
**Aluna:** Lorena Daumann
**Turma:** T3

## Objetivo

Realizar uma Análise Exploratória de Dados (AED) sobre a base pública **Varejo**
(Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data), cobrindo
verificação de qualidade, limpeza, estatísticas descritivas e agrupamentos, a
fim de responder perguntas operacionais sobre o comportamento de compra dos
clientes.

## Como executar

1. Baixe a base `Varejo.csv` no link do Kaggle acima e coloque o arquivo na
   mesma pasta deste script (`Miniprojeto_LorenaDaumann_T3.py`).
2. **VSCode:** instale as extensões *Python* e *Jupyter* e rode:
   ```
   python Miniprojeto_LorenaDaumann_T3.py
   ```
3. **Google Colab:** faça upload do script (ou copie o conteúdo em células)
   e do `Varejo.csv`, depois execute todas as células.
4. Ao final da execução, o arquivo `df_limpo.csv` (base tratada) é gerado
   automaticamente na mesma pasta.

> Observação: o script identifica automaticamente os nomes das colunas
> (data, gênero, número de filhos, categoria, valor etc.) mesmo que variem
> um pouco de grafia. Caso alguma coluna apareça como "NÃO ENCONTRADA" no
> início da execução, ajuste a lista de nomes candidatos na seção
> `CONFIGURAÇÃO DE COLUNAS`, no topo do script.

## Etapas de desenvolvimento

1. **Carregamento da base** — leitura do `Varejo.csv` com `pandas`, exibindo
   número de registros, colunas e tipos de dados.
2. **Diagnóstico de problemas** — verificação de valores nulos por coluna,
   linhas duplicadas, categorias vazias e datas em formato inválido.
3. **Limpeza dos dados**:
   - Categorias vazias/nulas foram preenchidas com `"Sem Categoria"` por meio
     de uma regra condicional (if/else), em vez de descartar a linha —
     assim preservamos os dados de venda, cliente e valor daquele registro.
   - Valores nulos em colunas numéricas (incluindo número de filhos do
     cliente) foram imputados pela **mediana** da própria coluna. A mediana
     foi escolhida em vez da média por ser mais robusta a valores extremos
     (outliers), evitando distorcer a estatística com poucos casos fora do
     padrão.
   - Linhas sem identificação de cliente/compra foram removidas, pois não é
     possível rastreá-las de forma confiável.
   - Linhas duplicadas foram eliminadas com `drop_duplicates()`.
   - A coluna de data foi convertida para `datetime` com `pd.to_datetime()`;
     registros com data em formato inválido (não convertível) foram
     removidos.
4. **Estatísticas descritivas** da coluna "Número de filhos do cliente":
   média, mediana, desvio padrão, moda, máximo, mínimo e contagem.
5. **Agrupamentos** (via `groupby()` e `pivot_table()`):
   - Total de vendas por gênero.
   - Total de vendas e quantidade de compras por categoria.
   - Tabela dinâmica cruzando categoria x gênero.
6. **Exportação** da base tratada (`df_limpo.csv`) e geração das conclusões.

## Reflexão teórica: ETL e qualidade de dados

O processo realizado neste mini-projeto segue a lógica de um pipeline **ETL**
(*Extract, Transform, Load*): primeiro os dados brutos foram **extraídos**
do arquivo `Varejo.csv`; em seguida passaram por uma etapa de
**transformação**, na qual problemas de qualidade — nulos, duplicatas,
categorias vazias e tipos de dados incorretos — foram identificados e
corrigidos; por fim, o resultado foi **carregado** em um novo arquivo
(`df_limpo.csv`), pronto para alimentar análises mais avançadas ou um
dashboard de BI.

A qualidade dos dados é o que sustenta a confiabilidade de qualquer análise
ou indicador construído a partir deles: uma base com nulos não tratados pode
subestimar métricas, duplicatas podem inflar contagens e vendas, e colunas
com tipo incorreto (por exemplo, datas como texto) impedem análises
temporais corretas. Por isso, cada decisão de limpeza foi documentada com a
justificativa correspondente diretamente nos comentários do script — é
importante que o tratamento de dados seja *reproduzível* e *auditável*, e
não apenas "correto" no resultado final.

## Principais insights obtidos

> Preencha os itens abaixo com os valores exibidos na seção **CONCLUSÕES**
> impressa no terminal após rodar o script com a base `Varejo.csv` real.

1. A base final ficou com `<PREENCHER>` registros após a limpeza (remoção de
   duplicatas, linhas sem identificação e datas inválidas).
2. O número médio de filhos por cliente é `<PREENCHER>`, com mediana
   `<PREENCHER>` e moda `<PREENCHER>`.
3. O gênero com maior volume de vendas foi `<PREENCHER>`, totalizando
   `<PREENCHER>` em valor de compras.
4. A categoria de maior faturamento foi `<PREENCHER>`.
5. Havia registros sem categoria informada, tratados como "Sem Categoria"
   em vez de descartados.
6. Como problema remanescente, recomenda-se validar a origem dos valores
   nulos da base original (erro de coleta vs. ausência real de informação)
   antes de usá-la para decisões de negócio mais sensíveis.

## Estrutura de arquivos

```
Miniprojeto_LorenaDaumann_T3/
├── Miniprojeto_LorenaDaumann_T3.py   # script da análise
├── README_LorenaDaumann_T3.md        # este arquivo
├── Varejo.csv                        # base de dados original (adicionar manualmente)
└── df_limpo.csv                      # gerado automaticamente ao rodar o script
```
