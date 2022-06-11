from random import randint

class Propriedade:
    def __init__(self, id) -> None:
        self.id = id
        self.aluguel = randint(45, 150)
        self.venda = randint(45, 150)

    