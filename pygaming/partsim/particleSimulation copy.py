import random, math, pygame as pg, os
from dataclasses import dataclass
from m3ta import save, load, shuffle, agora


windowSize = [120,120]
windowCenter = [windowSize[0]/2,windowSize[1]/2]
population = 1

class Particle:
    def __init__(self,stochastic=False):
        self.position = self.q = position = [random.randrange(0,windowSize[0]),random.randrange(0,windowSize[1])] if stochastic else windowCenter
        self.angle = angle = random.randrange(100000)#random.random()*math.pi*2
        self.mass = self.m = mass = random.random()*.6 + .4
        self.velocity = self.v = velocity = [math.sin(angle), math.cos(angle)]
        self.momentum = self.p = momentum = [mass*velocity[0], mass*velocity[1]]
        self.history = [position]
        self.start = {
            'mass':mass,
            'angle':angle,
            'q':position,
            'v':velocity,
            'p':momentum
        }
    def state(self): 
        return {
            'mass':self.mass,
            'angle':self.angle,
            'q':self.position,
            'v':self.velocity,
            'p':self.momentum
        }
    def tunnel(self):
        self.position = [random.randrange(0,windowSize[0]),random.randrange(0,windowSize[1])]
        return self
    def shake(self):
        # self.angle = angle = random.random()*math.pi*2
        self.angle = angle = random.randrange(100000)#random.random()*math.pi*2
        mass = self.mass
        self.velocity = self.v = velocity = [math.sin(angle), math.cos(angle)]
        self.momentum = self.p = [mass*velocity[0], mass*velocity[1]]
    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.history.append(self.position)
    def flip(self):
        x,y = self.velocity
        self.velocity[0] = y
        self.velocity[1] = x

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
            # Edge rebounds
            if (a:=not 0 < particle.position[0] < windowSize[0]) or (b:=not 0 < particle.position[1] < windowSize[1]):
                a = not 0 < particle.position[0] < windowSize[0]
                b = not 0 < particle.position[1] < windowSize[1]
                if a:
                    if particle.position[0]<=0: 
                        # particle.position[0] = windowSize[0]-1
                        particle.velocity[0] *= -1
                    elif particle.position[0]>=windowSize[0]: 
                        # particle.position[0] = 1
                        particle.velocity[0] *= -1
                        self.augment(1,True)
                if b:
                    if particle.position[1]<=0: 
                        # particle.position[1] = windowSize[1]-1
                        particle.velocity[1] *= -1
                    elif particle.position[1]>=windowSize[1]: 
                        # particle.position[1] = 1
                        particle.velocity[1] *= -1
                        self.augment(1,True)
            particle.move()
            # particle.flip()
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

        self.system = load('partSim1-systems.pkl') if os.path.exists('partSim1-systems.pkl') else []

        self.styles = load('partSim1-styles.pkl') if os.path.exists('partSim1-styles.pkl') else []
        self.backs = load('partSim1-backs.pkl') if os.path.exists('partSim1-backs.pkl') else []
        self.fores = load('partSim1-fores.pkl') if os.path.exists('partSim1-fores.pkl') else []
        
        self.dots = load('partSim1-dots.pkl') if os.path.exists('partSim1-dots.pkl') else []
        self.trails = load('partSim1-trails.pkl') if os.path.exists('partSim1-trails.pkl') else []
        self.ensembles = load('partSim1-ensembles.pkl') if os.path.exists('partSim1-ensembles.pkl') else []
    
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
        self.backcolour = backcolour = tuple(random.randint(0,255) for i in range(3))
        self.dotcolour = dotcolour = tuple(abs(255-i) for i in backcolour)
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)
        self.surface.fill(self.backcolour)
    def newEnsemble(self,conservative=True,stochastic=False):
        self.ensemble = Ensemble(self.currentSize,stochastic) if conservative else Ensemble(population,stochastic)
    def newSystem(self,conservative=True,stochastic=False):
        self.ensemble = Ensemble(self.currentSize,stochastic) if conservative else Ensemble(population,stochastic)
        self.backcolour = backcolour = tuple(random.randint(0,255) for i in range(3))
        self.dotcolour = dotcolour = tuple(abs(255-i) for i in backcolour)
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)
        self.surface.fill(self.backcolour)
    def newDotcolour(self):
        self.dotcolour = tuple(random.randint(0,255) for i in range(3))
    def newTrailcolour(self):
        self.trailcolour = tuple(random.randint(0,255) for i in range(3))
    def newBackcolour(self):
        self.backcolour = tuple(random.randint(0,255) for i in range(3))
        self.surface.fill(self.backcolour)
    def newForecolours(self):
        self.dotcolour = dotcolour = tuple(random.randint(0,255) for i in range(3))
        self.trailcolour = shuffle(abs(255-i) for i  in dotcolour)
        # print(dotcolour,t)

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
                'ensemble':self.ensemble,
                'dimensions': windowSize,

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
        clock = pg.time.Clock()
        # initialize and prepare screen
        pg.init()
        pg.display.set_caption("pygame Stars Example")

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
                    for particle in self.ensemble:
                        particle.tunnel()
                        particle.shake()
                    print('shaken and stirred')
                elif e.type == pg.KEYDOWN and e.key==48:
                    '0 - save system'
                    self.saveSystem()
                elif e.type == pg.KEYDOWN and e.key==49:
                    '1 - save ensemble'
                    self.saveEnsemble()
                elif e.type == pg.KEYDOWN and e.key==50:
                    '2 - save styles'
                    self.saveStyle()
                elif e.type == pg.KEYDOWN and e.key==51:
                    '3 - save back'                 
                    self.saveBack()
                elif e.type == pg.KEYDOWN and e.key==52:
                    '4 - save fores'
                    self.saveFore()
                elif e.type == pg.KEYDOWN and e.key==53:
                    '5 - save dotcolour'
                    self.saveDotcolour()
                elif e.type == pg.KEYDOWN and e.key==54:
                    '6 - save trailcolour'
                    self.saveTrailcolour()
                
                elif e.type == pg.KEYDOWN and e.key==56:
                    '8 - save trailcolour'
                    self.augment()
                elif e.type == pg.KEYDOWN and e.key==59:
                    '9 - save trailcolour'
                    self.reset()
                
                elif e.type == pg.KEYDOWN and e.key==112:
                    'p - new system'
                    self.newSystem()
                elif e.type == pg.KEYDOWN and e.key==113:
                    'q - new ensemble'
                    self.newEnsemble()
                elif e.type == pg.KEYDOWN and e.key==119:
                    'w - new styles'
                    self.newStyles()
                elif e.type == pg.KEYDOWN and e.key==101:
                    'e - new backcolour'
                    self.newBackcolour()
                elif e.type == pg.KEYDOWN and e.key==114:
                    'r - new forecolour'
                    self.newForecolours()
                elif e.type == pg.KEYDOWN and e.key==116:
                    't - new dotcolour'
                    self.newDotcolour()
                elif e.type == pg.KEYDOWN and e.key==121:
                    'y - new trailcolour'
                    self.newTrailcolour()
            clock.tick(50)


cues = [
'0 - save system',
'1 - save ensemble',
'2 - save styles',
'3 - save back',
'4 - save fores',
'5 - save dotcolour',
'6 - save trailcolour',
'8 - save trailcolour',
'9 - save trailcolour',
'p - new system',
'q - new ensemble',
'w - new styles',
'e - new backcolour',
'r - new forecolour',
't - new dotcolour',
'y - new trailcolour'
]
if __name__ == '__main__':
    for i,q in enumerate(cues):
        print(f'#{i}:\t{q}')
    L = Visor(stochastic=True)
    # L = Visor()
    L.main()




    pass