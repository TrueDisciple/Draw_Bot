import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
PX_PER_IN = 20

shapes_list = []
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

class UserPointer():
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.clicking = False
        self.currentNodes = []

    def set_pos(self, mouse_pos):
        self.pos = mouse_pos

player = UserPointer()

def pos_to_snap(pos):
    new_pos = (pos[0]-PX_PER_IN/2, pos[1]-PX_PER_IN/2)
    new_pos = (round(new_pos[0] / PX_PER_IN) * PX_PER_IN, round(new_pos[1] / PX_PER_IN) * PX_PER_IN)
    new_pos = (new_pos[0]+PX_PER_IN/2, new_pos[1]+PX_PER_IN/2)
    return new_pos

while running:
    # process input
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            player.clicking = True
            if len(player.currentNodes) == 0:
                player.currentNodes.append(player.pos)
            else:
                if not player.currentNodes[len(player.currentNodes)-1] == player.pos:
                    player.currentNodes.append(player.pos)
                else:
                    shapes_list.append(player.currentNodes)
                    player.currentNodes = []

        if event.type == MOUSEBUTTONUP:
            player.clicking = False

    # update code
    player.set_pos(pos_to_snap(pygame.mouse.get_pos()))

    # render
    screen.fill((0, 0, 50))
    i, j = 0, 0
    while i < SCREEN_WIDTH:
        i += PX_PER_IN
        j = 0
        while j < SCREEN_HEIGHT:
            j += PX_PER_IN
            pygame.draw.circle(screen, (255, 255, 255), (i-PX_PER_IN/2, j-PX_PER_IN/2), 2)

    pygame.draw.circle(
        screen,
        (255, 0, 0) if player.clicking else (255, 255, 255),
        player.pos,
        7
    )
    if(len(player.currentNodes) >= 2):
        pygame.draw.lines(screen, (255, 255, 255), False, player.currentNodes, 10)
    for shape in shapes_list:
        pygame.draw.lines(screen, (255, 255, 0), False, shape, 10)
    if len(player.currentNodes) > 0:
        pygame.draw.line(screen, (255, 255, 255), player.currentNodes[len(player.currentNodes)-1], player.pos, 10)
    pygame.display.flip()
    # Aricks Code
    # Git Blame

    def super_ui():
        pass
