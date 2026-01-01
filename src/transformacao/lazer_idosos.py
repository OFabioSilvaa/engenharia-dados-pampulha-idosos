import pandas as pd

# ===============================
# 1. Leitura dos dados
# ===============================
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

# ===============================
# 2. Filtra apenas idosos
# ===============================
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

# ===============================
# 3. Seleciona colunas de lazer
# ===============================
colunas_lazer = [
    col for col in df_idosos.columns
    if col.startswith('principaispreferenciaslazer')
]

# ===============================
# 4. Transforma wide → long
# ===============================
lazer_long = df_idosos[colunas_lazer].melt(
    value_name='tipo_lazer'
)

# Remove valores vazios
lazer_long = lazer_long.dropna()

# ===============================
# 5. Ranking de preferências
# ===============================
ranking_lazer = lazer_long['tipo_lazer'].value_counts()

print("\nRanking de preferências de lazer dos idosos:")
print(ranking_lazer)
