import wget
import pandas as pd
from zipfile import ZipFile

pasta = "/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/SIGEO/imagem"

# Função de requisição para a API SIGEO


def baixar_imagem(url, pasta, nomea):
    wget.download(url, pasta + nomea + ".zip")
    z = ZipFile(pasta+nomea+'.zip', 'r')
    z.extractall(pasta)
    z.close()


# Baixar os dados a partir de uma listagem de url
coluna = ['6907', '6923', '6939', '6955', '6971', '6987', '7003',
          '7019', '7035', '7051', '7067', '7083', '7099', '7115']
linha = ['74714', '74704', '74694', '74684', '74674', '74664', '74654', '74644',
         '74634', '74624', '74614', '74604', '74594', '74584', '74574', '74564']

# print(df)
for x in coluna:
    for y in linha:
        baixar_imagem("http://www.sigeo.niteroi.rj.gov.br/ortofotos/2019/TIFF/" +
                      '{}-{}'.format(x, y) + "-TIFF.zip", pasta, '{}-{}'.format(x, y))
        print('{}-{}'.format(x, y))
