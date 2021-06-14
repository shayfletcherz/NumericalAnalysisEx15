import sympy as sp
from sympy.utilities.lambdify import lambdify

#חישוב נגזרת
def calcDerivative(function):
    x = sp.symbols('x')
    f_prime = function.diff(x)
    return f_prime

#חישוב סימפסון לערך השטח באינטגרל
def simpson(function, startPoint, endPoint, parts):
    if parts % 2 == 1:
        print("Amount of parts is not even.")
        return None
    x = sp.symbols('x')
    func = lambdify(x, function)
    gap = abs(endPoint - startPoint) / parts
    appr = func(startPoint)
    for i in range(1, parts):
        if i % 2 == 0:
            appr += 2 * func((i * gap) + startPoint)
        else:
            appr += 4 * func((i * gap) + startPoint)
    appr += func(endPoint)
    appr *= 1 / 3 * gap
    return appr


def rombergMethod(function, startPoint, endPoint, limit, epsilon):
    results = [[0 for i in range(limit + 1)] for j in range(limit + 1)]
    for k in range(0, limit):
        res = trapezMethod(function, startPoint, endPoint, 2 ** k)
        results[k][1] = res
    for j in range(2, limit + 1):
        for k in range(2, limit + 1):
            results[k][j] = results[k][j - 1] + (
                        (1 / ((4 ** (j - 1)) - 1)) * (results[k][j - 1] - results[k - 1][j - 1]))
            if abs(results[k][j] - results[k - 1][j]) < epsilon:
                return results[k][j]


def trapezMethod(function, startPoint, endPoint, segments):
    x = sp.symbols('x')
    function = lambdify(x, function)
    h = (endPoint - startPoint) / segments
    sum = 0
    while startPoint < endPoint:
        sum += 0.5 * ((startPoint + h) - startPoint) * (function(startPoint) + function(startPoint + h))
        startPoint += h
    return sum




def driver():
    x = sp.symbols('x')
    f =
    epsilon = 0.00001
    startRange = -0.4
    endRange = 0.4
    print("Simpson method:")
    print(simpson(f, startRange, endRange, 6))
    print("Romberg Method")
    print(rombergMethod(f, startRange, endRange, 5, epsilon))

driver()