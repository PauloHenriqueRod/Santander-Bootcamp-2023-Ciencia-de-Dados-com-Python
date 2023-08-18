def deposito(saldo:float, valor:float) -> None:
    return saldo+valor

def saque(saldo:float, valor: float) -> None:
    return saldo-valor


saldo_atual = float(input())
valor_deposito = float(input())
saldo_atual = deposito(saldo=saldo_atual, valor=valor_deposito)
valor_retirada = float(input())
saldo_atual = saque(saldo=saldo_atual, valor=valor_retirada)
print(f'Saldo atualizado na conta: {saldo_atual:.1f}')