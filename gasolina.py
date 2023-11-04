import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('gasolina.csv')

# Crie um DataFrame com os dados
df = pd.DataFrame(data)

# Crie o gráfico de linhas
plt.plot(data['dia'], data['venda'])

# Adicione rótulos aos eixos
plt.xlabel('Dia')
plt.ylabel('Preço')

# Adicione um título ao gráfico
plt.title('Preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021')

plt.savefig('preco_medio_de_venda_da_gasolina_na_cidade_de_Sao_Paulo_nos_10_primeiros_dias_de_Julho_de_2021.png')

# Exiba o gráfico
plt.show()
