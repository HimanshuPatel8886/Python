def divides(m, n):
    if n % m == 0:
        return True
    else:
        return False


def evenNum(n):
    return divides(2, n)


def oddNum(n):
    return not divides(2, n)


