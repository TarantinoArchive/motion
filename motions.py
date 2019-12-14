import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
redDot, = plt.plot(0, 0, 'ro') # Disegno il Punto Materiale

x = int(input("Posizione iniziale sull'asse X: ")) # Chiedo la Posizione Iniziale sull'asse X
y = int(input("Posizione iniziale sull'asse Y: ")) # Chiedo la Posizione Iniziale sull'asse Y
velx = int(input("Velocità sull'asse X: ")) # Chiedo la Velocità Iniziale sull'asse X
vely = int(input("Velocità sull'asse Y: ")) # Chiedo la Velocità Iniziale sull'asse Y
accx = int(input("Accelerazione sull'asse X: ")) # Chiedo l'accelerazione sull'asse X
accy = -9.8
tempo = int(input("Per quanto tempo dura il moto: ")) # Chiedo la durata del moto
# Formula per calcolare posizione finale: S0+V0*T+0.5*A*T*T
posFinX = x+velx*tempo+0.5*accx*tempo*tempo # Calcolo la posizione finale di X
posFinY = y+vely*tempo+0.5*accy*tempo*tempo
maxY = y+vely*vely/2*9.8
if posFinY < 0: posFinY = 0 # Calcolo la posizione finale di Y
if x>=0 and y>=0:  # Adatto la dimensione degli assi a seconda delle posizioni iniziali e finali
    ax = plt.axis([x-5, posFinX+5, 0, maxY])
elif x<0 and y>=0:
    ax = plt.axis([posFinX-5, x+5, 0, maxY])
elif x>=0 and y<0:
    ax = plt.axis([x-5, posFinX+5, 0, maxY])
elif x<0 and y<0:
    ax = plt.axis([posFinX-5, x+5, 0, maxY])
else:
    ax = plt.axis([-500, 500, -500, 500]) # Caso che non dovrebbe succere, ma in caso di problemi si attiva questo
def animate(i):
    global x, y, velx, vely, tempo, accx
    if x < posFinX and y!=0: x += velx/30 # Aggiungo ad X un valore pari alla sua velocità attuale
    if y > 0 and y+vely/30>0: 
        y += vely/30
    elif y > 0 and y+vely/30<0:
        y = 0  # Aggiungo ad Y un valore pari alla sua velocità attuale, controllando che non vada a superare lo 0
    velx += accx/30  # Aggiungo l'accelerazione alla velocità 
    vely -= 9.8/30 # Sottraggo alla velocità attuale il valore g
    redDot.set_data(x, y) # Setto infine la posizione del punto
    return redDot,

myAnimation = animation.FuncAnimation(fig, animate, \
                                    interval=10, blit=True, repeat=True)
print('La posizione iniziale sulla X è: ' + str(x))
print('La posizione iniziale sulla X è: ' + str(y))

plt.show()