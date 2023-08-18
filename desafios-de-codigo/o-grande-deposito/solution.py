saldo = 0
valor = float(input())
if valor > 0:
    saldo += valor
    print(f'Deposito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}')
elif valor == 0:
    print('Encerrando o programa...')
else:
    print('Valor invalido! Digite um valor maior que zero.')