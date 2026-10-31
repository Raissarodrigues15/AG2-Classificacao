

from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Localizar os arquivos de treinamento e teste
pasta = Path(__file__).resolve().parent.parent / "data" / "processed"

# Carregar os dados
X_train = pd.read_csv(pasta / "X_train.csv")
X_test = pd.read_csv(pasta / "X_test.csv")
y_train = pd.read_csv(pasta / "y_train.csv").squeeze("columns")
y_test = pd.read_csv(pasta / "y_test.csv").squeeze("columns")

# Criar e treinar o modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Testar o modelo
previsoes = modelo.predict(X_test)

# Mostrar os resultados
print("=== RESULTADOS DA CLASSIFICACAO ===")
print(f"Acuracia: {accuracy_score(y_test, previsoes) * 100:.2f}%")

print("\nRelatorio de classificacao:")
print(classification_report(y_test, previsoes))
print(classification_report(y_test, previsoes))

# Classificar novos clientes
while True:
    print("\n=== CLASSIFICAR NOVO CLIENTE ===")
    print("Regioes: 0 = Lisbon, 1 = Oporto, 2 = Other")

    try:
        regiao = int(input("Digite a regiao (0, 1 ou 2): "))
        if regiao not in (0, 1, 2):
            print("Regiao invalida!")
            continue

        fresh = float(input("Gasto com produtos frescos: "))
        milk = float(input("Gasto com laticinios: "))
        grocery = float(input("Gasto com mercearia: "))
        frozen = float(input("Gasto com congelados: "))
        detergents = float(input("Gasto com detergentes e papel: "))
        delicatessen = float(input("Gasto com guloseimas: "))

        valores = [
            regiao, fresh, milk, grocery, frozen,
            detergents, delicatessen
        ]

        if any(valor < 0 for valor in valores):
            print("Os gastos nao podem ser negativos.")
            continue

        novo_cliente = pd.DataFrame(
            [valores],
            columns=X_train.columns
        )

        resultado = modelo.predict(novo_cliente)[0]

        if resultado == 0:
            print("\nCanal previsto: HoReCa")
        else:
            print("\nCanal previsto: Retail")

    except ValueError:
        print("Digite apenas numeros validos!")
        continue

    continuar = input(
        "\nDeseja classificar outro cliente? (s/n): "
    ).strip().lower()

    if continuar != "s":
        print("\nPrograma encerrado!")
        break
