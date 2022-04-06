# Função para baixar dados do SIGEO-Niteroi-Dados Abertos
# a partir de uma lista com os nomes das camadas e a URL da API
# salvar na pasta dados/sigeo

import wget
import pandas as pd

# url = "https://opendata.arcgis.com/datasets/c5ba3f423a084e559cef63c07447cbb3_30.geojson"
pasta = "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/SIGEO/"
# nomea = "logradouro"

# Função de requisição para a API SIGEO


def baixar_sigeo(url, pasta, nomea):

    wget.download(url, pasta + nomea + ".geojson")


# if __name__ == "main":
df = pd.read_csv(
    "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/sigeo_dado.csv", sep=';')
# print(df)
for x in range(len(df)):
    baixar_sigeo(df['url'][x], pasta, df['nomea'][x])
