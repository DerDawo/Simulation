import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math
import random
import agent as ag
import environment as env
import virus as vir

class simulation:
    def __init__(self,Virus,Environment):
        self.Virus = Virus
        self.Environment = Environment
        self.stateList = self.__setStates()
        self.colorList = self.__setColors()
        self.agentList = self.__generateAgents()
        self.xCoordinates, self.yCoordinates = self.__setCoordinates()
        self.direction = self.__setDirections()
        self.duration = 1
        self.extinctDiseas = False
        self.SusAmmountList = []
        self.InfAmmountList = []
        self.RemAmmountList = []
        self.TimeList = []
        self.TimeCounter = 0

    #generiere Agenten mittels der Populationsanzahl der Enviornment
    def __generateAgents(self):
        agList = []
        for i in range(self.Environment.populationAmmount):
            xPos = random.random()*self.Environment.xDimension
            yPos = random.random()*self.Environment.yDimension
            if(self.stateList[i] == "s"):
                agList.append(ag.agent(i,ag.position(xPos,yPos),True,False,False))
            elif(self.stateList[i] == "i"):
                agList.append(ag.agent(i,ag.position(xPos,yPos),False,True,False))
            elif(self.stateList[i] == "r"):
                agList.append(ag.agent(i,ag.position(xPos,yPos),False,False,True))
        return agList

    #Setze die Koordinaten der Agenten in einen x- und y- Array fest
    def __setCoordinates(self):
        xCoor = []
        yCoor = []
        for i in range(self.Environment.populationAmmount):
            xCoor.append(self.agentList[i].position.x)
            yCoor.append(self.agentList[i].position.y)
        return xCoor, yCoor

    #Update die Koordianten der Agenten
    def __updateCoordinates(self):
        for i in range(self.Environment.populationAmmount):
            self.xCoordinates[i] = self.agentList[i].position.x
            self.yCoordinates[i] = self.agentList[i].position.y

    #Weise den Agente eine Richtung zu, welche in einem Array gespeichert wird
    def __setDirections(self):
        dir=[]
        for i in range(self.Environment.populationAmmount):
            a = random.random()*2*math.pi
            b = random.random()*2*math.pi
            dir.append(ag.position((math.sin(a))/10,(math.cos(b))/10,))
        return dir

    #Weise jedem Agenten den Susceptiblestatus zu und einem den infected Status
    def __setStates(self):
        states = []
        infect = int(random.random()*self.Environment.populationAmmount)
        for i in range(self.Environment.populationAmmount):
            if(i==infect):
                states.append("i")
            else:
                states.append("s")
        return states

    #Weise jedem Agenten entsprechend seines Status eine Farbe zu
    def __setColors(self):
        colors = []
        for i in range(self.Environment.populationAmmount):
            if(self.stateList[i]=="s"):
                colors.append("blue")
            elif(self.stateList[i]=="i"):
                colors.append("red")
            elif(self.stateList[i]=="r"):
                colors.append("green")
        return colors

    #Update den Status der Agenten
    def __updateStates(self):
        for i in range(self.Environment.populationAmmount):
            if(self.agentList[i].isSusceptible==True):
                self.stateList = "s"
            elif(self.agentList[i].isInfected==True):
                self.stateList = "i"
            elif(self.agentList[i].isRemoved==True):
                self.stateList = "r"

    #Uodate die Farbe der Agenten 
    def __updateColors(self):
        for i in range(self.Environment.populationAmmount):
            if(self.colorList[i]=="s"):
                self.colorList[i]="blue"
            elif(self.colorList[i]=="i"):
                self.colorList[i]="red"
            elif(self.colorList[i]=="r"):
                self.colorList[i]="green"

    #Erfasse die GruppenGrößen
    def __getSIRAmmounts(self):
        sus, inf, rem = 0,0,0
        for a in self.agentList:
            if (a.isSusceptible == True):
                sus += 1
            elif (a.isInfected == True):
                inf += 1
            elif (a.isRemoved == True):
                rem += 1

        self.SusAmmountList.append(sus)
        self.InfAmmountList.append(inf)
        self.RemAmmountList.append(rem)

    #Starte Simulation
    def start(self):
        print("Start")

        fig, ax = plt.subplots()
        sc = ax.scatter(self.xCoordinates,self.yCoordinates,color=self.colorList)

        plt.xlim(0,self.Environment.xDimension)
        plt.ylim(0,self.Environment.yDimension)
        plt.xlabel("Position X")
        plt.ylabel("Position Y")
        plt.title(self.Environment.name)

        def animate(i):
            #Bewege jeden einzelnen Agenten
            for i in range(self.Environment.populationAmmount):
                self.agentList[i].move(self.direction[i],self.Environment.xDimension,self.Environment.yDimension)
            
            #checke den Status jedes Agenten und führe die dazugehörige Operation aus.
            #for i in range(self.Environment.populationAmmount):
            #    self.agentList[i].checkState()

            #update die Koordinaten der Agenten
            self.__updateCoordinates()

            #Stelle die neuen Koordinaten und Farben dar
            sc.set_offsets(np.c_[self.xCoordinates,self.yCoordinates])

            #wenn 1 Sekunde vergangen ist, dann speichere den Zeitpunkt t in TimeList
            #und die Anzahl der S, I und R zum Zeitpunkt t
            if(self.TimeCounter%50==0):
                self.__getSIRAmmounts()
                self.TimeList.append(self.TimeCounter//50)

            self.TimeCounter += 1

        ani = matplotlib.animation.FuncAnimation(fig, animate, frames=50*self.duration, interval=20, repeat=self.extinctDiseas) 
        plt.show()

    #Setze StoppBedingung der Simulation
    #(duration -int =Dauer der Simulation in Sekunden, extinctDiseas -Bool =standardmäßig False, wenn true, hört die Simulation auf, wenn die Krankheit ausgestorben ist)
    def setStopCondition(self, **conditions):
        keys = []
        vals = []
        for k, v in conditions.items():
            keys.append(k)
            vals.append(v)

        if(k=="duration"):
            self.duration = v
        elif(k=="extinctDiseas"):
            self.extinctDiseas = v



