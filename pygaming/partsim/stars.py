#!/usr/bin/env python

"""A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management"""


import random, math, pygame, os
from pygame.locals import *
from m3ta import save,load,nameSpacer,shuffle,agora,jar

#constants
WINSIZE = [300, 680][::-1]
# WINCENTER = [round(WINSIZE[0]/2), round(WINSIZE[1]/2)]
WINCENTER = [WINSIZE[0]/2, WINSIZE[1]/2]
NUMSTARS = 150
NUMSTARS = 15


def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random.random()*.6+.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]


def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        # vel, pos = star
        vel, pos = star[0], [random.randrange(WINSIZE[0]),random.randrange(WINSIZE[1])]
        # steps = random.randint(0, WINCENTER[0])
        steps = random.randint(0, round(WINCENTER[0]))
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .09)# * -1*(-1 if x%2==0 else 1)
        vel[1] = vel[1] * (steps * .09)# * -1*(1 if x%2==0 else -1)
        stars.append(star)
    move_stars(stars)
    return stars
  

def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        
        # 
        # 
        # Edge rebounds
        if (a:=not 0 < pos[0] < WINSIZE[0]) or (b:=not 0 < pos[1] < WINSIZE[1]):
            if a:
                if pos[0]<=0: 
                    # pos[0] = WINSIZE[0]-1
                    vel[0] *= -1#init_star()[0]
                elif pos[0]>=WINSIZE[0]: 
                    # pos[0] = 1
                    vel[0] *= -1#init_star()[0]
            if b:
                if pos[1]<=0: 
                    # pos[1] = WINSIZE[1]-1
                    vel[1] *= -1#init_star()[0]
                elif pos[1]>=WINSIZE[1]: 
                    # pos[1] = 1
                    vel[1] *= -1#init_star()[0]   
        # if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            # vel[:], pos[:] = init_star()
        # Mid-line rebounds
        elif (a:=pos[0] == WINCENTER[0]) or (b:=pos[1]==WINCENTER[1]):
            if a:
                if pos[0]<=0: 
                    # pos[0] = WINSIZE[0]-1
                    vel[0] *= -1#init_star()[0]
                elif pos[0]>=WINSIZE[0]: 
                    # pos[0] = 1
                    vel[0] *= -1#init_star()[0]
            if b:
                if pos[1]<=0: 
                    # pos[1] = WINSIZE[1]-1
                    vel[1] *= -1#init_star()[0]
                elif pos[1]>=WINSIZE[1]: 
                    # pos[1] = 1
                    vel[1] *= -1#init_star()[0]
        else:
            x,y = vel
            vel[0] = y #* 1.015 #if random.random() > .5 else 1-.015#* -1*(1 if random.random()<.5 else -1) #* (random.random(),2)[random.randint(0,1)]#* 1.05
            vel[1] = x #* 1.015 #if random.random() > .5 else 1-.015#* -1*(1 if random.random()<.5 else -1) #* (random.random(),2)[random.randint(0,1)]#* 1.05
  

