import pandas as pd

# Caminho do arquivo
moradores = "data/raw/pampulha_moradores_b.csv"

# Leitura
df = pd.read_csv(
    moradores,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

# Padronizando nomes das colunas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Criando grupo etário
df['grupo_etario'] = df['faixaidade']

# Filtrando apenas idosos
df_idosos = df[df['grupo_etario'] == 'Com 60 anos ou mais']

print("Total de registros:", df.shape[0])
print("Total de idosos:", df_idosos.shape[0])

print("\nExemplo de dados dos idosos:")
print(df_idosos.head())
