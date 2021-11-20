import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math

class view:
    def __inti__(self, simulation):
        self.simulation = simulation

    def animate(self, data, FPS):
        iv = 1000/FPS
        #erstelle 2 Plots
        fig, (ax1, ax2) = plt.subplots(1,2)
        #Scatter Plot - Simulation
        sc = ax1.scatter(self.simulation.environment.xCoordinates,self.simulation.environment.yCoordinates,color=self.simulation.colorList)
        #Line Plot - Verbreitung
        pl1, = ax2.plot(self.simulation.TimeList,self.simulation.SusAmmountList,"-b", label="susceptible")
        pl2, = ax2.plot(self.simulation.TimeList,self.simulation.InfAmmountList,"-r", label="infectious")
        pl3, = ax2.plot(self.simulation.TimeList,self.simulation.RemAmmountList,"-g", label="removed")
        ax2.legend(loc="upper left")
        #Scatter Plot Spezifikationen
        ax1.set_xlim(0,self.simulation.Environment.xDimension)
        ax1.set_ylim(0,self.simulation.Environment.yDimension)
        ax1.set_xlabel("Position X")
        ax1.set_ylabel("Position Y")
        ax1.set_title(str(self.simulation.Environment.name)+" Simulation")
        #Line Plot Spezifikationen
        ax2.set_ylim(0,self.simulation.Environment.populationAmmount)
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Agents")
        ax2.set_title(str(self.simulation.Environment.name)+" Spread")

        def animate(i):
            #Update die Daten der Simualtion (Koordinaten der Agenten)
            sc.set_facecolor(self.simulation.colorList)
            sc.set_offsets(np.c_[self.simulation.environment.xCoordinates,self.simulation.environment.yCoordinates])
            
            #Update die Daten der Verbreitung (Kennzahlen der Gruppen)
            pl1.set_data(self.simulation.TimeList,self.simulation.SusAmmountList)
            pl2.set_data(self.simulation.TimeList,self.simulation.InfAmmountList)
            pl3.set_data(self.simulation.TimeList,self.simulation.RemAmmountList)
            #Update die x Achse des Line Plots
            ax2.relim()
            ax2.autoscale_view()
                
        ani = matplotlib.animation.FuncAnimation(fig, animate, frames=FPS*self.simulation.duration, interval=iv, repeat=self.simulation.extinctDiseas) 
        plt.show()


    def show(data, **kwargs):
        print("SHOW")
