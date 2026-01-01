# Engenharia de Dados & IA — Percepção de Idosos sobre a Pampulha (BH)

## 1. Contexto e Problema

O envelhecimento da população exige políticas públicas e soluções urbanas baseadas em dados. Este projeto analisa a **percepção de moradores idosos (60+) de Belo Horizonte** sobre o Complexo da Pampulha, com foco em **lazer, mobilidade e necessidade de melhorias**.

O objetivo é **construir um pipeline de dados do zero**, utilizando dados públicos reais, para gerar **tabelas analíticas confiáveis** que apoiem decisões e análises futuras.

---

## 2. Fonte de Dados

* **Portal de Dados Abertos da Prefeitura de Belo Horizonte**
* Pesquisa: *Percepção dos moradores de Belo Horizonte sobre o Complexo da Pampulha (2019)*
* Formato original: CSV (dados brutos, não tratados)

Características dos dados:

* Dados reais
* Presença de valores nulos
* Colunas não padronizadas
* Respostas múltiplas em colunas distintas

---

## 3. Arquitetura do Projeto

```
engenharia-dados-pampulha-idosos/
│
├── data/
│   ├── raw/          # Dados brutos
│   └── processed/    # Dados tratados e analíticos
│
├── src/
│   ├── ingestao/     # Leitura e padronização inicial
│   └── transformacao/# Limpeza, regras de negócio e modelagem
│
└── README.md
```

---

## 4. Pipeline de Dados

### 4.1 Ingestão

* Leitura do CSV original
* Tratamento de encoding (latin-1)
* Remoção de registros inválidos
* Padronização de nomes de colunas

### 4.2 Limpeza e Transformação

* Remoção de BOM (Byte Order Mark)
* Normalização de texto
* Conversão de tipos
* Criação de regras de negócio

### 4.3 Enriquecimento

* Filtro da população idosa (60+)
* Categorização de sugestões de melhoria
* Análise de percepção urbana
* Ranking de preferências de lazer

### 4.4 Modelagem Analítica

* Conversão de dados *wide → long*
* Criação de **tabela analítica final** pronta para BI e Analytics

---

## 5. Principais Resultados

* Total de registros analisados: **660**
* Total de idosos identificados: **110**
* Registros na tabela analítica final: **178**

### Insights relevantes:

* **82%** dos idosos acreditam que a Pampulha precisa de melhorias
* A maior demanda está relacionada à **limpeza e meio ambiente**
* Preferência dominante por **atividades ao ar livre**

---

## 6. Tecnologias Utilizadas

* Python
* Pandas
* Estruturação de pipelines de dados
* Modelagem analítica
* Dados públicos

---

## 7. Próximos Passos

* Criação de dashboards (Power BI / Data Studio)
* Evolução para processamento distribuído (PySpark)
* Integração com bancos de dados
* Storytelling e publicação no LinkedIn

---

## 8. Aprendizados

Este projeto simula desafios reais enfrentados por **Engenheiros de Dados**, incluindo:

* Dados sujos
* Problemas de schema
* Padronização
* Modelagem analítica
* Estruturação de pipelines reutilizáveis

---

📌 Projeto desenvolvido com foco em **aprendizado prático**, engenharia de dados e impacto social.
