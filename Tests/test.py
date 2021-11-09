import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math
import random
import agent as ag
import environment as env

env1 = env.environment("Env1",100,100,100,0.5,False,False,False)

#Agenten
agentList = []
for i in range(env1.populationAmmount):
    xPos = random.random()*env1.xDimension
    yPos = random.random()*env1.yDimension
    agentList.append(ag.agent(i,ag.position(xPos,yPos),True,False,False))

print(len(agentList))

#Koordinaten für Animation
x = []
y = []

#SetzeKoordinaten
def setXandY():
    if(len(x)==env1.populationAmmount):
        for i in range(env1.populationAmmount):
            x[i] = agentList[i].position.x
            y[i] = agentList[i].position.y
    else:
        for i in range(env1.populationAmmount):
            x.append(agentList[i].position.x)
            y.append(agentList[i].position.y)
         
setXandY()

fig, ax = plt.subplots()
sc = ax.scatter(x,y,color="blue")

#Richtung
direction = []
for i in range(100):
    a = random.random()*2*math.pi
    b = random.random()*2*math.pi
    direction.append(ag.position((math.sin(a))/10,(math.cos(b))/10,))

plt.xlim(0,env1.xDimension)
plt.ylim(0,env1.yDimension)
plt.xlabel("Position X")
plt.ylabel("Position Y")
plt.title(env1.name)

def animate(i):
    for i in range(env1.populationAmmount):
        agentList[i].move(direction[i],env1.xDimension,env1.yDimension)
    
    setXandY()

    sc.set_offsets(np.c_[x,y])

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=25, interval=10, repeat=True) 
plt.show()