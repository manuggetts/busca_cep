import requests
import pandas as pd

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Lendo os CEPs da planilha
df = pd.read_excel('ceps.xlsx')

# Buscando as infos de cada CEP e adicionando ao DataFrame
for i, row in df.iterrows():
    cep = row['CEP']
    resultado = buscar_cep(cep)
    if resultado:
        for key, value in resultado.items():
            if key != 'cep':  # Ignorando a chave 'cep' porque já temos essa coluna
                df.loc[i, key] = value

# DataFrame atualizado na planilha original
df.to_excel('ceps.xlsx', index=False)