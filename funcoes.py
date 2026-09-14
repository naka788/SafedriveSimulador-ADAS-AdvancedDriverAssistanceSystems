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
    status = 'seguro'
    if veloRelativa <= float(0):
        return status, 'não acionado'
    elif distanciaValidada >= distanciaSegura:
        return status, 'não acionado'
    elif distanciaValidada < distanciaSegura and distanciaValidada >= (distanciaSegura / 2):
        status = 'atenção'
        return status, 'não acionado'
    else:
        status = 'risco de colisão (AEB - Frenagem Automática de Emergência acionado)'
        return status, 'ACIONADO'

def assFaixaDinamico(x,y,z):
    velocidadeAtual = x
    distFaixaEsq = y
    distFaixaDir = z
    margemBase = float(0.50)
    acrescimoDinamico = float(0)
    margemSeguranca = float(0.20)

    if velocidadeAtual > 80:
        acrescimoDinamico = ((velocidadeAtual - 80) / 1000) + margemBase


    if distFaixaEsq < (acrescimoDinamico + margemSeguranca):

        if distFaixaDir < (acrescimoDinamico + margemSeguranca):
            return acrescimoDinamico, 'atenção', 'atenção'

        elif distFaixaDir < acrescimoDinamico:
            return acrescimoDinamico, 'atenção', 'perigo de invasão'

        else:
            return acrescimoDinamico, 'atenção', 'normal'    


    elif distFaixaEsq < acrescimoDinamico:

        if distFaixaDir < (acrescimoDinamico + margemSeguranca):
            return acrescimoDinamico, 'perigo de invasão', 'atenção'

        elif distFaixaDir < acrescimoDinamico:
             return acrescimoDinamico, 'perigo de invasão', 'perigo de invasão'
        else:
            return acrescimoDinamico, 'perigo de invasão', 'normal'


    elif distFaixaDir < (acrescimoDinamico + margemSeguranca):
        return acrescimoDinamico, 'normal', 'atenção'

    elif distFaixaDir < acrescimoDinamico:
        return acrescimoDinamico, 'normal', 'perigo de invasão'
    else:
        return acrescimoDinamico, 'normal', 'normal' 