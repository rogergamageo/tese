import wget

pasta = "/home/rogeriogama/Área de Trabalho/Projetos/Tese/Dados/"
nomea = "logradouro"


def baixar_sigeo(url, pasta, nomea):
    wget.download(url, pasta + nomea + ".geojson")
