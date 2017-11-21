from rna.model.multilayer import *

def main():
    network = None
    rna = MultiLayer(network, 8, 13, 1, "intel")
    rna.adicionaDadosTreinamento()
    rna.realizaTreinamento()
    rna.testaRede()
if __name__ == '__main__':
    main()