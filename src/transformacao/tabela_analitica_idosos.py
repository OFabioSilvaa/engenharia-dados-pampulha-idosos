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

# ===============================
# 2. Padronização de colunas
# ===============================
df.columns = df.columns.str.replace('ï»¿', '', regex=False)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# ===============================
# 3. Filtra idosos
# ===============================
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

# ===============================
# 4. Colunas de lazer
# ===============================
colunas_lazer = [
    col for col in df_idosos.columns
    if col.startswith('principaispreferenciaslazer')
]

# ===============================
# 5. Normalização (wide → long)
# ===============================
lazer_long = df_idosos.melt(
    id_vars=[
        'respondent_id',
        'sexo',
        'idade',
        'regionalmora',
        'precisa_melhorias',
        'indicaria_pampulha_lazer'
    ],
    value_vars=colunas_lazer,
    value_name='tipo_lazer'
)

# Remove valores nulos
lazer_long = lazer_long.dropna(subset=['tipo_lazer'])

# ===============================
# 6. Limpeza textual
# ===============================
lazer_long['tipo_lazer'] = (
    lazer_long['tipo_lazer']
    .str.strip()
    .str.lower()
)

# ===============================
# 7. Salva dataset final
# ===============================
saida = "data/processed/tabela_analitica_idosos_lazer.csv"
lazer_long.to_csv(saida, index=False)

print("Tabela analítica criada com sucesso!")
print("Total de registros:", lazer_long.shape[0])
print(lazer_long.head())
