# from puch1.modul import say_hello as hello,sum as summa , factorial as fac
# from puch1.puch2.newpuch import score as asum
# print(hello("Evgeny"))
# print(fac(5))
# print(asum(1,2,3,4,5,6))

# import pygame
# from pygame.locals import *

# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# GRAY = (150, 150, 150)
#
# pygame.init()
# screen = pygame.display.set_mode((640, 240))
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         drawing = False
#         points = []
#
#         if event.type == QUIT:
#             running = False
#         elif event.type == MOUSEBUTTONDOWN:
#             points.append(event.pos)
#             drawing = True
#         elif event.type == MOUSEBUTTONUP:
#             drawing = False
#         elif event.type == MOUSEMOTION and drawing:
#             points[-1] = event.pos
#         screen.fill(GRAY)
#         if len(points) > 1:
#             rect = pygame.draw.lines(screen, RED, True, points, 3)
#             pygame.draw.rect(screen, GREEN, rect, 1)
#             pygame.display.update()
#         elif event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 if len(points) > 0:
#                     points.pop()
#
#
#     screen.fill(GRAY)
#     pygame.display.update()
#
# pygame.quit()

# import pygame
# from pygame.locals import *
#
# SIZE = 500, 200
# RED = (255, 0, 0)
# GRAY = (150, 150, 150)
#
# pygame.init()
# screen = pygame.display.set_mode(SIZE)
#
# rect = Rect(50, 60, 200, 80)
# print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
# print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
# print(f'center={rect.center}')
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#
#     screen.fill(GRAY)
#     pygame.draw.rect(screen, RED, rect)
#     pygame.display.flip()
#
# pygame.quit()

#https://docs.google.com/document/d/1LHVxTJTYMkBNf8k0A9NXsn0KZqnTA14x/edit











# '''Вариант 1'''
# import pygame, sys , random
#
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# clock = pygame.time.Clock()
# PARTICLE_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(PARTICLE_EVENT, 150)
# nyan_surface = pygame.image.load('nyam cat/nyan_cat.png').convert_alpha()
#
#
#
# class ParticlePrinciple:
#     def __init__(self):
#         self.particles = []
#         self.size = 8
#
#
#     def emit(self):
#         if self.particles:
#             self.delete_particles()
#             for particle in self.particles:
#                 particle[0][1] += particle[2][0]
#                 particle[0][0] += particle[2][1]
#                 particle[1] -= 0.2
#                 pygame.draw.circle(screen, pygame.Color('White'), particle[0], int(particle[1]))
#
#
#
#     def add_particles(self):
#         pos_x = pygame.mouse.get_pos()[0]
#         pos_y = pygame.mouse.get_pos()[1]
#         radius = 10
#         direction_x = random.randint(-3, 3)
#         direction_y = random.randint(-3, 3)
#         particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
#         self.particles.append(particle_circle)
#
#
#     def delete_particles(self):
#         particles_copy = [particle for particle in self.particles if particle[1] > 0]
#         self.particles = particles_copy
#
# particle1 = ParticlePrinciple()
#
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == PARTICLE_EVENT:
#             particle1.add_particles()
#
#
#
#
#     screen.fill((30, 30, 30))
#     particle1.emit()
#     pygame.display.update()
#     clock.tick(120)












'''Вариант 2'''
import pygame, sys , random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 40)
nyan_surface = pygame.image.load('nyam cat/nyan_cat.png').convert_alpha()
nyan_rect=pygame.image.load('nyam cat/star.png').convert_alpha()



class ParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.size = 10


    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pygame.draw.rect(screen, particle[1], particle[0])
                self.draw_nyancat()






    def add_particles(self, offset, color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1] + offset
        particle_rect = pygame.Rect(pos_x - self.size / 2, pos_y - self.size / 2,self.size, self.size)
        self.particles.append((particle_rect, color))




    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[0].x > 0]
        self.particles = particles_copy
    def draw_nyancat(self):
        nyan_rect = nyan_surface.get_rect(center=pygame.mouse.get_pos())
        screen.blit(nyan_surface, nyan_rect)



particle1 = ParticlePrinciple()
particle2=ParticlePrinciple()





while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            # particle1.add_particles()
            particle2.add_particles(0, pygame.Color('Red'))




    particle2.add_particles(-30, pygame.Color('Red'))
    particle2.add_particles(-18, pygame.Color('Orange'))
    particle2.add_particles(-6, pygame.Color('Yellow'))
    particle2.add_particles(6, pygame.Color('Green'))
    particle2.add_particles(18, pygame.Color('Blue'))
    particle2.add_particles(30, pygame.Color('Purple'))


    screen.fill((30, 30, 30))
    particle2.emit()
    pygame.display.update()
    clock.tick(120)