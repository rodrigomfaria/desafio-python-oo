class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            resultado = transacao.registrar(conta)
            if resultado:
                conta.historico.adicionar_transacao(transacao)
            return resultado
        return False

    def adicionar_conta(self, conta):
        self.contas.append(conta)

