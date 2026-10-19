
import pandas as pd
from pathlib import Path


def carregar_dados():
    # Localizar a pasta dos arquivos preparados
    pasta = Path("data/processed")

    # Carregar os dados de treinamento e teste
    X_train = pd.read_csv(pasta / "X_train.csv")
    X_test = pd.read_csv(pasta / "X_test.csv")
    y_train = pd.read_csv(pasta / "y_train.csv").squeeze("columns")
    y_test = pd.read_csv(pasta / "y_test.csv").squeeze("columns")

    # Conferir se os arquivos possuem os dados esperados
    assert len(X_train) == len(y_train), "Treino com quantidades diferentes"
    assert len(X_test) == len(y_test), "Teste com quantidades diferentes"

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = carregar_dados()

    print("Dados carregados com sucesso!")
    print("Entradas de treinamento:", X_train.shape)
    print("Entradas de teste:", X_test.shape)
    print("Rótulos de treinamento:", y_train.shape)
    print("Rótulos de teste:", y_test.shape)
