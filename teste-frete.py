# Cliente: decide qual estratégia de frete usar e a injeta no pedido.
# O Pedido apenas executa o cálculo com a estratégia recebida.

from pedido import Pedido
from frete import FreteSedex, FretePac, FreteTransportadora, FreteMotoboy, FreteDrone


def main():
    print("*" * 30)
    print("Executando Versão Refatorada (Strategy)")
    print("*" * 30)

    pedido = Pedido(peso_kg=2.5)

    # Para cada tipo de frete: define a estratégia e depois calcula.
    # O mesmo pedido pode trocar de estratégia sem ser recriado.
    pedido.set_estrategia(FreteSedex())
    print(f"Valor do frete SEDEX: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FretePac())
    print(f"Valor do frete PAC: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FreteTransportadora())
    print(f"Valor do frete TRANSPORTADORA: R$ {pedido.calcular_frete():.2f}")

    pedido.set_estrategia(FreteMotoboy())
    print(f"Valor do frete MOTOBOY: R$ {pedido.calcular_frete():.2f}")

    # Teste de extensibilidade: o novo frete DRONE funciona sem alterar o Pedido.
    pedido.set_estrategia(FreteDrone())
    print(f"Valor do frete DRONE: R$ {pedido.calcular_frete():.2f}")

    # Outro pedido, com peso diferente, usando a mesma lógica de frete.
    pedido2 = Pedido(peso_kg=10.0)
    pedido2.set_estrategia(FretePac())
    print(f"Valor do frete PAC (10 kg): R$ {pedido2.calcular_frete():.2f}")


# Ponto de entrada: executa main() apenas quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    main()
