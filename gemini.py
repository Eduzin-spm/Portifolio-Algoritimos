
import math

def eh_valido(v):
    return isinstance(v,(int,float)) and -20 <= v <= 200

def filtrar_dados(dados):
    validos = [v for v in dados if eh_valido(v)]
    return validos, len(dados)-len(validos)

def estatisticas(dados):
    media = sum(dados)/len(dados)
    variancia = sum((x-media)**2 for x in dados)/len(dados)
    return media, min(dados), max(dados), math.sqrt(variancia)

def classificar_medicoes(dados):
    classes = []
    for v in dados:
        if v > 120:
            classes.append("CRITICO")
        elif v > 90:
            classes.append("ALERTA")
        else:
            classes.append("NORMAL")
    return classes
