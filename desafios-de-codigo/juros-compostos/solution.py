def juros_compostos(valor_inicial: float, taxa: float, tempo: int) -> float:
    return round(valor_inicial*(1+taxa)**(tempo), 2)


valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = juros_compostos(valor_inicial=valor_inicial, taxa=taxa_juros, tempo=periodo)

print(f"Valor final do investimento: R$ {valor_final}")