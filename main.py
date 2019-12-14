import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
fig, ax = plt.subplots()
redDot, = plt.plot(0, 0, 'ro')
x, y = 0, 0
velx, vely = 0, 0
accx, accy = 0, 0
posIn, posInx, posIny = 0, 0, 0
print("1: Moto Rettilineo Uniforme \n2: Moto Uniformemente Accelerato")
moto = input("Che moto vuoi rappresentare? ")
if moto == "1":
    velx = int(input("Velocità iniziale: "))
    posIn = int(input("Posizione iniziale: "))
    tempo = int(input("Tempo: "))
    ax = plt.axis([0,velx*tempo+x+2,0,max(vely*tempo+y, 5)])
    x = posIn
    print("La posizione finale è " + str(velx*tempo+x) + " e il corpo ha quindi percorso " + str(velx*tempo))
    def animate(i):
        global x, y, velx, tempo, posIn
        x += velx/30
        if x >= velx*tempo:
            x = velx*tempo 
        redDot.set_data(x, y)
        return redDot,
if moto == "2":
    xy = input("Vuoi attuarlo sull'asse X o sull'asse Y? ")
    if xy=="y" or xy=="Y":
        vely = int(input("Velocità iniziale: "))
        accy = input("Accelerazione: ")
        if accy=="g" or accy=="G":
            accy=-9.81
        else:
            accy=int(accy)
        posIny = int(input("Posizione iniziale: "))
    else:
        velx = int(input("Velocità iniziale: "))
        accx = int(input("Accelerazione: "))
        posInx = int(input("Posizione iniziale: "))
    tempo = int(input("Tempo: "))
    posfinx = posInx+velx*tempo+0.5*accx*tempo*tempo
    posfiny = posIny+vely*tempo+0.5*accy*tempo*tempo
    if posfinx>0 or posfiny>0:
        ax = plt.axis([0,posfinx+2,0,posfiny+2],option="equal")
    else: ax = plt.axis([posfinx-2,0,posfiny-2,0])
    if xy=="y" or xy=="Y":
        y = posIny
        print("\n\nLa posizione finale è " + str(posfiny) + " e il corpo ha quindi percorso " + str(posfiny-posIn))
    else: 
        x = posInx
        print("\n\nLa posizione finale è " + str(posfinx) + " e il corpo ha quindi percorso " + str(posfinx-posIn))
    redDot.set_data(x, y)
    def animate(i):
        global x, y, velx, vely, tempo, posIn, accx, accy, xy
        x += velx/30
        y += vely/30
        if posfinx>0 or posfiny>0:
            if (xy=="y" or xy=="Y") and y >= posfiny:
                y = posfiny
            elif (xy=="x" or xy=="X") and x >= posfinx:
                x = posfinx
        else:
            if (xy=="y" or xy=="Y") and y <= posfiny:
                y = posfiny
            elif (xy=="x" or xy=="X") and x <= posfinx:
                x = posfinx            
        velx += accx/30
        vely += accy/30
        redDot.set_data(x, y)
        return redDot,

if moto == "3":
    x = int(input("Posizione iniziale sull'asse X: "))
    y = int(input("Posizione iniziale sull'asse Y: "))
    velx = int(input("Velocità sull'asse X: "))
    vely = int(input("Velocità sull'asse Y: "))
    accx = int(input("Accelerazione sull'asse X: "))
    accy = int(input("Accelerazione sull'asse Y: "))
    tempo = int(input("Per quanto tempo dura il moto: "))
    xin, yin, velxin, velyin = x, y, velx, vely
    def animate(i):
        global x, y, velx, vely, tempo, accx, accy
        x += velx/30
        y += vely/30
        velx += accx/30
        vely += vely/30
        if x>=xin+velxin*tempo+0.5*accx*tempo*tempo and y>=yin+velyin*tempo+0.5*accy*tempo*tempo:
            redDot. set_data(xin+velxin*tempo+0.5*accx*tempo*tempo, yin+velyin*tempo+0.5*accy*tempo*tempo)
        elif x>=xin+velxin*tempo+0.5*accx*tempo*tempo:
            redDot.set_data(xin+velxin*tempo+0.5*accx*tempo*tempo, y)
        elif y>=yin+velyin*tempo+0.5*accy*tempo*tempo:
            redDot.set_data(x, yin+velyin*tempo+0.5*accy*tempo*tempo)
        else: 
            redDot.set_data(x, y)
        return redDot,

myAnimation = animation.FuncAnimation(fig, animate, \
                                      interval=10, blit=True, repeat=True)

plt.show()