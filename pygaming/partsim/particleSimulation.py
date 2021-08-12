import random, math, pygame as pg, os
from dataclasses import dataclass
from m3ta import save, load, shuffle, agora


windowSize = [640, 480]
windowCenter = [windowSize[0]/2,windowSize[1]/2]
population = 15

class Particle:
    def __init__(self,stochastic=False):
        self.position = self.q = position = [random.randrange(0,windowSize[0]),random.randrange(0,windowSize[1])] if stochastic else windowCenter
        self.angle = angle = random.random()*math.pi*2
        self.mass = self.m = mass = random.random()*.6 + .4
        self.velocity = self.v = velocity = [math.sin(angle), math.cos(angle)]
        self.momentum = self.p = momentum = [mass*velocity[0], mass*velocity[1]]
        self.start = {
        'q':position,
        'v':velocity,
        'p':momentum
    }
    def state(self): 
        return {
            'angle':self.angle,
            'q':self.q,
            'v':self.v,
            'p':self.p
    }
    def tunnel(self):
        self.position = (random.randrange(0,windowSize[0]),random.randrange(0,windowSize[1]))
        return self

class Ensemble:
    def __init__(self,cardinality=population,stochastic=False):
        self.particles = [Particle(stochastic) for i in range(cardinality)]
        self.ind = -1
    def __next__(self):
        if self.ind<len(self.particles)-1:
            self.ind += 1
            return self.particles[self.ind]
        else:
            self.ind = -1
            raise StopIteration
    def __iter__(self):
        return self
    def __getitem__(self,value):
        return self.particles[value]
    def initialize(self,stochastic=False):
        for i in range(population):
            self.particles.append(Particle(stochastic))
    def update(self):
        parts = tuple(particle for particle in self.particles)
        for i,particle in enumerate(self.particles):
            if any(particle.q[0]==part.q[0] and i!=j for j,part in enumerate(parts)):
                particle.velocity[0] *= -1
            if any(particle.q[1]==part.q[1] and i!=j for j,part in enumerate(parts)):
                particle.velocity[1] *= -1
            if not 0<particle.position[0]<windowSize[0]:
                if particle.position[0]<=0:
                    particle.position[0] = windowSize[0]-1
                elif particle.position[0]>=windowSize[0]:
                    particle.position[0] = 1
            if not 0<particle.position[1]<windowSize[1]:
                if particle.position[1]<=0:
                    particle.position[1] = windowSize[1]-1
                elif particle.position[1]:
                    particle.position[1] = 1
            # if not 0<=particle.position[0]<=windowCenter[0]:
            #     particle.velocity[0] *= -1
            #     # particle.position[0] = windowSize[0]
            # if not 0<=particle.position[1]<=windowCenter[1]:
            #     particle.velocity[1] *= -1
            #     # particle.position[0] = windowSize[0]
            particle.position[0] += particle.velocity[0]
            particle.position[1] += particle.velocity[1]
    def augment(self,extent=1,stochastic=False):
        for i in range(extent):
            self.particles.append(Particle(stochastic))
            
    
