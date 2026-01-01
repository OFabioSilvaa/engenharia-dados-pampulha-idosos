import pandas as pd

# Leitura dos dados
arquivo = "data/raw/pampulha_moradores_b.csv"

df = pd.read_csv(
    arquivo,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

# Padronização de colunas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Filtro de idosos
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

print("Total de idosos:", df_idosos.shape[0])

# Análise: precisa de melhorias?
print("\nNecessidade de melhorias:")
print(df_idosos['precisa_melhorias'].value_counts())

# Análise: quais melhorias (texto livre)
print("\nPrincipais sugestões de melhoria:")
print(
    df_idosos['quais_melhorias']
    .dropna()
    .value_counts()
)
