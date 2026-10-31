# AG2 — Classificação de Canais de Vendas

Projeto desenvolvido para a atividade AG2 do Instituto Nacional de Telecomunicações (Inatel), com o objetivo de classificar canais de vendas utilizando técnicas de aprendizado de máquina.

O projeto utiliza o algoritmo de Árvore de Decisão (Decision Tree) para identificar se um cliente pertence ao canal **HoReCa** (hotéis, restaurantes e cafés) ou **Retail** (varejo), considerando seus gastos anuais em diferentes categorias de produtos e sua região.

## 1. Conjunto de dados

Foi utilizado o conjunto de dados **Wholesale Customers**, disponibilizado pelo UCI Machine Learning Repository, contendo 440 registros.

O conjunto possui os seguintes atributos:

- **Region:** região do cliente.
- **Fresh:** gastos anuais com produtos frescos.
- **Milk:** gastos anuais com laticínios.
- **Grocery:** gastos anuais com produtos de mercearia.
- **Frozen:** gastos anuais com produtos congelados.
- **Detergents Paper:** gastos anuais com detergentes e produtos de papel.
- **Delicatessen:** gastos anuais com guloseimas.
- **Channel:** canal de vendas, utilizado como variável-alvo da classificação.

## 2. Preparação dos dados

A preparação dos dados foi implementada no arquivo `src/preparar_dados.py`.

As etapas realizadas são:

1. Leitura do arquivo CSV utilizando a biblioteca Pandas.
2. Padronização dos nomes das colunas.
3. Conversão dos valores de `Channel` e `Region` para números inteiros.
4. Reordenação das colunas conforme o enunciado.
5. Separação dos dados em 80% para treinamento e 20% para teste, utilizando `train_test_split`.
6. Armazenamento dos arquivos processados.

### Conversão dos valores

**Coluna Channel:**
- HoReCa = 0
- Retail = 1

**Coluna Region:**
- Lisbon = 0
- Oporto = 1
- Other = 2

### Ordem das colunas

Após a preparação, as colunas são organizadas nesta ordem:

```text
Region
Fresh
Milk
Grocery
Frozen
Detergents Paper
Delicatessen
Channel
```

### Divisão dos dados

O conjunto original possui 440 registros, divididos da seguinte maneira:

- Treinamento: 352 registros (80%).
- Teste: 88 registros (20%).

Foi utilizado `random_state=42` para permitir a reprodução da divisão e `stratify=y` para preservar a proporção das classes.

## 3. Estrutura dos dados preparados

Os arquivos gerados ficam armazenados em `data/processed/`:

- `dados_preparados.csv`: conjunto completo após o pré-processamento.
- `X_train.csv`: atributos utilizados no treinamento.
- `X_test.csv`: atributos utilizados no teste.
- `y_train.csv`: classes correspondentes aos dados de treinamento.
- `y_test.csv`: classes correspondentes aos dados de teste.

O arquivo `src/carregar_dados.py` realiza a leitura dos conjuntos de treinamento e teste utilizando Pandas e verifica a correspondência entre a quantidade de entradas e seus respectivos rótulos.

## 4. Modelo de classificação

O modelo de aprendizado de máquina foi implementado em `src/classificar.py`.

Foi utilizado o algoritmo **Decision Tree Classifier**, disponível na biblioteca Scikit-learn.

O modelo é criado utilizando:

```python
modelo = DecisionTreeClassifier(random_state=42)
```

O programa realiza as seguintes operações:

1. Carregamento dos dados de treinamento e teste.
2. Criação do classificador.
3. Treinamento utilizando o método `fit()`.
4. Classificação das amostras de teste utilizando `predict()`.
5. Avaliação do desempenho do modelo.
6. Classificação de novos clientes a partir de informações fornecidas pelo usuário.

## 5. Avaliação do modelo

O desempenho do classificador é avaliado utilizando as funções `accuracy_score` e `classification_report`.

As principais métricas apresentadas são:

- **Acurácia (Accuracy):** proporção de previsões corretas.
- **Precisão (Precision):** proporção de previsões positivas que estão corretas.
- **Revocação (Recall):** capacidade de identificar corretamente as amostras de cada classe.
- **F1-score:** média harmônica entre precisão e revocação.

Nos testes realizados, o modelo apresentou uma acurácia de aproximadamente **89,77%**, classificando corretamente 79 das 88 amostras de teste.

## 6. Classificação de novos clientes

Além da classificação do conjunto de teste, o programa permite inserir manualmente os dados de novos clientes.

O usuário deverá informar:

1. Região (0 = Lisbon, 1 = Oporto, 2 = Other).
2. Gasto com produtos frescos.
3. Gasto com laticínios.
4. Gasto com produtos de mercearia.
5. Gasto com produtos congelados.
6. Gasto com detergentes e papel.
7. Gasto com guloseimas.

