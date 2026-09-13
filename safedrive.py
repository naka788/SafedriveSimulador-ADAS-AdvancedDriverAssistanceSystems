import funcoes


velocidadeAtual = float(input('Velocidade do veículo atual (km/h): ')) #1
velocidadeFrente = float(input('Velocidade do veículo à frente (km/h): ')) #2

#valores para "Fusão de Sensores"
radar = float(input('Leitura do sensor radar (ondas de rádio) (metros): ')) #3
lidar = float(input('Leitura do sensor lidar (pulsos de luz laser) (metros): ')) #4
camera = float(input('Leitura do sensor câmera (metros): ')) #5

atritoVia = float(input('Atrito da via (ex: 0.8 para pista seca, 0.4 para pista molhada, 0.25 baixa aderência): ')) #6

#valor para "Modos de condução e distância segura"
nivelADAS = int(input('Nível de sensibilidade ADAS (1 = esportivo, 2 = normal, 3 = seguro): ')) #7

distFaixaEsq = float(input('Distância da faixa esquerda (metros): ')) #8
distFaixaDir = float(input('Distância da faixa direita (metros): ')) #9


#atribui os valores do return a 3 variaveis identificadas por começo, meio e fim.
valorComeço, valorMeio, valorFim = funcoes.FusaoDeSensores(radar, lidar, camera)

#imprimi a mediana, e de acordo com a doc, a "Distância Validada"
print(f'Distância validada: {valorMeio} M')
