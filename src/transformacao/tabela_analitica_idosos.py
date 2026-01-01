import pandas as pd

# Lê o arquivo original da pesquisa
arquivo = "data/raw/pampulha_moradores_b.csv"

df = pd.read_csv(
    arquivo,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

# Remove o BOM do nome da primeira coluna e padroniza os nomes
df.columns = df.columns.str.replace('ï»¿', '', regex=False)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Mantém apenas os registros da população idosa (60+)
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

# Identifica todas as colunas relacionadas às preferências de lazer
colunas_lazer = [
    col for col in df_idosos.columns
    if col.startswith('principaispreferenciaslazer')
]

# Transforma o formato dos dados para facilitar análise
# (uma linha por idoso e tipo de lazer)
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

# Remove registros onde não houve resposta de lazer
lazer_long = lazer_long.dropna(subset=['tipo_lazer'])

# Padroniza o texto das preferências para evitar duplicidades
lazer_long['tipo_lazer'] = (
    lazer_long['tipo_lazer']
    .str.strip()
    .str.lower()
)

# Salva a tabela analítica final para uso em BI ou análises futuras
saida = "data/processed/tabela_analitica_idosos_lazer.csv"
lazer_long.to_csv(saida, index=False)

print("Tabela analítica criada com sucesso!")
print("Total de registros:", lazer_long.shape[0])
print(lazer_long.head())
