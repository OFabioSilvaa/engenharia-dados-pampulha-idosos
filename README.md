# Engenharia de Dados — Percepção de Idosos sobre a Pampulha (BH)

## 1. Contexto e Problema

O envelhecimento da população exige políticas públicas e soluções urbanas cada vez mais orientadas por dados. Este projeto analisa a percepção de moradores **idosos (60+)** de Belo Horizonte sobre o **Complexo da Pampulha**, com foco em lazer, mobilidade urbana e necessidades de melhoria.

O objetivo central é **construir um pipeline de Engenharia de Dados do zero**, utilizando dados públicos reais, para gerar **tabelas analíticas confiáveis**, prontas para análises, dashboards e apoio à tomada de decisão.

O foco do projeto está na **engenharia de dados**: ingestão, limpeza, aplicação de regras de negócio e modelagem analítica.

---

## 2. Fonte de Dados

* **Portal:** Dados Abertos da Prefeitura de Belo Horizonte (PBH)
* **Pesquisa:** Percepção dos moradores de Belo Horizonte sobre o Complexo da Pampulha (2019)
* **Link oficial do dataset (PBH):** [https://dados.pbh.gov.br/dataset/pesquisa-de-percepcao-dos-moradores-de-belo-horizonte-sobre-o-complexo-da-pampulha-2019/resource/05e00aac-99f9-48b8-9585-daaa490a7ae4](https://dados.pbh.gov.br/dataset/pesquisa-de-percepcao-dos-moradores-de-belo-horizonte-sobre-o-complexo-da-pampulha-2019/resource/05e00aac-99f9-48b8-9585-daaa490a7ae4)
* **Formato original:** CSV (dados brutos, não tratados)

### Características dos dados

* Dados reais
* Presença de valores nulos
* Encoding inconsistente (BOM / latin-1)
* Colunas não padronizadas
* Respostas múltiplas distribuídas em várias colunas

---

## 3. Arquitetura do Projeto

```
engenharia-dados-pampulha-idosos/
│
├── data/
│   ├── raw/            # Dados brutos
│   └── processed/      # Dados tratados e tabelas analíticas
│
├── src/
│   ├── ingestao/       # Leitura, encoding e padronização inicial
│   └── transformacao/  # Limpeza, regras de negócio e modelagem
│
└── README.md
```

---

## 4. Pipeline de Dados (ETL)

### 4.1 Ingestão

* Leitura do CSV original
* Tratamento de encoding (remoção de BOM e ajuste para latin-1)
* Remoção de registros inválidos
* Padronização de nomes de colunas

### 4.2 Limpeza e Transformação

* Normalização de textos
* Conversão de tipos de dados
* Tratamento de valores ausentes
* Aplicação de regras de negócio

### 4.3 Enriquecimento

* Filtro da população idosa (idade ≥ 60 anos)
* Criação da variável `grupo_etario`
* Categorização das sugestões de melhoria
* Análise da percepção urbana
* Ranking de preferências de lazer

### 4.4 Modelagem Analítica

* Conversão do formato **wide → long**
* Criação de **tabela analítica final**, pronta para BI e Analytics

---

## 5. Principais Resultados

* **Total de registros analisados:** 660
* **Total de idosos identificados:** 110
* **Registros na tabela analítica final:** 178

### Insights relevantes

* **82%** dos idosos acreditam que a Pampulha precisa de melhorias
* A principal demanda está relacionada à **limpeza e meio ambiente**
* A preferência dominante é por **atividades ao ar livre**

---

## 6. Tecnologias Utilizadas

* Python
* Pandas
* Estruturação de pipelines de dados (ETL)
* Modelagem analítica
* Dados públicos

---

## 7. Próximos Passos

* Criação de dashboards (Power BI / Looker Studio)
* Evolução para processamento distribuído (PySpark)
* Integração com bancos de dados
* Storytelling e publicação de análises no LinkedIn

---

## 8. Aprendizados

Este projeto **reproduz desafios reais** enfrentados por Engenheiros de Dados, incluindo:

* Dados sujos e inconsistentes
* Problemas de schema
* Padronização de dados
* Definição de regras de negócio
* Modelagem analítica
* Estruturação de pipelines reutilizáveis

---

📌 Projeto desenvolvido com foco em **aprendizado prático**, **engenharia de dados** e **impacto social**, utilizando dados públicos reais da cidade de Belo Horizonte.
