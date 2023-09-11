import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#escrevendo o arquivo csv
fields = ['Dia', 'Venda']

rows = [ ['1', '5.11'],
         ['2', '4.99'],
         ['3', '5.02'],
         ['4', '5.21'],
         ['5', '5.07'],
         ['6', '5.09'],
         ['7', '5.13'],
         ['8', '5.12'],
         ['9', '4.94'],
         ['10', '5.03'] ]

filename = 'gasolina.csv'

with open(filename, 'w') as file:
  writer = csv.writer(file)
  writer.writerow(fields)
  writer.writerows(rows)

  #criando o dataframe
df = pd.read_csv('gasolina.csv')
print(df.head())
print(df.info())

# visuzalização
plt.figure(figsize=(8,5))
sns.set_theme(style="darkgrid")
grap = sns.lineplot(data=df, x='dia', y='venda', color='r')
plt.title('Preço da gasolina em jul-21')
plt.show()

