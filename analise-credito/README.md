# 📊 Projeto de Análise e Prevenção de Risco de Crédito

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn)

---

## 🏢 O Problema de Negócio (Empresa Fictícia)

A **Fintech / Instituição Financeira Fictícia** vinha enfrentando dificuldades na concessão de crédito para novos clientes. O processo de avaliação de perfil dependia de análises manuais e inconsistentes, resultando em dois grandes problemas de negócio:

1. **Inadimplência Elevada:** Aprovação de crédito para perfis de alto risco (*Score Low*) que não possuíam capacidade financeira de honrar os pagamentos.
2. **Perda de Oportunidades:** Rejeição ou demora na aprovação de bons clientes (*Score High*), gerando insatisfação e migração para concorrentes.

**Objetivo Central:** Construir um pipeline de Análise Exploratória de Dados (EDA) e pré-processamento estruturado para identificar os padrões comportamentais e demográficos que determinam o risco de crédito, preparando a base para modelos preditivos sem viés.

---

## 💡 A Solução Encontrada

Para resolver esse desafio, desenvolvemos um projeto robusto dividido em 3 etapas estratégicas de Ciência de Dados:

### 1. Limpeza e Padronização de Dados
* **Tratamento de Tipos e Moedas:** Conversão da variável `Income` para tipo numérico (*float*).
* **Imputação Inteligente:** Tratamento de valores ausentes na variável `Age` utilizando a **mediana** (36 anos) para conter o impacto de *outliers*.
* **Verificação de Consistência:** Higienização de variáveis categóricas sem perda de registros.

### 2. Análise Exploratória & Diagnóstico de Negócio (EDA)
Análise profunda das variáveis demográficas e financeiras cruzadas com a classificação de crédito:
* **Fatores Determinantes de Crédito Alto (*High*):** Renda elevada e maturidade etária apresentam forte correlação positiva com a pontuação. Além disso, **98,2% dos clientes com casa própria (`Owned`) pertencem à classe de score alto**.
* **Indicadores de Risco (*Low/Average*):** Moradia em imóvel alugado (`Rented`, $r = -0,85$) e estado civil solteiro (`Single`, $r = -0,62$) apresentaram forte associação negativa com o score de crédito.

### 3. Engenharia de Recursos & Mitigação de Viés
* **Encoding de Variáveis:** Aplicação de *One-Hot Encoding* para categóricas nominais (`Gender`, `Marital Status`, `Home Ownership`) e *Label Encoding* para ordinais (`Education` e `Credit Score`).
* **Divisão Estratificada:** Separação rígida em **80% Treino (131 amostras)** e **20% Teste (33 amostras)** para evitar sobreajuste (*Overfitting*).
* **Tratamento do Desequilíbrio de Classes (SMOTE):** A base original continha 68,7% de clientes *High* e apenas 9,2% de clientes *Low*. Aplicou-se a técnica **SMOTE** exclusivamente no conjunto de treino, equilibrando a base em **90 registros por categoria** sem contaminar a base de teste (*Data Leakage*).

---

## 📈 Impacto e Conclusões

Com o pipeline concluído, a empresa passa a contar com:
* **Base Pronta para Modelagem Machine Learning:** Dados 100% numéricos, dimensionados e balanceados.
* **Redução Potencial de Inadimplência:** Identificação clara de variáveis de risco antes da concessão do crédito.
* **Equidade Preditiva:** Garantia de que o futuro modelo aprenderá os padrões de clientes de risco baixo/médio com a mesma precisão da classe majoritária.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn
* **Pré-Processamento & Machine Learning:** Scikit-Learn
* **Balanceamento de Dados:** Imbalanced-Learn (`SMOTE`)

---

## 👩‍💻 Autora

**Aline L.**  
*Estudante de Ciência de Dados — EBAC*  
* GitHub: [@AlineLGo](https://github.com/AlineLGo)
