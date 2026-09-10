def FusaoDeSensores():
    radar = float(input('Leitura do sensor radar (ondas de rádio) (metros): '))
    lidar = float(input('Leitura do sensor lidar (pulsos de luz laser) (metros): '))
    camera = float(input('Leitura do sensor câmera (metros): '))

def ordenarCrescente(x,y,z):
    if x > y and x > z:
        if y > z:
            return x, y, z
        else:
            return x, z, y
    elif y > z:
        if z > x:
            return y, z, x
    else:
        return z, x, y

print(ordenarCrescente(1,2,3))

"""    
Organize os dados: Coloque os números do menor para o maior (ou do maior para o menor). [1] 

Conte a quantidade de elementos: Veja se o total de números no conjunto é ímpar ou par.

Se a quantidade for ímpar: A mediana é exatamente o número que fica no meio da lista.

Se a quantidade for par: A mediana é a média aritmética dos dois números centrais (some os dois do meio e divida por 2)
"""