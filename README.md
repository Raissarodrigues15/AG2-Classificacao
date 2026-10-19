# AG2 — Classificação de Canais de Vendas

Projeto desenvolvido para a atividade AG2 do Inatel, com o objetivo de classificar canais de vendas utilizando aprendizado de máquina.

## Conjunto de dados

Foi utilizado o conjunto Wholesale Customers, disponibilizado pelo UCI Machine Learning Repository, com 440 registros.

## Preparação dos dados

A etapa de preparação foi implementada em `src/preparar_dados.py` e inclui:

- Leitura do arquivo CSV com Pandas.
- Conversão dos valores de `Channel` e `Region` para números inteiros.
- Reordenação das colunas conforme o enunciado.
- Divisão dos dados em 80% para treinamento e 20% para teste, utilizando `train_test_split`.

## Estrutura dos dados preparados

Os arquivos gerados ficam em `data/processed/`:

- `dados_preparados.csv`
- `X_train.csv`
- `X_test.csv`
- `y_train.csv`
- `y_test.csv`

## Como executar

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute a preparação:

```bash
python src/preparar_dados.py
```

## Integrantes

- Pessoa 1: obtenção e preparação dos dados.
- Pessoa 2: desenvolvimento e avaliação do modelo de classificação.