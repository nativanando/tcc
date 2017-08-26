from seriestemporais.pandas_analise.Analisador import *

if __name__ == '__main__':
    analisador = Analisador('microsoft')
    analisador.calcula_media_movel(26)
    analisador.calcula_media_movel(10)
    analisador.formata_dataset()

    analisador1 = Analisador('intel')
    analisador1.calcula_media_movel(26)
    analisador1.calcula_media_movel(10)
    analisador1.formata_dataset()

    analisador2 = Analisador('cisco')
    analisador2.calcula_media_movel(26)
    analisador2.calcula_media_movel(10)
    analisador2.formata_dataset()

    analisador3 = Analisador('apple')
    analisador3.calcula_media_movel(26)
    analisador3.calcula_media_movel(10)
    analisador3.formata_dataset()

    analisador4 = Analisador('amazon')
    analisador4.calcula_media_movel(26)
    analisador4.calcula_media_movel(10)
    analisador4.formata_dataset()


