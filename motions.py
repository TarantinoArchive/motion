import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import radians as r
import math

fig, ax = plt.subplots()
redDot, = plt.plot(0, 0, 'ro') # Disegno il Punto Materiale

x = float(input("Posizione iniziale sull'asse X: ")) # Chiedo la Posizione Iniziale sull'asse X
y = float(input("Posizione iniziale sull'asse Y: ")) # Chiedo la Posizione Iniziale sull'asse Y
vel = float(input("Velocità iniziale: "))
angolo = float(input("Angolo della velocità: "))
velx = vel*math.cos(r(angolo)) # Chiedo la Velocità Iniziale sull'asse X
vely = vel*math.sin(r(angolo)) # Chiedo la Velocità Iniziale sull'asse Y
accx = 0 # Chiedo l'accelerazione sull'asse X
accy = -9.81
tempo = velx/9.81*2 # Chiedo la durata del moto
# Formula per calcolare posizione finale: S0+V0*T+0.5*A*T*T
posFinX = x+velx*tempo # Calcolo la posizione finale di X
posFinY = 0
tmax = vely/9.81
maxY = vely*tmax+0.5*accy*tmax*tmax
maxX = velx*tmax*2
if x>=0 and y>=0:  # Adatto la dimensione degli assi a seconda delle posizioni iniziali e finali
    ax = plt.axis([x-5, posFinX+5, 0, 50])
elif x<0 and y>=0:
    ax = plt.axis([posFinX-5, x+5, 0, 50])
elif x>=0 and y<0:
    ax = plt.axis([x-5, posFinX+5, 0, 50])
elif x<0 and y<0:
    ax = plt.axis([posFinX-5, x+5, 0, 50])
else:
    ax = plt.axis([-500, 500, -500, 500]) # Caso che non dovrebbe succere, ma in caso di problemi si attiva questo
def animate(i):
    global x, y, velx, vely, tempo, accx
    if x < posFinX and y!=0: x += velx/30 # Aggiungo ad X un valore pari alla sua velocità
    if y+vely/30<0:
        y = 0 
    elif y >= 0: 
        y += vely/30
     # Aggiungo ad Y un valore pari alla sua velocità attuale, controllando che non vada a superare lo 0
    vely -= 9.81/30 # Sottraggo alla velocità attuale il valore g
    redDot.set_data(x, y) # Setto infine la posizione del punto
    return redDot,

myAnimation = animation.FuncAnimation(fig, animate, \
                                    interval=10, blit=True, repeat=True)
print('La posizione finale sulla X è: ' + str(round(maxX, 2)))
print('La posizione più alta sulla Y è: ' + str(round(maxY, 2)))

plt.show()