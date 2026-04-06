class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: valor inválido.\n")
            return
        self.saldo += valor
        print("Depósito realizado com sucesso!\n")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: valor inválido.\n")
        elif valor > self.saldo:
            print("Erro: saldo insuficiente.\n")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso!\n")

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}\n")


def menu():
    conta = ContaBancaria("Adan", 100.0)

    while True:
        print("===== CONTA BANCÁRIA =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando sistema...")
            break

        try:
            if opcao == "1":
                valor = float(input("Valor para depósito: "))
                conta.depositar(valor)
            elif opcao == "2":
                valor = float(input("Valor para saque: "))
                conta.sacar(valor)
            elif opcao == "3":
                conta.exibir_saldo()
            else:
                print("Opção inválida!\n")

        except ValueError:
            print("Erro: digite um valor numérico válido.\n")


if __name__ == "__main__":
    menu()