class Visor:
    def __init__(self,dimensions=windowSize,size=population,stochastic=False):
        self.surface = pg.display.set_mode(dimensions)
        self.originalSize = self.currentSize = size

        self.ensemble = self.originalEnsemble = Ensemble(size,stochastic)
        self.backcolour = self.originalBackColour = backcolour = tuple(random.randint(0,255) for i in range(3))
        self.dotcolour = self.originalDotColour = dotcolour = tuple(abs(255-i) for i in backcolour)
        self.trailcolour = self.originalTrailColour = shuffle(abs(255-i) for i  in dotcolour)

        self.styles = load('partSim1-styles.pkl') if os.path.exists('partSim1-styles.pkl') else []
        self.system = load('partSim1-.pkl') if os.path.exists('partSim1-.pkl') else []

        self.backs = load('partSim1-backs.pkl') if os.path.exists('partSim1-backs.pkl') else []
        self.fores = load('partSim1-.pkl') if os.path.exists('partSim1-.pkl') else []
        
        self.dots = load('partSim1-dots.pkl') if os.path.exists('partSim1-dots.pkl') else []
        self.trails = load('partSim1-trails.pkl') if os.path.exists('partSim1-trails.pkl') else []
        self.ensembles = load('partSim1-.pkl') if os.path.exists('partSim1-.pkl') else []
    
    def drawParticles(self,colour):
        "used to draw (and clear) the stars"
        for particle in self.ensemble:
            pos = (int(particle.position[0]), int(particle.position[1]))
            self.surface.set_at(pos, colour)
    def moveParticles(self):
        self.ensemble.update()
    def augment(self,value=1,stochastic=False):
        self.ensemble.augment(value,stochastic)
        self.currentSize += 1
    def reset(self):
        self.ensemble = self.originalEnsemble
        self.backcolour = self.originalBackColour
        self.dotcolour = self.originalDotColour
        self.trailcolour = self.originalTrailColour

    def newStyles(self):
        self.backcolour = backcolour = (random.randint(0,255) for i in range(3))
        self.dotcolour = dotcolour = tuple(abs(255-i) for i in backcolour)
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)
    def newEnsemble(self,conservative=True,stochastic=False):
        self.ensemble = Ensemble(self.currentSize,stochastic) if conservative else Ensemble(population,stochastic)
    def newSystem(self,conservative=True,stochastic=False):
        self.ensemble = Ensemble(self.currentSize,stochastic) if conservative else Ensemble(population,stochastic)
        self.backcolour = backcolour = tuple(random.randint(0,255) for i in range(3))
        self.dotcolour = dotcolour = tuple(abs(255-i) for i in backcolour)
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)
    def newDotcolour(self):
        self.dotcolour = (random.randint(0,255) for i in range(3))
    def newTrailcolour(self):
        self.trailcolour = (random.randint(0,255) for i in range(3))
    def newBackcolour(self):
        self.backcolour = (random.randint(0,255) for i in range(3))
    def newForecolours(self):
        self.dotcolour = dotcolour = (random.randint(0,255) for i in range(3))
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)

    def saveStyle(self):
        self.styles.append(
            {
                'dotcolour':self.dotcolour,
                'trailcolour':self.trailcolour,
                'backcolour':self.backcolour
            }
        )
        save(self.styles,'partSim1-styles.pkl')
        print(f'saved style @ {agora(True)}')
    def saveSystem(self):
        self.system.append(
            {
                'styles':{
                    'dotcolour':self.dotcolour,
                    'trailcolour':self.trailcolour,
                    'backcolour':self.backcolour
                },
                'ensemble':self.ensemble
            }
        )
        save(self.system,'partSim1-systems.pkl')
        print(f'saved system @ {agora(True)}')
    def saveBack(self):
        self.backs.append(self.backcolour)
        save(self.backs,'partSim1-backs.pkl')
        print(f'saved back @ {agora(True)}')
    def saveFore(self):
        self.fores.append(
            {
                'dotcolour':self.dotcolour,
                'trailcolour':self.trailcolour
            }
        )
        save(self.fores,'partSim1-fores.pkl')
        print(f'saved fore @ {agora(True)}')
    def saveDotcolour(self):
        self.dots.append(self.dotcolour)
        save(self.dots,'partSim1-dots.pkl')
        print(f'saved dot colour @ {agora(True)}')
    def saveTrailcolour(self):
        self.trails.append(self.trailcolour)
        save(self.trails,'partSim1-trails.pkl')
        print(f'saved trail colour @ {agora(True)}')
    def saveEnsemble(self):
        self.ensembles.append(self.ensemble)
        save(self.ensembles,'partSim1-ensembles.pkl')
        print(f'saved ensemble @ {agora(True)}')

    def main(self):
        "This is the starfield code"
        # create our starfield
        random.seed()
        # stars = Ensemble()
        # stars.initialize()
        clock = pg.time.Clock()
        # initialize and prepare screen
        pg.init()
        pg.display.set_caption("pygame Stars Example")
        # white = 255, 240, 200
        # black = 20, 20, 40
        # screen.fill(black)
        self.backcolour = (0,0,255)
        self.dotcolour = (0,0,0)
        self.trailcolour = (255,255,255)
        self.surface.fill(self.backcolour)

        # main game loop
        done = 0
        while not done:
            self.drawParticles(self.trailcolour)
            self.moveParticles()
            self.drawParticles(self.dotcolour)
            pg.display.update()
            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                    done = 1
                    break
                elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                    # windowCenter[:] = [random.randint(0,windowSize[0]),random.randint(0,windowSize[1])]#list(e.pos)
                    # [particle.position[0],particle]
                    for particle in self.ensemble:
                        particle.position[0] = random.randint(0,windowSize[0])
                        particle.position[1] = random.randint(0,windowSize[1])
            clock.tick(50)

if __name__ == '__main__':
    L = Visor(stochastic=True)
    L.main()




    pass