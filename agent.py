from environment import environment
from virus import virus
import random

class agent:
    def __init__(self, id, position, isSusceptible, isInfected, isRemoved, Environment):
        self.id = id
        self.position = position
        self.isSusceptible = isSusceptible
        self.isInfected = isInfected
        self.isRemoved = isRemoved
        self.Environment = Environment
        self.Virus = None
        self.TimeBeeingInfected = 0

    def move(self,direction,xDimension,yDimension,agentList):
        #Ist die Neue Position des Agenten außerhalb der xDimension des Enviornemnt, kehre die Richtung des Agenten um
        if(self.position.x+direction.x>xDimension):
            direction.x = direction.x*(-1)
        elif(self.position.x+direction.x<0):
            direction.x = direction.x*(-1)

        #Ist die Neue Position des Agenten außerhalb der yDimension des Enviornemnt, kehre die Richtung des Agenten um
        if(self.position.y+direction.y>yDimension):
            direction.y = direction.y*(-1)
        elif(self.position.y+direction.y<0):
            direction.y = direction.y*(-1)

        self.position.x += direction.x 
        self.position.y += direction.y

        #Hat die DistanceToKeep einen Wert größer als 0, so muss Abstand eingahlten werden
        """
        if(self.Environment.distanceToKeep>0):

            dist = self.Environment.distanceToKeep

            #checke als erstes welche Punkte in Betracht kommen könnten
            for i in agentList:

                distAg = (abs(i.position.x-self.position.x)**2 + abs(i.position.y-self.position.y)**2)**0.5
                #Wenn die SSK <= SH ist, dann befindet sich der Punkt im Infektionsradius und es kann eine mögliche Infektion stattfinden
                if (dist<=distAg):

                    #Ist die Neue Position des Agenten außerhalb der xDimension des Enviornemnt, kehre die Richtung des Agenten um
                    if(self.position.x+direction.x>i.position.x-dist):
                        direction.x = direction.x*(-1)
                    elif(self.position.x+direction.x<i.position.x+dist):
                        direction.x = direction.x*(-1)

                    #Ist die Neue Position des Agenten außerhalb der yDimension des Enviornemnt, kehre die Richtung des Agenten um
                    if(self.position.y+direction.y>i.position.y-dist):
                        direction.y = direction.y*(-1)
                    elif(self.position.y+direction.y<i.position.y+dist):
                        direction.y = direction.y*(-1)

            self.position.x += direction.x 
            self.position.y += direction.y
        """



    def infect(self, agentList):
        #Quadrat der Hypothenuse
        sh = self.Virus.infectionRadius**2

        #checke als erstes welche Punkte in Betracht kommen könnten
        for i in agentList:
            #Summe der Kathetenquadrate
            ssk = abs(i.position.x-self.position.x)**2 + abs(i.position.y-self.position.y)**2
            #Wenn die SSK <= SH ist, dann befindet sich der Punkt im Infektionsradius und es kann eine mögliche Infektion stattfinden
            if (ssk<=sh) and i.isSusceptible == True:
                #Ziehe zufallszahl r
                #Ist diese größer, als die Infektionswahrscheinlichkeit, infiziere
                r = random.random()
                if(r>1-self.Virus.infectionProbability):
                    i.getInfected()                

    def increaseTimeBeeingInfected(self):
        self.TimeBeeingInfected +=1

    def setVirus(self,v):
        self.Virus = v

    def getInfected(self):
        self.isInfected = True
        self.isSusceptible = False

    def getRemoved(self):
        self.isRemoved = True
        self.isInfected = False
        self.Virus = None
        self.TimeBeeingInfected = 0

class position:
    def __init__(self,x,y):
        self.x = x
        self.y = y