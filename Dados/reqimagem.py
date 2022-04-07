import wget
import pandas as pd

pasta = "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/SIGEO/"

# Função de requisição para a API SIGEO


def baixar_sigeo(url, pasta, nomea):

    wget.download(url, pasta + nomea + ".tiff")

# Baixar os dados a partir de uma listagem de url


df = pd.read_csv(
    "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/imagem_nit.csv", sep=';')
# print(df)
for x in range(len(df)):
    if df['tipo'] == 'TIFF':
        baixar_sigeo(df['url'][x], pasta, df['nomei'][x])
