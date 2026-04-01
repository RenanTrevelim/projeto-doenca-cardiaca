import streamlit as st
from src.predict import predict
import pandas as pd

st.set_page_config(
    page_title="Classificador de Doença Cardíaca",
    layout="centered"
)

st.title("Classificador de Doença Cardíaca")
st.write("Faça o upload do arquivo CSV com os dados para a classificação")

arquivo = st.file_uploader("Coloque o arquivo CSV aqui", type=["csv"])

if arquivo:
    try:
        df = pd.read_csv(arquivo)

        st.subheader("📄 Dados carregados:")
        st.dataframe(df)

        if st.button("Prever"):

            previsoes = predict(df)
            df['classificador'] = previsoes

            map = {
                1:"Presença",
                0:"Ausência"
            }
            df["classificador"] = df['classificador'].map(map)

            st.subheader("📊 Resultado do Classificador:")
            st.dataframe(df)

            # Botão para download
            csv_resultado = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Baixar resultados",
                data=csv_resultado,
                file_name="doenca_cardiaca_resultados.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")