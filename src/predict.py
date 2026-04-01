import joblib
import pandas as pd

preprocessador = joblib.load("models/preprocessamento.pkl")
modelo = joblib.load("models/modelo_classificacao.pkl")

colunas = ['Idade', 'Sexo', 'Tipo dor', 'Pressao arterial', 'Colesterol',
       'Glicemia jejum >120', 'Resultados ECG', 'Frequencia cardiaca max',
       'Dor exercicio', 'Depressao ST', 'Inclinacao ST', 'Numero vasos fluro',
       'Teste cintilografia']

def predict(dados):

    df = pd.DataFrame(dados)

    df_tratado = preprocessador.transform(df)
    df_tratado = pd.DataFrame(df_tratado, columns=colunas)

    previsao = modelo.predict(df_tratado)

    return previsao
