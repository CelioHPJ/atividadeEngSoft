# Padrão Strategy: cada forma de calcular o frete vira uma classe separada.
# Assim, novos tipos de frete são adicionados criando classes novas,
# sem modificar o código que já existe (Princípio Aberto/Fechado).

from abc import ABC, abstractmethod


# Strategy (interface): contrato comum a todos os fretes.
# Quem usa o frete (o Pedido) conhece apenas esta abstração, nunca as classes concretas.
class EstrategiaFrete(ABC):

    # Método abstrato: toda subclasse é obrigada a implementá-lo.
    # Recebe o pedido para poder usar seus dados (ex.: peso) no cálculo.
    @abstractmethod
    def calcular(self, pedido) -> float:
        pass


# --- Estratégias concretas ---
# Cada classe contém a regra que antes ficava em um "elif" do Pedido.

# SEDEX: taxa base de R$ 10 + R$ 1,50 por kg.
class FreteSedex(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 10.0 + (pedido.peso_kg * 1.5)


# PAC: taxa base de R$ 5 + R$ 1,00 por kg.
class FretePac(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 5.0 + (pedido.peso_kg * 1.0)


# Transportadora: taxa base de R$ 20 + R$ 3,00 por kg.
class FreteTransportadora(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 20.0 + (pedido.peso_kg * 3.0)


# Motoboy: valor fixo de R$ 15, independente do peso.
class FreteMotoboy(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 15.0


# Drone (novo requisito): valor fixo de R$ 25.
# Foi adicionado apenas criando esta classe; a classe Pedido não foi alterada.
class FreteDrone(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 25.0
