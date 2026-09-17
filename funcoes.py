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
        return status, 'não acionado'
    elif distanciaValidada >= distanciaSegura:
        return status, 'não acionado'
    elif distanciaValidada < distanciaSegura and distanciaValidada >= (distanciaSegura / 2):
        status = 'ATENÇÃO'
        return status, 'não acionado'
    else:
        status = 'RISCO DE COLISÃO'
        return status, 'ACIONADO'

def assFaixaDinamico(x,y,z):
    velocidadeAtual = x
    distFaixaEsq = y
    distFaixaDir = z
    margemBase = float(0.50)
    acrescimoDinamico = float()
    margemSeguranca = float(0.20)

    if velocidadeAtual > 80:
        acrescimoDinamico = (0.01 * (velocidadeAtual - 80)) + margemBase
    else:
        acrescimoDinamico = margemBase

    if distFaixaEsq < (acrescimoDinamico + margemSeguranca):

        if distFaixaDir < (acrescimoDinamico + margemSeguranca):
            return acrescimoDinamico, 'ATENÇÃO', 'ATENÇÃO'

        elif distFaixaDir < acrescimoDinamico:
            return acrescimoDinamico, 'ATENÇÃO', 'PERIGO DE INVASÃO'

        else:
            return acrescimoDinamico, 'ATENÇÃO', 'NORMAL'    


    elif distFaixaEsq < acrescimoDinamico:

        if distFaixaDir < (acrescimoDinamico + margemSeguranca):
            return acrescimoDinamico, 'PERIGO DE INVASÃO', 'ATENÇÃO'

        elif distFaixaDir < acrescimoDinamico:
             return acrescimoDinamico, 'PERIGO DE INVASÃO', 'PERIGO DE INVASÃO'
        else:
            return acrescimoDinamico, 'PERIGO DE INVASÃO', 'NORMAL'


    elif distFaixaDir < (acrescimoDinamico + margemSeguranca):
        return acrescimoDinamico, 'NORMAL', 'ATENÇÃO'

    elif distFaixaDir < acrescimoDinamico:
        return acrescimoDinamico, 'NORMAL', 'PERIGO DE INVASÃO'
    else:
        return acrescimoDinamico, 'NORMAL', 'NORMAL' 


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
