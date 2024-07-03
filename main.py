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

import pygame
from pygame.locals import *

SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)
print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()

pygame.quit()

#https://docs.google.com/document/d/1LHVxTJTYMkBNf8k0A9NXsn0KZqnTA14x/edit