import joblib

# carregar modelo treinado
model = joblib.load("models/sales_model.pkl")

# pedir mês ao usuário
month = int(input("Digite o mês para previsão: "))

prediction = model.predict([[month]])

print(f"Previsão de vendas para o mês {month}: {prediction[0]}")