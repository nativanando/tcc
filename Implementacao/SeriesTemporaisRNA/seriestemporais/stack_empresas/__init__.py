"""
__init__.py: Arquivo responsável por iniciar as buscas das respectivas empresas selecionadas
"""
from seriestemporais.stack_empresas.amazon import *
from seriestemporais.stack_empresas.apple import *
from seriestemporais.stack_empresas.microsoft import *
from seriestemporais.stack_empresas.cisco import *
from seriestemporais.stack_empresas.intel import *
from seriestemporais.stack_empresas.crawler import *

def main():
    amazon = Amazon()
    busca(amazon)
    apple = Apple()
    busca(apple)
    microsoft = Microsoft()
    busca(microsoft)
    cisco = Cisco
    busca(cisco)
    intel = Intel()
    busca(intel)

def busca(empresa):
    crawler = Crawler(empresa.nome_empresa, empresa.codigo)
    crawler.executa_busca()

if __name__ == '__main__':
    main()