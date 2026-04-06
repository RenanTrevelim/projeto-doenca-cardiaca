# ❤️ Classificador de Doença Cardíaca

Projeto de Ciência de Dados e Machine Learning para predição da presença de doença cardíaca com base em dados clínicos.

O projeto abrange desde a análise exploratória dos dados (EDA), treinamento de modelos de machine learning, até a construção de uma aplicação interativa utilizando Streamlit.

---

## 📊 Objetivo

O objetivo deste projeto é desenvolver um modelo capaz de identificar a presença de doença cardíaca a partir de variáveis clínicas, auxiliando na tomada de decisão e priorização de casos.

---

## 🧠 Etapas do Projeto

### 🔎 1. Análise Exploratória (EDA)
- Entendimento da distribuição dos dados  
- Identificação de padrões e correlações  
- Análise de variáveis críticas para a doença  
- Verificação de dados nulos e inconsistências  

📄 Arquivo: `EDA_Classificação_Doença_Cardíaca.ipynb`

---

### 🤖 2. Modelagem de Machine Learning
- Treinamento de modelos de classificação  
- Otimização com GridSearchCV  
- Ajuste de threshold  
- Avaliação com:
  - Precision
  - Recall
  - F1-score
  - Matriz de confusão
  - Curva ROC (AUC)

📄 Arquivo: `ML_Classificação_Doença_Cardíaca.ipynb`

---

### 📈 3. Resultados do Modelo
O modelo final apresentou:

- Accuracy: ~0.83  
- Recall (classe positiva): ~0.83  
- Precision: ~0.80  
- F1-score: ~0.82  
- AUC: ~0.83  

✔ Bom equilíbrio entre detecção de casos positivos e controle de falsos positivos  

---

### 🌐 4. Aplicação com Streamlit

Foi desenvolvida uma aplicação interativa para realizar previsões a partir de arquivos CSV.

#### Funcionalidades:
- Upload de arquivo CSV  
- Visualização dos dados  
- Geração de previsões  
- Download dos resultados  

---


## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
code .
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# Linux / Mac
source venv/bin/activate  

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Streamlit

```bash
pip streamlit run main.py
```
