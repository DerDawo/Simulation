import agent as ag
import environment as em
import virus as vi

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.animation
import numpy as np
import random
import math

figure(figsize=(8,8), dpi=100)

agents = []
agentsX = []
agentsY = []

#eigenschaften des Virus
covid19 = vi.virus("Sars-Cov-2",1.5,0.5,5,14,0.1)

#initialisere Umgebung
environment1 = em.enviroment("Test-City",10,10,100,1,False,False,False) 

positions = []

#initialisiere alle Positionen
for i in range(environment1.xDimension):
    for j in range(environment1.yDimension):
        pos = ag.position(i-0.5,j-0.5)
        positions.append(pos)

#Arrays für Plot
for i in range(environment1.populationAmmount):
    agentsX.append(positions[i].x)
    agentsY.append(positions[i].y)

agentsDir = []
for i in range(environment1.populationAmmount):
    direction = ag.position(math.sin(random.random()*2*math.pi)/1000,math.cos(random.random()*2*math.pi)/1000)
    agentsDir.append(direction)

#Initialisere alle Agenten (Alle sind Anfangs susceptible)
for j in range(environment1.populationAmmount):
    agent = ag.agent(j,positions[j],True,False,False)
    agents.append(agent)


#Wähle den ersten erkrankten aus
FIID = np.random.randint(0,environment1.populationAmmount)
agents[FIID].isSusceptible=False
agents[FIID].isInfected=True
firstill=agents[FIID]

fig, ax = plt.subplots()
plt.xlim(0, environment1.xDimension)
plt.ylim(0, environment1.yDimension)

#Größe der Marker
plt.plot(markersize=10)
#zeichne alle Agenten ein
plt.xlabel("Position X")
plt.ylabel("Position Y")
sc = ax.scatter(agentsX, agentsY, c="blue")

def animate(i):

    for k in range(environment1.populationAmmount):
        agents[k].move(agentsDir[k])

        agentsX[k] += (agents[k].position.x)
        agentsY[k] += (agents[k].position.y)

    sc.set_offsets(np.c_[agentsX,agentsY])


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=25, interval=1000, repeat=True) 

plt.show()

plt.show()
