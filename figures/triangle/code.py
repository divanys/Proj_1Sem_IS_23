_a = 7
_b = 2
_c = 8


def triangle_perimetr(a=_a, b=_b, c=_c):
    return a + b + c


def triangle_area(a=_a, b=_b, c=_c):
    p = (triangle_perimetr()) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)