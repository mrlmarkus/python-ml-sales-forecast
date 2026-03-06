import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import joblib

# carregar dados
data = pd.read_csv('data/sales.csv')

# separar variáveis
X = data[['month']]
y = data['sales']

# treinar modelo
model = LinearRegression()
model.fit(X, y)

# prever mês futuro
future_month = [[13]]
prediction = model.predict(future_month)

print(f"Previsão de vendas para o mês 13: {prediction[0]}")

# salvar modelo treinado
joblib.dump(model, "models/sales_model.pkl")
print("Modelo salvo com sucesso!")

# gerar gráfico
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.title("Previsão de Vendas com Machine Learning")
plt.show()