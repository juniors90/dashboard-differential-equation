# El objetivo es resolver la ecuoación diferencial
#
# y' = 2y -5sen(t)
# y_0=1
#
# usando el método de Euler
# Vamos a resolver entre = y T, dejand T coo parámetro a variar
import numpy as np
import matplotlib.pyplot as plt

def y_prima(t,y):
    return 2*y-5*np.sin(t)

def euler():
    T=np.pi/2     # Tiempo máximo a resolver
    N=100         # Cantidad de iteraciones
    dt=T/N
    t_exact = np.arange(0,T,dt)
    y_exact = 2*np.sin(t_exact) + np.cos(t_exact)
    y = [1]   # Empiezo en Cero
    t = [0]   # Empiezo en 1 por la condicón inicial
    while t[-1] <= T:
        y_new = y[-1] + y_prima(t[-1],y[-1])*dt
        t_new =  t[-1] + dt
        y.append(y_new)
        t.append(t_new)
    # 
    # t[-1] el último elemento de la lista T
    plt.plot(t,y,label='Euler')
    plt.plot(t_exact,y_exact,label='Exacta')
    plt.legend()
    plt.savefig('euler_exacta.jpg')
    return plt.plot(t,y,label='Euler'), plt.plot(t_exact,y_exact,label='Exacta')

if __name__=='__main__':
    euler()


      