"""
__init__.py: Arquivo responsável por iniciar as buscas das respectivas empresas selecionadas.
"""
from seriestemporais.stack_empresas.amazon import *
from seriestemporais.stack_empresas.apple import *
from seriestemporais.stack_empresas.microsoft import *
from seriestemporais.stack_empresas.cisco import *
from seriestemporais.stack_empresas.intel import *
from seriestemporais.stack_empresas.crawler import *

__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"
__version__ = "0.0.1"

def main():
    amazon = Amazon()
    apple = Apple()
    cisco = Cisco()
    intel = Intel()
    microsoft = Microsoft()

if __name__ == '__main__':
    main()