
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

# Ler o arquivo CSV
dados = pd.read_csv("data/wholesale_customers.csv")

# Padronizar os nomes das colunas
dados = dados.rename(columns={
    "Detergents_Paper": "Detergents Paper",
    "Delicassen": "Delicatessen"
})

# Converter Channel para 0 = HoReCa e 1 = Retail
if dados["Channel"].dtype == "object":
    dados["Channel"] = dados["Channel"].replace({
        "HoReCa": 0,
        "Retail": 1
    })
else:
    dados["Channel"] = dados["Channel"].replace({
        1: 0,
        2: 1
    })

# Converter Region para 0 = Lisbon, 1 = Oporto e 2 = Other
if dados["Region"].dtype == "object":
    dados["Region"] = dados["Region"].replace({
        "Lisbon": 0,
        "Oporto": 1,
        "Other": 2
    })
else:
    dados["Region"] = dados["Region"].replace({
        1: 0,
        2: 1,
        3: 2
    })

# Garantir que as categorias sejam números inteiros
dados["Channel"] = dados["Channel"].astype(int)
dados["Region"] = dados["Region"].astype(int)

# Organizar as colunas na ordem exigida
ordem = [
    "Region",
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents Paper",
    "Delicatessen",
    "Channel"
]

dados = dados[ordem]

# Separar entradas e variável-alvo
X = dados.drop(columns=["Channel"])
y = dados["Channel"]

# Dividir em 80% para treino e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Criar pasta para salvar os resultados
pasta = Path("data/processed")
pasta.mkdir(parents=True, exist_ok=True)

# Salvar os dados preparados
dados.to_csv(pasta / "dados_preparados.csv", index=False)
X_train.to_csv(pasta / "X_train.csv", index=False)
X_test.to_csv(pasta / "X_test.csv", index=False)
y_train.to_frame().to_csv(pasta / "y_train.csv", index=False)
y_test.to_frame().to_csv(pasta / "y_test.csv", index=False)

# Exibir resultados para conferência
print("Dimensões dos dados:", dados.shape)
print("Valores de Channel:", sorted(dados["Channel"].unique()))
print("Valores de Region:", sorted(dados["Region"].unique()))
print("Colunas:", dados.columns.tolist())
print("Registros de treinamento:", len(X_train))
print("Registros de teste:", len(X_test))
print("Preparação concluída!")
