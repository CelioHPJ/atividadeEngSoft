# Representa um pedido em um sistema de comércio eletrônico.
# No padrão Strategy, esta classe é o "Contexto": ela não sabe COMO o frete
# é calculado, apenas guarda uma estratégia e delega o cálculo para ela.

from frete import EstrategiaFrete


class Pedido:

    def __init__(self, peso_kg: float):
        self._peso_kg = peso_kg
        # Estratégia de frete atual; começa vazia e é definida pelo cliente.
        self._estrategia: EstrategiaFrete | None = None

    # Setter: permite ao cliente escolher (injetar) a estratégia de frete.
    # Pode ser trocada a qualquer momento, inclusive em tempo de execução.
    def set_estrategia(self, estrategia: EstrategiaFrete) -> None:
        self._estrategia = estrategia

    # Delega o cálculo para a estratégia definida, passando o próprio pedido.
    # Substitui o antigo if/elif: o Pedido não precisa mudar quando surge um novo frete.
    def calcular_frete(self) -> float:
        if self._estrategia is None:
            raise ValueError("Nenhuma estratégia de frete definida.")
        return self._estrategia.calcular(self)

    # Getter (somente leitura) do peso, usado pelas estratégias no cálculo.
    @property
    def peso_kg(self) -> float:
        return self._peso_kg
