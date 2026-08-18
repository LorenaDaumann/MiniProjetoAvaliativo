# MiniProjeto Avaliativo 1 - Lorena Daumann (T3)

Resumo do trabalho realizado no Módulo 1 (Semana 07) — Visualização de Dados e
Business Intelligence (T3).

- **Aluna:** Lorena Daumann
- **Turma:** T3
- **Arquivo principal:** Miniprojeto_LorenaDaumann_T3/Miniprojeto_LorenaDaumann_T3.py
- **Dados originais:** BaseVarejo.csv
- **Arquivo gerado (limpo):** df_limpo.csv

Descrição:

O projeto realiza uma Análise Exploratória de Dados (AED) sobre um recorte de
compras de clientes de uma rede de supermercados. O script carrega a base,
identifica problemas de qualidade (colunas fantasma, duplicatas, categorias
marcadas como `#N/D`, datas inválidas), faz limpeza (remoção de colunas
fantasma, substituição de categorias inválidas, remoção de duplicatas, conversão
de datas) e gera estatísticas descritivas e agregadas por gênero, categoria e
segmento econômico.

Como executar:

1. Coloque `BaseVarejo.csv` na mesma pasta do script ou em uma subpasta do
   projeto.
2. Execute:

```bash
python3 Miniprojeto_LorenaDaumann_T3/Miniprojeto_LorenaDaumann_T3.py
```

Saída esperada:

- Um arquivo `df_limpo.csv` com os registros limpos e tratados.
- Impressão no terminal com os resumo da limpeza e principais insights.

Observações e limitações:

- A base original não possui coluna de quantidade por item; linhas idênticas
  podem representar duplicação de registro ou múltiplas unidades compradas. O
  script opta por remover duplicatas exatas.
- Confirme regras de negócio com a equipe de dados antes de usar `df_limpo.csv`
  para análises que dependam da quantidade adquirida por item.

Licença: uso acadêmico / educativo.
