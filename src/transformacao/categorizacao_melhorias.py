import pandas as pd

arquivo = "data/raw/pampulha_moradores_b.csv"

df = pd.read_csv(
    arquivo,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Filtra idosos
df_idosos = df[df['faixaidade'] == 'Com 60 anos ou mais']

# Função de categorização simples
def categorizar_melhoria(texto):
    if pd.isna(texto):
        return None
    texto = texto.lower()

    if "limpeza" in texto or "lagoa" in texto or "fedor" in texto:
        return "Limpeza e Meio Ambiente"
    elif "segurança" in texto:
        return "Segurança"
    elif "banheiro" in texto:
        return "Infraestrutura básica"
    elif "transporte" in texto or "acesso" in texto:
        return "Acesso e Mobilidade"
    elif "aliment" in texto or "lanchonete" in texto:
        return "Alimentação"
    else:
        return "Outros"

df_idosos['categoria_melhoria'] = df_idosos['quais_melhorias'].apply(categorizar_melhoria)

print("\nPrincipais categorias de melhoria:")
print(df_idosos['categoria_melhoria'].value_counts())
