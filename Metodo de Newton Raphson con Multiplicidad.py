# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

Metodo de Newton Raphson con Multiplicidad
"""

from pylab import *
from tabulate import tabulate

def newtonRaphson(f, fprima, x0, tolerance, max_iterations, d):
    xi = float(x0)
    iterations = 0
    ea = 100  # Error relativo inicial arbitrariamente grande
    
    tabla = [['i', 'xi', 'ea'], [iterations, xi, ea]]
    
    while ea > tolerance and iterations < max_iterations:
        
        x = xi
        fxi = eval(f)
        fprimaxi = eval(fprima)
        
        if abs(fprimaxi) < 1e-10:
            print("La derivada se aproxima a cero. No se puede continuar.")
            return None
        
        xii = xi - fxi / fprimaxi
        
        ea = abs((xii - xi) / xii) * 100
        iterations += 1
        
        fila = [iterations, xii, ea]
        redondeados = [round(elemento, d) for elemento in fila]
        tabla.append(redondeados)
        
        xi = xii
    
    if iterations >= max_iterations:
        print("El método no convergió después de {} iteraciones.".format(max_iterations))
    
    print(tabulate(tabla, headers="firstrow"))
    return xi

# Aplicación del método de Newton-Raphson
# newtonRaphson("f(x)", "fprima(x)", x0, tolerance, max_iterations, d)

# Polinomio 1
# newtonRaphson("-48+(208*x)-(288*x**2)+(108*x**3)+(27*x**4)", "208-(576*x)+(324*x**2)+(108*x**3)", 0.65, 20, 4)

# Polinomio 2
# newtonRaphson("144 + 192*x + 40*x**2 - 40*x**3 - 15*x**4 + 2*x**5 + x**6", "192 + 80*x - 120*x**2 - 60*x**3 + 10*x**4 + 6*x**5", -2.1, 20, 4)
# newtonRaphson("144 + 192*x + 40*x**2 - 40*x**3 - 15*x**4 + 2*x**5 + x**6", "192 + 80*x - 120*x**2 - 60*x**3 + 10*x**4 + 6*x**5", 2.9, 20, 4)