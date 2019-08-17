import requests
import os

pasta = input("Digite a pasta onde os dados de exportação devem ser salvos:")
print('\nBaixando os dados...')

# Pasta para armazenar os arquivos

if not os.path.exists(pasta):
    os.makedirs(pasta)



# Dados de exportações
arquivos = ['http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2009_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2010_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2011_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2012_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2013_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2014_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2015_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2016_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2017_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2018_MUN.csv',
           'http://www.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2019_MUN.csv']

		   
for url in arquivos:
  
    r = requests.get(url)
    with open(os.path.join(pasta, url.split('/')[-1]), mode='wb') as file:
        file.write(r.content)

print('\nDados das exportações salvos em {}!'.format(pasta))

# Dados auxiliares
pasta_dados_aux_produtos = input("\nDigite o caminho onde as tabelas auxiliares devem ser salvas:")

print('\nBaixando os dados...')
		
# Baixando as tabelas auxiliares
if not os.path.exists(pasta_dados_aux_produtos):
    os.makedirs(pasta_dados_aux_produtos)

    
dados_auxiliares = ['http://www.mdic.gov.br/balanca/bd/tabelas/NCM.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_SH.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_CUCI.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_CGCE.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_ISIC.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_SIIT.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_FAT_AGREG.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_PPE.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/NCM_UNIDADE.csv',
                   ]
		
		
for url in dados_auxiliares:    
    r = requests.get(url)
    with open(os.path.join(pasta_dados_aux_produtos, url.split('/')[-1]), mode='wb') as file:
        file.write(r.content)

print('\nDados auxiliares salvos em {}!'.format(pasta_dados_aux_produtos))



# Baixando as tabelas auxiliares - paises, ufs
pasta_paises_blocos = input('\nDigite a pasta onde os dados de UF e país devem ser salvos:')
print('\nBaixando os dados...')

if not os.path.exists(pasta_paises_blocos):
    os.makedirs(pasta_paises_blocos)

    
dados_paises_blocos = ['http://www.mdic.gov.br/balanca/bd/tabelas/PAIS.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv',
                   'http://www.mdic.gov.br/balanca/bd/tabelas/UF.csv',
                      'http://www.mdic.gov.br/balanca/bd/tabelas/VIA.csv',
                      'http://www.mdic.gov.br/balanca/bd/tabelas/URF.csv']


for url in dados_paises_blocos:
    
    r = requests.get(url)
    with open(os.path.join(pasta_paises_blocos, url.split('/')[-1]), mode='wb') as file:
        file.write(r.content)
		
print('\nTodos os dados foram baixados!')
