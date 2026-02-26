import requests
import pandas as pd

# Tabela 1612 - Produção agrícola municipal
# Produto 393 - Soja
# Variável 214 - Quantidade produzida
# Ano 2021 (mais estável)
# Municípios (n6)

url = "https://apisidra.ibge.gov.br/values/t/1612/n6/all/v/214/p/2021/c81/393"

response = requests.get(url)

if response.status_code != 200:
    print("Erro na API:", response.status_code)
    print(response.text)
    exit()

data = response.json()

# Criar DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Selecionar colunas corretas
df = df[["D1C", "D1N", "V"]]

# Renomear
df = df.rename(columns={
    "D1C": "cod_municipio",
    "D1N": "municipio",
    "V": "producao_ton"
})

# Filtrar apenas municípios de SP (código começa com 35)
df = df[df["cod_municipio"].str.startswith("35")]

# Limpar valores
df["producao_ton"] = df["producao_ton"].str.replace(",", ".", regex=False)
df["producao_ton"] = pd.to_numeric(df["producao_ton"], errors="coerce")

# Remover municípios sem produção
df = df.dropna(subset=["producao_ton"])

# Ordenar do maior para o menor
df = df.sort_values(by="producao_ton", ascending=False)

# Exportar CSV
df.to_csv("soja_sp_2021.csv", index=False)

print(df.head())
print("\nTotal municípios com produção:", len(df))
print("Produção total SP:", df["producao_ton"].sum())
print("\nArquivo exportado: soja_sp_2021.csv")