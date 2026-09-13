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

