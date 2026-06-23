
import statistics

def validar_medicoes(dados):
    validas, descartadas = [], 0
    for valor in dados:
        if isinstance(valor, (int, float)) and -20 <= valor <= 200:
            validas.append(valor)
        else:
            descartadas += 1
    return validas, descartadas

def classificar(valor):
    if valor > 120:
        return "CRITICO"
    elif valor > 90:
        return "ALERTA"
    return "NORMAL"

def calcular_estatisticas(valores):
    return {
        "media": statistics.mean(valores),
        "min": min(valores),
        "max": max(valores),
        "desvio": statistics.stdev(valores) if len(valores) > 1 else 0
    }

def detectar_eventos(valores):
    criticos = [v for v in valores if v > 120]
    maior = atual = 0
    for v in valores:
        if v > 120:
            atual += 1
            maior = max(maior, atual)
        else:
            atual = 0
    return len(criticos), maior

def main():
    dados = [80,95,130,140,85,150,"x",-30]
    validas, descartadas = validar_medicoes(dados)
    print(calcular_estatisticas(validas))

if __name__ == "__main__":
    main()
