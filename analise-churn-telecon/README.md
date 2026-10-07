Projeto: Análise de Dados de Churn em Telecomunicações

📋 Sobre o Projeto
Este projeto tem como objetivo analisar o comportamento de clientes de uma empresa de telecomunicações para identificar os principais fatores associados ao cancelamento de serviços (Churn). O pipeline do projeto abrange a limpeza e tratamento de dados, análise descritiva, tratamento de outliers e uma análise bivariada aprofundada para apoiar decisões estratégicas de retenção.

🛠️ 1. Preparação e Limpeza dos Dados
Antes da exploração estatística, a base de dados passou por um rigoroso processo de tratamento de qualidade para garantir a integridade das análises:

Carregamento e Padronização: Leitura de bases estruturadas, correção de delimitadores (separadores por ponto e vírgula ;) e normalização dos nomes das colunas para o formato snake_case.

Tratamento de Tipos e Nulos: Conversão de tipos de dados (como a variável de idosos/Idoso), tratamento de valores ausentes através de imputação ou remoção estratégica, e uniformização das categorias textuais.

Exportação: Salvamento da base tratada e limpa (telecom_dados_limpos.csv) pronta para modelagem e consumo.

📊 2. Análise Exploratória de Dados (EDA)
A exploração inicial permitiu compreender a distribuição estatística e o comportamento macro da base de clientes:

Estatística Descritiva (.describe()): Identificou-se que o tempo_como_cliente varia de recém-chegados (0 meses) até veteranos de 72 meses (6 anos). A média de pagamento_mensal ($66.35) revelou que a base de clientes está massivamente concentrada nos pacotes básicos e intermediários.

Investigação de Outliers: Através de gráficos Boxplot e histogramas na variável total_pago, concluiu-se que os valores máximos elevados não representam erros ou outliers matemáticos, mas sim o acúmulo natural de clientes antigos e fiéis.

Análise de Balanceamento: Verificou-se que a base possui um desbalanceamento significativo na variável alvo (churn), com uma ampla maioria de clientes ativos (No) em relação aos cancelamentos (Yes), o que alerta para a necessidade de técnicas de balanceamento futuras em modelos preditivos.

🔍 3. Análise Bivariada e Insights Estratégicos
Cruzamos o cancelamento (churn) com os principais pilares operacionais, resultando nos seguintes insights críticos para o negócio:

Tipo de Contrato (tipo_contrato): Clientes com contratos mensais (Month-to-month) apresentam uma taxa de churn alarmante de 42,39%, enquanto contratos bianuais reduzem o abandono para apenas 1,49%. O compromisso de longo prazo é o maior fator de retenção.

Método de Pagamento (metodo_pagamento): O Electronic check destaca-se negativamente como o principal canal associado ao cancelamento (45,55% de churn), indicando forte fricção ou falta de fidelização em comparação com os pagamentos automáticos.

Serviço de Internet (servico_internet): O serviço de Fibra Óptica (Fiber optic), principal produto da operadora, apresenta uma anomalia crítica com cerca de 42% de taxa de abandono, exigindo auditoria de preços e competitividade de mercado.

Suporte Técnico (suporte_tecnico): Clientes que optam por não contratar o suporte técnico adicional abandonam o serviço em massa (42,03%), demonstrando que o suporte especializado funciona como uma barreira preventiva essencial contra o churn.

🎯 4. Conclusão e Recomendações
As três variáveis de maior impacto crítico para a retenção são o tipo de contrato, o tipo de serviço de internet e o método de pagamento.

Ação Recomendada: Recomenda-se uma atuação integrada entre o Marketing (campanhas de incentivo à migração para planos anuais) e as Vendas (estímulo a meios de pagamento automáticos e integração de pacotes de suporte técnico) para reduzir a evasão de clientes.
