# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
13/07/2023

Metdo de Biseccion
"""
from pylab import *
from tabulate import tabulate

# biseccion("sin(x)-x**2",0.8,0.9,10,4)

def biseccion (f,a,b,n,d):
    """La funcion implementa el metodo de biseccion para calcular 
    la raiz de la funcion f en el intervalo [a,b] con n interaciones 
    y redondeandoa d decimales"""
    
    xi = float(a); xs = float(b)
    #Convierte el entero a numero de punto flotante o con decimales
    # ; es cambio de linea
    
    x = xi
    fa = eval(f) #Guardar en 'a' mi funcion evaluada en a
    
    x = xs
    fb = eval(f)
    
# Esta es la evalucion de cambio de signo
    if fa*fb > 0:
        return "No se cumple con la condicion de cambio de signo"
   
    elif fa*fb == 0:
        return "Uno de los extremos del intervalo es una raiz"
    
    tabla = [['i','xi','xs','xr','ea'],]
    # --------- TITULO DE LA TABLA
    # i = iteracion,              ea = error aproximado

    fila = []
    
    ea = float(0)
    
    xr = (xi + xs)/2
    
    for i in range(n):
        
    #Evaluamos el XR
        
        fila = [i,xi,xs,xr,ea]
        redondeados = []
        
#        for i in range(5):
#            redondeados.append(round(fila(i)))

#La funcion de arriba y abajo hacen lo mismo         
   
        for elementos in fila:
            redondeados.append(round(elementos,d))
            
        tabla.append(redondeados) #Mete 'redondeados' a 'fila'
        
        x = xi
        fxi = eval(f)
        
        x = xr
        fxr = eval(f)
        
        
    #Cuando si hay cambio de signo en el lado de xi para xr ... xs = xr
        if fxi*fxr < 0:
            xs = xr
            
        elif fxi*fxr == 0:
            break 
        #El break termina el ciclo FOR
        
    #Si el cambio de signo esta del otro lado entre xr y xs ... xi = xr
        else:
            xi = xr
            
        xrant = xr
        
        xr = (xi + xs)/2
        
        ea = abs((xr - xrant)/xrant)*100
        
    print (tabulate(tabla))
    
# Proyecto 1

# Ec. de Van der Waals
# biseccion("20000*x**(3) - 344.4667*x**(2) + 1.7042*x - 2.8807*10**(-3)", 0.015, 0.0155, 10, 4)

# Ec. de Hooke no lineal
# biseccion("2 * 3 + 0.5*x*(3) - 7",0.5,2,10,4)

# Ec. de Torque de Motor de Corriente Continua
# biseccion("0.21*x**(2) + 0.1*x - 0.05 - 1.5", 2, 4, 10, 4)

# Ec. de Fricción de Coulomb
# biseccion("0.3*15*sign(x)*(abs(x))**(1/2)+0.02*x**2",-37,-36,10,4)

# Ecuacion de Corriente que Pasa a travez de un Diodo
# biseccion("5 * 1e-12 * math.exp(x / (1.8 * 25 * 1e-3)) - 1 - 5 * 1e-6",1.1,1.2,20,4)