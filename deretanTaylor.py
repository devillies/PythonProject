# mencari turunan 1 aksen dan 2 aksen menggunakan deretan taylor
def X(x):
    return 0.25*(x**3) + 0.5*(x**2) + 0.25*x + 0.5


def Y(y0, y1, y2, yaf2, ybf0):
    resultMundur = (y1 - y0) / 0.5
    resultMaju = (y2-y1)/0.5
    resultTerpusat = (y2-y0)/(2*0.5)
    resultAksen1 = [resultMundur, resultMaju, resultTerpusat]
    resultDoubleMundur = (ybf0-(2*y0)+y1)/(0.5**2)
    resultDoubleMaju = (yaf2 - (2*y2)+y1)/(0.5**2)
    resultDoubleTerpusat = (y0 - (2*y1)+y2)/(0.5**2)
    resultAksen2 = [resultDoubleMundur, resultDoubleMaju, resultDoubleTerpusat]
    return 'hasil deretan taylor f1:', resultAksen1, 'hasil deretan taylor f2:', resultAksen2


print(Y(X(0), X(0.5), X(1), X(1.5), X(-0.5)))
