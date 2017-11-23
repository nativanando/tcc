from rna.model.multilayer import *

def main():
    network = None
    rna = MultiLayer(network, 8, 13, 1, "intel")
    rna.adicionaDadosTreinamento()
    rna.testarRedeEmpresa()

if __name__ == '__main__':
    main()