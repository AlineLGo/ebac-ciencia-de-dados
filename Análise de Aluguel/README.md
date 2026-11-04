# 🏢 Análise Preditiva de Preços de Aluguéis Imobiliários

Este projeto de Ciência de Dados desenvolve e compara modelos de **Regressão Linear Simples** e **Regressão Linear Múltipla** para a precificação de aluguéis residenciais. O projeto foi elaborado como parte do curso de Ciência de Dados da **EBAC** (Escola Britânica de Artes Criativas e Tecnologia).

O objetivo principal é prever o `Valor_Aluguel` de imóveis a partir de suas características físicas e financeiras, avaliando o ganho de desempenho ao migrar de um modelo univariado para um modelo multivariado.

---

## 📌 Principais Resultados e Métricas ($R^2$)

| Modelo | Variáveis Utilizadas | $R^2$ Treino | $R^2$ Teste | Avaliação de Desempenho |
| :--- | :--- | :---: | :---: | :--- |
| **Regressão Linear Simples** | `Metragem` | 52,14% | 56,98% | Modelo estável, porém limitado por utilizar apenas 1 variável. |
| **Regressão Linear Múltipla** | `Metragem`, `Valor_Condominio`, `N_Quartos`, `N_banheiros`, `N_Suites`, `N_Vagas` | 59,72% | **63,28%** | **Melhor Desempenho (+6.3% no teste)**, capturando múltiplos fatores de preço. |

> **Conclusão:** O modelo de Regressão Múltipla apresentou melhor capacidade de generalização nos dados inéditos (teste), confirmando que a precificação imobiliária depende do impacto conjunto de diversas características do imóvel.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.x
* **Análise de Dados:** Pandas, NumPy
* **Visualização de Dados:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (`LinearRegression`, `train_test_split`)

---

## 📊 Estrutura e Etapas do Projeto

1. **Exploração e Limpeza de Dados:**
   * Diagnóstico de estrutura (`info()`) e verificação de valores ausentes (ausência de dados nulos).
   * Tratamento formal de *outliers* utilizando a **Amplitude Interquartil (IQR)** para garantir distribuição consistente dos dados.
2. **Análise Bivariada e Visual:**
   * Avaliação da dispersão e tendência do `Valor_Aluguel` em relação às principais características.
   * Identificação de particularidades do mercado, como o valor elevado por m² em imóveis compactos (studios/1 quarto) em regiões nobres.
3. **Matriz de Correlação:**
   * Identificação das variáveis explicativas com maior associação ao preço final, destacando `Valor_Condominio` ($0,46$), `Metragem` ($0,46$) e `N_Vagas` ($0,40$).
4. **Treinamento e Avaliação dos Modelos:**
   * Separação dos dados em conjuntos de **Treino (80%)** e **Teste (20%)**.
   * Treinamento e extração de parâmetros da equação da reta ($y = a + bx$).
   * Comparação dos resultados via Coeficiente de Determinação ($R^2$).

---

## 🚀 Próximos Passos e Melhorias Futuras (Feedback Técnico)

Com base na revisão contínua do pipeline, os próximos aprimoramentos previstos incluem:
* [ ] **Ajuste de Data Leakage:** Reestruturação do cálculo do IQR estritamente no conjunto de treino antes de aplicá-lo ao conjunto de teste.
* [ ] **Análise de Multicolinearidade:** Avaliação de VIF (*Variance Inflation Factor*) entre variáveis explicativas altamente correlacionadas (ex: metragem vs. número de quartos).
* [ ] **Padronização de Features (*Z-score*):** Escalonamento das variáveis para comparar diretamente a magnitude dos coeficientes angulares.
* [ ] **Análise de Resíduos:** Plotagem diagnóstica para validação das premissas de homocedasticidade e normalidade dos erros.

---

## 👤 Autora

* **Aline Lopes Gomes**
* Data Science Student @ EBAC
* GitHub: [@AlineLGo](https://github.com/AlineLGo)
