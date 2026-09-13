def FusaoDeSensores(x,y,z):
    #ordena em crescente os valores
    if x < y:
        if x < z:
            if y < z:
                return x, y, z
            else:
                return x, z, y
        else:
            return z, x, y
    else:
        if x > z:
            if z > y:
                return y, z, x
            else:
                return z, y, x
        else:
            return y, x, z


    


"""    
Organize os dados: Coloque os números do menor para o maior (ou do maior para o menor). [1] 

Conte a quantidade de elementos: Veja se o total de números no conjunto é ímpar ou par.

Se a quantidade for ímpar: A mediana é exatamente o número que fica no meio da lista.

Se a quantidade for par: A mediana é a média aritmética dos dois números centrais (some os dois do meio e divida por 2)
"""