# Sales Forecast with Machine Learning

Projeto de previsão de vendas utilizando Python e Machine Learning.

## Tecnologias utilizadas

- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Joblib

## Estrutura do projeto

sales-forecast-ml
│
├── data
│   └── sales.csv
│
├── models
│   └── sales_model.pkl
│
├── src
│   └── train_model.py
│
├── requirements.txt
└── README.md

## Como executar o projeto

1. Clone o repositório

git clone https://github.com/mrlmarkus/python-ml-sales-forecast.git

2. Instale as dependências

pip install -r requirements.txt

3. Execute o modelo

python src/train_model.py

## Resultado

O modelo treina uma regressão linear para prever vendas futuras com base nos meses anteriores.