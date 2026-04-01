from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from operacoes import Deposito, Saque
from datetime import date

if __name__ == "__main__":
    cliente = PessoaFisica("123.456.789-00", "João Silva", date(1990, 5, 20), "Rua das Flores, 123")
    conta = ContaCorrente(cliente, 1, limite=500, limite_saques=3)
    cliente.adicionar_conta(conta)

    print(f"Saldo inicial: {conta.saldo}")
    cliente.realizar_transacao(conta, Deposito(200))
    print(f"Saldo após depósito: {conta.saldo}")
    cliente.realizar_transacao(conta, Saque(100))
    print(f"Saldo após saque: {conta.saldo}")
    print(f"Transações registradas: {len(conta.historico.transacoes)}")

