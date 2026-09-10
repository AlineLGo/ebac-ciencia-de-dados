import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# PROJETO: ANÁLISE EXPLORATÓRIA E VISUALIZAÇÃO DE DADOS DE E-COMMERCE
# =====================================================================

# 1. Carregamento dos Dados
print("Carregando base de dados...")
df = pd.read_csv('ecommerce_preparados.csv')

# Estilo visual padrão para deixar todos os gráficos mais bonitos
sns.set_theme(style="whitegrid")


# =====================================================================
# 1º GRÁFICO: HISTOGRAMA (Distribuição das Notas)
# =====================================================================
print("Gerando Histograma...")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Nota', bins=30, kde=True, color='purple')
plt.title('Distribuição das Notas dos Produtos no E-commerce', fontsize=14)
plt.xlabel('Nota do Produto', fontsize=12)
plt.ylabel('Quantidade de Produtos (Frequência)', fontsize=12)
plt.show() # Feche a janela do gráfico para o código continuar!


# =====================================================================
# 2º GRÁFICO: DISPERSÃO (Avaliações vs Nota)
# =====================================================================
print("Gerando Gráfico de Dispersão...")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='N_Avaliações', y='Nota', color='blue', alpha=0.5)
plt.title('Relação entre Número de Avaliações e Nota do Produto', fontsize=14)
plt.xlabel('Número de Avaliações (Quantidade)', fontsize=12)
plt.ylabel('Nota do Produto', fontsize=12)
plt.show()


# =====================================================================
# 3º GRÁFICO: MAPA DE CALOR (Correlações Numéricas)
# =====================================================================
print("Gerando Mapa de Calor...")
colunas_numericas = df.select_dtypes(include=['float64', 'int64'])
correlacao = colunas_numericas.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Mapa de Calor: Correlação entre Variáveis Numéricas', fontsize=14)
plt.show()


# =====================================================================
# 4º GRÁFICO: BARRAS (Top 5 Gêneros)
# =====================================================================
print("Gerando Gráfico de Barras...")
top_5_generos = df['Gênero'].value_counts().head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_generos.index, y=top_5_generos.values, color='teal')
plt.title('Top 5 Gêneros com Mais Produtos Disponíveis', fontsize=14)
plt.xlabel('Gênero do Produto', fontsize=12)
plt.ylabel('Quantidade de Produtos Cadastrados', fontsize=12)
plt.show()


# =====================================================================
# 5º GRÁFICO: PIZZA (Top 5 Marcas)
# =====================================================================
print("Gerando Gráfico de Pizza...")
top_5_marcas = df['Marca'].value_counts().head(5)

plt.figure(figsize=(8, 8))
plt.pie(top_5_marcas.values, labels=top_5_marcas.index, autopct='%1.1f%%',
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'], startangle=90)
plt.title('Participação das Top 5 Marcas no E-commerce', fontsize=14)
plt.show()


# =====================================================================
# 6º GRÁFICO: DENSIDADE (Concentração das Notas)
# =====================================================================
print("Gerando Gráfico de Densidade...")
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Nota', fill=True, color='orange')
plt.title('Gráfico de Densidade: Concentração das Notas dos Produtos', fontsize=14)
plt.xlabel('Nota do Produto', fontsize=12)
plt.ylabel('Densidade (Concentração)', fontsize=12)
plt.show()


# =====================================================================
# 7º GRÁFICO: REGRESSÃO (Desconto vs Nota)
# =====================================================================
print("Gerando Gráfico de Regressão...")
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Desconto', y='Nota',
            scatter_kws={'alpha':0.3, 'color':'gray'},
            line_kws={'color':'red', 'linewidth':2})
plt.title('Gráfico de Regressão: Impacto do Desconto na Nota do Produto', fontsize=14)
plt.xlabel('Valor do Desconto (R$)', fontsize=12)
plt.ylabel('Nota do Produto', fontsize=12)
plt.show()

print("Análise concluída com sucesso!")

