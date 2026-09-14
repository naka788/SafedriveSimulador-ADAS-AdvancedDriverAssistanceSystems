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