Após receber os valores, o programa utiliza o modelo treinado para apresentar o canal previsto:

- **HoReCa:** hotéis, restaurantes e cafés.
- **Retail:** varejo.

O sistema verifica se a região informada é válida e impede a utilização de gastos negativos.

Ao final de cada classificação, o usuário pode escolher classificar outro cliente ou encerrar o programa.

## 7. Estrutura do projeto

```text
AG2-Classificacao/
├── data/
│   ├── wholesale_customers.csv
│   └── processed/
│       ├── dados_preparados.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── src/
│   ├── preparar_dados.py
│   ├── carregar_dados.py
│   └── classificar.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

A pasta `.venv` será criada localmente durante a configuração do ambiente e não precisa ser enviada ao repositório.

## 8. Tecnologias utilizadas

- **Python:** linguagem de programação utilizada.
- **Pandas:** leitura, manipulação e preparação dos dados.
- **Scikit-learn:** divisão dos dados, treinamento e avaliação do modelo.
- **Pathlib:** gerenciamento dos caminhos dos arquivos.

## 9. Como executar o projeto

Para executar o projeto, é necessário ter o Python instalado no computador.

Os comandos apresentados a seguir são destinados ao **Windows**, utilizando o PowerShell ou o terminal do Visual Studio Code.

### Passo 1 — Obter o projeto pelo GitHub

O repositório está disponível em:

https://github.com/Raissarodrigues15/AG2-Classificacao

Para clonar o repositório, execute:

```powershell
git clone https://github.com/Raissarodrigues15/AG2-Classificacao.git
```

Depois entre na pasta do projeto:

```powershell
cd AG2-Classificacao
```

**Importante:** se a pasta do projeto já estiver no computador, não é necessário clonar novamente. Basta abrir a pasta `AG2-Classificacao` no VS Code.

Caso o terminal esteja na pasta que contém `AG2-Classificacao`, utilize:

```powershell
cd .\AG2-Classificacao
```

Todos os comandos seguintes devem ser executados dentro da pasta principal `AG2-Classificacao`.

### Passo 2 — Criar o ambiente virtual

Execute:

```powershell
python -m venv .venv
```

Esse comando cria o ambiente virtual Python na pasta `.venv` do projeto.

### Passo 3 — Instalar as dependências

Execute:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Esse comando instala as bibliotecas necessárias utilizando o Python do ambiente virtual.

### Passo 4 — Preparar os dados

Execute:

```powershell
.\.venv\Scripts\python.exe src\preparar_dados.py
```

Esse comando realiza:

- Leitura do conjunto de dados original.
- Conversão dos valores das colunas `Channel` e `Region`.
- Organização das colunas.
- Divisão dos registros em treinamento e teste.
- Armazenamento dos arquivos processados.

Ao final, deverá ser apresentada uma mensagem semelhante a:

```text
Dimensões dos dados: (440, 8)
Valores de Channel: [0, 1]
Valores de Region: [0, 1, 2]
Registros de treinamento: 352
Registros de teste: 88
Preparação concluída!
```

### Passo 5 — Carregar e verificar os dados

Execute:

```powershell
.\.venv\Scripts\python.exe src\carregar_dados.py
```

Esse comando verifica o carregamento dos arquivos preparados.

Resultado esperado:

```text
Dados carregados com sucesso!
Entradas de treinamento: (352, 7)
Entradas de teste: (88, 7)
Rótulos de treinamento: (352,)
Rótulos de teste: (88,)
```

### Passo 6 — Executar o classificador

Execute:

```powershell
.\.venv\Scripts\python.exe src\classificar.py
```

**Este é o comando principal para executar o modelo de aprendizado de máquina.**

O programa realizará:

1. Carregamento dos conjuntos de treinamento e teste.
2. Treinamento do modelo Decision Tree.
3. Previsão das classes das amostras de teste.
4. Exibição da acurácia e do relatório de classificação.
5. Solicitação dos dados de um novo cliente.
6. Exibição do canal de vendas previsto.

### Exemplo de utilização

O programa solicita os seguintes dados:

```text
=== CLASSIFICAR NOVO CLIENTE ===
Regioes: 0 = Lisbon, 1 = Oporto, 2 = Other

Digite a regiao (0, 1 ou 2): 0
Gasto com produtos frescos: 12000
Gasto com laticinios: 6000
Gasto com mercearia: 9000
Gasto com congelados: 2000
Gasto com detergentes e papel: 5000
Gasto com guloseimas: 1500
```

Após a inserção dos valores, o modelo apresentará o canal de vendas previsto para o cliente: **HoReCa** ou **Retail**.

Para encerrar, basta digitar `n` quando o programa perguntar se deseja classificar outro cliente.


## 11. Referência

Cardoso, Margarida. *Wholesale Customers*. UCI Machine Learning Repository, 2014.

https://doi.org/10.24432/C5030X