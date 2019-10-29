def é_hipotenusa(n):
    cont = 0
    a = 1
    b = n - 1
    while b > 0:
        while a < n:
            c = (a**2) + ((b)**2)
            if c == n**2:
                cont = 1
                a = a + 1
            else:
                a = a + 1
        b = b - 1
        a = 1
    if cont > 0:
        return True
    else:
        return False


def soma_hipotenusas (a):
    b = 1
    c = 0
    while b <= a:
        if é_hipotenusa(b) == True:
            c = b + c
            b = b + 1
        else:
            b = b + 1
    return c


