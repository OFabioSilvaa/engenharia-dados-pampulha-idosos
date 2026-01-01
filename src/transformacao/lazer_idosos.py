import pandas as pd

# Leitura do arquivo original da pesquisa
arquivo = "data/raw/pampulha_moradores_b.csv"

df = pd.read_csv(
    arquivo,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

# Padroniza os nomes das colunas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Filtra apenas os respondentes com 60 anos ou mais
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

# Colunas que representam preferências de lazer
colunas_lazer = [
    col for col in df_idosos.columns
    if col.startswith('principaispreferenciaslazer')
]

# Transforma as respostas múltiplas em formato long
lazer_long = df_idosos[colunas_lazer].melt(
    value_name='tipo_lazer'
)

# Remove respostas vazias
lazer_long = lazer_long.dropna()

# Gera o ranking de preferências
ranking_lazer = lazer_long['tipo_lazer'].value_counts()

print("\nRanking de preferências de lazer dos idosos:")
print(ranking_lazer)
