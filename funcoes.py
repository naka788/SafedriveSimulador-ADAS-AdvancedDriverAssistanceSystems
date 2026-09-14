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
        return status
    elif distanciaValidada >= distanciaSegura:
        return status
    elif distanciaValidada < distanciaSegura and distanciaValidada >= (distanciaSegura / 2):
        status = 'atenção'
        return status
    else:
        status = 'risco de colisão (AEB - Frenagem Automática de Emergência acionado)'
        return status
