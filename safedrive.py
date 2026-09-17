import funcoes

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


#atribui os valores do return a 3 variaveis identificadas por começo, meio e fim para representação apenas de um dos valores do return
valorComeço, valorMeio, valorFim = funcoes.FusaoDeSensores(radar, lidar, camera)


#atribui os valores do return a uma variavel para poder ser reutilizado na impressao da analise de colisão frontal
distanciaSegura = funcoes.CalcDistanciaSegura(velocidadeAtual, nivelADAS, atritoVia)

#atribui os valores do return a 2 variaveis identificadas como status frontal e aeb para representação individual de cada return
statusFrontal, aeb = funcoes.anlsColisaoFrontal(velocidadeAtual, velocidadeFrente, distanciaSegura, valorMeio)

#atribui os valores do return a 3 variaveis identificadas como margemExigida, faixaEsquerda, faixaDireita para representação individual de cada return
margemExigida, faixaEsquerda, faixaDireita = funcoes.assFaixaDinamico(velocidadeAtual, distFaixaEsq, distFaixaDir)


#imprime a mediana, e de acordo com a doc, a "Distância Validada"
print(f'Distância validada: {valorMeio} m')

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


print(f'STATUS GERAL: {funcoes.decisaoFinal(statusFrontal, faixaEsquerda, faixaDireita)}')
