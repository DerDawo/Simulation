import environment as env
import virus as vir
import simulation as sim

#initialisere eine Umgebung
#environment(name -str, xDimension -int, yDimension -int, populationAmmount -int, distance -float, hasMasks -bool, hasAusgangssperre -bool, hasLockdown-bool)
env1 = env.environment("Environment 1",50,50,100,0,False,False,False)

#initialisiere einen Virus
#virus(name -str, infectionRadius -float, infectionProbability -float, incubationTime -int, infectionTime -int, deathProbability -float)
virus1 = vir.virus("cov",1.5,0.9990,14,10,0.001)

#initialisere eine Simulation
#simulation(virus -virus, environment -environment)
sim1 = sim.simulation(virus1,env1)

#setStopCondition(duration -int =Dauer der Simulation in Sekunden, extinctDiseas -Bool =standardmäßig False, wenn true, hört die Simulation auf, wenn die Krankheit ausgestorben ist)
sim1.setStopCondition(extinctDiseas=True)
#Starte Simmulation(FPS -wie viel frames sollen pro Sekunde berechnet werden) 
sim1.start(25)
