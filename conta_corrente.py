from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques, agencia="0001"):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            return False
        if valor > self.limite:
            return False
        if super().sacar(valor):
            self.saques_realizados += 1
            return True
        return False

