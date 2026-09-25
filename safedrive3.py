def FusaoDeSensores(x,y,z):
    #ordena em crescente os valores
    if x > y and x > z and z < y:
        mediana = y
        return mediana
    elif x > y and x > z and z > y:
        mediana = z
        return mediana
    else:
        mediana = x
        return mediana
        


def CalcDistanciaSegura(x,y,z):
    Vms = x / 3.6
    tempoDeReacao = float(1.5)
    if y == 3:
        tempoDeReacao = float(2.0)
    elif y == 1:
        tempoDeReacao = float(1.0)
    atrito = z
    
    DistanciaSegura = (Vms * tempoDeReacao) + (Vms**2) / (2 * atrito * 9.81)

    return DistanciaSegura 

def anlsColisaoFrontal(a,b,c,d):
    veloAtual = a
    veloFrente = b
    veloRelativa = veloAtual - veloFrente
    distanciaSegura = c
    distanciaValidada = d
    status = 'SEGURO'
    if veloRelativa <= float(0):
        return status
    elif distanciaValidada >= distanciaSegura:
        return status
    elif distanciaValidada < distanciaSegura and distanciaValidada >= (distanciaSegura / 2):
        status = 'ATENÇÃO'
        return status
    else:
        status = 'RISCO DE COLISÃO'
        return status

def assAcrescimoDinamico(x,y,z):
    velocidadeAtual = x
    distFaixaEsq = y
    distFaixaDir = z
    margemBase = float(0.50)
    acrescimoDinamico = float()
    margemSeguranca = float(0.20)
    statusFaixaEsq = 'NORMAL'
    statusFaixaDir = 'NORMAL'

    if velocidadeAtual > 80:
        acrescimoDinamico = (0.01 * (velocidadeAtual - 80)) + margemBase
    else:
        acrescimoDinamico = margemBase


    if distFaixaEsq < (acrescimoDinamico + margemSeguranca):
        statusFaixaEsq = 'ATENÇÃO'
    elif distFaixaEsq < acrescimoDinamico:
        statusFaixaEsq = 'PERIGO DE INVASÃO'

    if distFaixaDir < (acrescimoDinamico + margemSeguranca):
        statusFaixaDir = 'ATENÇÃO'
    elif distFaixaDir < acrescimoDinamico:
        statusFaixaDir = 'PERIGO DE INVASÃO'

    return acrescimoDinamico, statusFaixaEsq, statusFaixaDir


def decisaoFinal(x,y,z):

    statusFrontal = x
    faixaEsq = y
    faixaDir = z
    statusGeral = 'NORMAL'

    if statusFrontal == 'RISCO DE COLISÃO' or faixaEsq == 'PERIGO DE INVASÃO' or faixaDir == 'PERIGO DE INVASÃO':
        statusGeral = 'INTERVENÇÃO CRITICA EXIGIDA'
        return statusGeral
    elif statusFrontal == 'ATENÇÃO' or faixaEsq == 'ATENÇÃO' or faixaDir == 'ATENÇÃO':
        statusGeral = 'ATENÇÃO'
        return statusGeral
    else:
        return statusGeral


#valores para "Modos de condução e distância segura"
velocidadeAtual = float(input('Velocidade do veículo atual (km/h): ')) #1


velocidadeFrente = float(input('Velocidade do veículo à frente (km/h): ')) #2

#valores para "Fusão de Sensores"
radar = float(input('Leitura do sensor radar (ondas de rádio) (metros): ')) #3
lidar = float(input('Leitura do sensor lidar (pulsos de luz laser) (metros): ')) #4
camera = float(input('Leitura do sensor câmera (metros): ')) #5

#valores para "Modos de condução e distância segura"
atritoVia = float(input('Atrito da via (ex: 0.8 para pista seca, 0.4 para pista molhada, 0.25 baixa aderência): ')) #6
nivelADAS = int(input('Nível de sensibilidade ADAS (1 = esportivo, 2 = normal, 3 = seguro): ')) #7

distFaixaEsq = float(input('Distância da faixa esquerda (metros): ')) #8
distFaixaDir = float(input('Distância da faixa direita (metros): ')) #9

#atribui valor da função em uma variavel para impressão
mediana = FusaoDeSensores(radar, lidar, camera)


#atribui os valores da função a uma variavel para impressão
distanciaSegura = CalcDistanciaSegura(velocidadeAtual, nivelADAS, atritoVia)

#atribui os valores da função a uma variavel para impressão
statusFrontal = anlsColisaoFrontal(velocidadeAtual, velocidadeFrente, distanciaSegura, valorMeio)

#estado padrão do AEB
aeb = 'não acionado'

#estado AEB caso haja risco de colisão da função statusFrontal
if statusFrontal == 'RISCO DE COLISÃO':
    aeb = 'ACIONADO'

#atribui os valores do return a 3 variaveis identificadas como margemExigida, faixaEsquerda, faixaDireita para representação individual de cada return
margemExigida, faixaEsquerda, faixaDireita = assFaixaDinamico(velocidadeAtual, distFaixaEsq, distFaixaDir)


#imprime a mediana, e de acordo com a doc, a "Distância Validada"
print(f'Distância validada: {mediana} m')

#imprime a "Distância segura" com base no calculo de acordo com a doc
print(f'Distância segura: {distanciaSegura:.2f} m')

#imprime o "Status frontal" com base na função "anlsColisaoFrontal"
print(f'Status frontal: {statusFrontal}')

#imprime o "AEB" com base na função "anlsColisaoFrontal"
print(f'AEB: {aeb}')

#imprime a "Margem lateral exigida" com base na função "assFaixaDinamico"
print(f'Margem lateral exigida: {margemExigida:.2f}M')

#imprime a "Faixa esquerda" com base na função "assFaixaDinamico"
print(f'Faixa esquerda: {faixaEsquerda}')

#imprime a "Faixa direita" com base na função "assFaixaDinamico"
print(f'Faixa direita: {faixaDireita}')


print(f'STATUS GERAL: {decisaoFinal(statusFrontal, faixaEsquerda, faixaDireita)}')