def main():
    "This is the starfield code"
    #create our starfield
    random.seed()
    stars = initialize_stars()
    clock = pygame.time.Clock()
    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('pygame Stars Example')
    num = random.randint(0,1)
    # fg1 = 255, 240, 200
    # fg2 = 20, 20, 40
    styles = load('starStyles.pkl') if os.path.exists('starStyles.pkl') else []
    paths = load('starPaths.pkl') if os.path.exists('starPaths.pkl') else []
    bgs = load('starBackgrounds.pkl') if os.path.exists('starBackgrounds.pkl') else []
    fgs = load('starForegrounds.pkl') if os.path.exists('starForegrounds.pkl') else []
    bg = tuple(random.randint(0,255) for i in range(3))
    fg1 = tuple(abs(255-i) for i in bg)
    fg2 = shuffle(abs(255-i) for i  in fg1)
    clrs = {
        'bg':bg,
        'wht':fg1,
        'blk':fg2
    }
    
    # m3ta.save()
    # print(bg)
    # print(f'{clrs["bg"] = }\n{clrs["wht"] = }\n{clrs["blk"] = }')
    screen.fill(bg)

    #main game loop
    done = 0
    while not done:
        # stars = initialize_stars()
        draw_stars(screen, stars, fg2)
        move_stars(stars)
        draw_stars(screen, stars, fg1)
        # move_stars(stars)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type==KEYDOWN and e.key==99:
                'C - New Colours'
                bg = tuple(random.randint(0,255) for i in range(3))
                fg1 = tuple(abs(255-i) for i in bg)
                fg2 = shuffle(abs(255-i) for i  in fg1)
                clrs = {
                    'bg':bg,
                    'wht':fg1,
                    'blk':fg2
                }
                screen.fill(bg)
            elif e.type==KEYDOWN and e.key==102:
            # elif random.randint(0,5)>4:
                'F - New fore colours'
                bg = tuple(random.randint(0,255) for i in range(3))
                fg1 = tuple(abs(255-i) for i in bg)
                fg2 = shuffle(abs(255-i) for i  in fg1)
                clrs = {
                    'bg':bg,
                    'wht':fg1,
                    'blk':fg2
                }
            elif e.type==KEYDOWN and e.key==110:
                'N - New styles and paths'
                bg = tuple(random.randint(0,255) for i in range(3))
                fg1 = tuple(abs(255-i) for i in bg)
                fg2 = shuffle(abs(255-i) for i  in fg1)
                clrs = {
                    'bg':bg,
                    'wht':fg1,
                    'blk':fg2
                }
                screen.fill(bg)
                stars = initialize_stars()
            elif e.type==KEYDOWN and e.key==114:
                'R - Reset Background'
                screen.fill(bg)
            elif e.type==KEYDOWN and e.key==98:
                'B - New Background'
                bg = tuple(random.randint(0,255) for i in range(3))
                screen.fill(bg)
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                'mleft - new paths'
                WINCENTER[:] = list(e.pos)
                stars = initialize_stars()
            elif e.type == MOUSEBUTTONDOWN and e.button == 3:
                'mright - save colours'
                styles.append(clrs)
                save(styles,'starStyles.pkl')
                print(f'saved styles @ {agora(True)}')
            elif e.type==KEYDOWN and e.key==112:
                'P - save paths'
                paths.append(stars)
                save(paths,'starPaths.pkl')
                print(f'saved paths @ {agora(True)}')
            elif e.type==KEYDOWN and e.key==56:
                '8 - save background'
                bgs.append(bg)
                save(bgs,'starPaths.pkl')
                print(f'saved back @ {agora(True)}')
            elif e.type==KEYDOWN and e.key==52:
                '4 - save foreground'
                fgs.append((fg1,fg2))
                save(fgs,'starForegrounds.pkl')
                print(f'saved fores @ {agora(True)}')
            elif e.type==KEYDOWN and e.key==97:
                'A - save all'
                styles.append(clrs)
                save(styles,'starStyles.pkl',True)
                print(f'saved styles @ {agora(True)}')
                paths.append(stars)
                save(paths,'starPaths.pkl',True)
                print(f'saved paths @ {agora(True)}')
            # elif e.type == KEYDOWN and e.key==:
                
        clock.tick(500)


# if python says run, then we should run
if __name__ == '__main__':
    hotkeys = [
        'A - save all',
        'P - save paths',
        '4 - save foreground',
        '8 - save background',
        'mleft - new particles',
        'mright - save styles',
        'B - New Background',
        'R - Reset Background',
        'N - New styles and paths',
        'F - New fore colours',
        'C - New Colours'
    ]
    print('\n'.join(f'{i+1}\t{j}' for i,j in enumerate(hotkeys)))
    main()
    # print(load('starColourings.pkl'))
    # jar('starColourings.pkl')
    # save(load('starColourings.pkl').append(load('starColourings_12.pkl')),'starColourings.pkl')
    # print(load('starColourings.pkl'))
    # from send2trash import send2trash as trash
    # trash('starColourings_12.pkl')
    


