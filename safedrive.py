import funcoes

#pede valores para a primeira "regra"
radar = float(input('Leitura do sensor radar (ondas de rádio) (metros): '))
lidar = float(input('Leitura do sensor lidar (pulsos de luz laser) (metros): ')) 
camera = float(input('Leitura do sensor câmera (metros): '))

#atribui os valores do return a 3 variaveis identificadas por começo, meio e fim.
valorComeço, valorMeio, valorFim = funcoes.FusaoDeSensores(radar, lidar, camera)

#imprimi a mediana, e de acordo com a doc, a "Distância Validada"
print(f'Distância validada: {valorMeio} M')
