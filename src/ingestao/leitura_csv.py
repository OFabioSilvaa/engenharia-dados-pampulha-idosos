import pandas as pd

moradores = "data/raw/pampulha_moradores_b.csv"

df = pd.read_csv(
    moradores,
    sep=';',
    encoding='latin-1',
    on_bad_lines='skip'
)

print(df.shape)
print(df.columns)
print(df.info())
print(df.head())

print("\nValores únicos por coluna:\n")

for col in df.columns:
    print(f"Coluna: {col}")
    print(df[col].unique()[:10])
    print("-" * 40)
