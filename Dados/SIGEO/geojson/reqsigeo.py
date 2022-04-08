# Função para baixar dados do SIGEO-Niteroi-Dados Abertos
# a partir de uma lista com os nomes das camadas e a URL da API
# salvar na pasta dados/sigeo

import wget
import pandas as pd
import os.path


pasta = "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/SIGEO/geojson"


# Função de requisição para a API SIGEO


def baixar_sigeo(url, pasta, nomea):

    wget.download(url, pasta + nomea + ".geojson")

# Baixar os dados a partir de uma listagem de API


# if __name__ == "main":
df = pd.read_csv(
    "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/sigeo_dado.csv", sep=';')
# print(df)
for x in range(len(df)):
    if(os.path.isfile(pasta + df['nomea'][x] + '.geojson')):
        print("O arquivo existe")
        break
    else:
        baixar_sigeo(df['url'][x], pasta, df['nomea'][x])
