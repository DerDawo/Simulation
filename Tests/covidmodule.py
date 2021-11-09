import environment as em

class agent:

    sir = {
        "s":"susceptible",
        "i":"infectious",
        "r":"removed",
    }

    def __init__(self, id, position, SIRState, infectionProbability, deathRate ):
        self.id = id
        self.position = position
        self.SIRState = SIRState
        self.infectionProbability = infectionProbability
        self.deathRate = deathRate

    def move(self,direction):
        self.position.x += direction[0] 
        self.position.y += direction[1]


class position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class virus:
    def __init__(self, infectionRadius, incubationTime):
        self.infectionRadius = infectionRadius
        self.incubationTime = incubationTime#
