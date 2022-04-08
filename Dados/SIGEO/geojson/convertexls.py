import pandas as pd
wb = pd.read_excel(
    '/home/rogeriogama/Área de Trabalho/Projetos/tese/Dados/sigeo_dado.xlsx')
df = pd.DataFrame(wb)
df.to_csv('sigeo_dado.csv', sep=';', index=False)
