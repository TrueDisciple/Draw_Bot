import pygame
import pygame_widgets as pw
import GenCommands 
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import math

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
pygame.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PX_PER_IN = 15

shapes_list = []
disable_grid = [pygame.Rect(0, 0, 500, 70)] # first entry from super_UI
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

def super_UI():
    topBar = pygame.Rect(0, 0, 500, 70)
    pygame.draw.rect(screen, (255,255,255), topBar)
    new_screen_but_bord = pygame.Rect(10, 30, 230, 30)
    pygame.draw.rect(screen, (200,200,200), new_screen_but_bord)
    save_drawing_but_bord = pygame.Rect(260, 30, 230, 30)
    pygame.draw.rect(screen, (200,200,200), save_drawing_but_bord)

    wantedFont = pygame.font.SysFont('verdana', 20)
    title = wantedFont.render("DRAW MACHINE IMAGE", True, (0,0,0))

    title_box = title.get_rect()
    title_box.center = (SCREEN_WIDTH // 2, 15)

    screen.blit(title, title_box)

def clearLines(players):
    players.currentNodes = []
    shapes_list.clear()

    #Actual buttons 
new_screen_but = Button(
        #Following documentation
        screen,  # Surface to place button on
        10,  # X-coordinate of top left corner
        30,  # Y-coordinate of top left corner
        230,  # Width
        30,  # Height

        # Optional Parameters
        text='Reset',  # Text to display
        fontSize=20,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(150,150,150),  # Colour of button when not being interacted with
        hoverColour=(100, 150, 150),  # Colour of button when being hovered over
        pressedColour=(100, 200, 200),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: clearLines(player) # Function to call when clicked on
    )
    
export_screen_but = Button(
        screen,  # Surface to place button on
        260,  # X-coordinate of top left corner
        30,  # Y-coordinate of top left corner
        230,  # Width
        30,  # Height

        # Optional Parameters
        text='Export',  # Text to display
        fontSize=20,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(150,150,150),  # Colour of button when not being interacted with
        hoverColour=(100, 150, 150),  # Colour of button when being hovered over
        pressedColour=(100, 200, 200),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: GenCommands.reciever(shapes_list)  # Function to call when clicked on
    )

class UserPointer():
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.clicking = False
        self.currentNodes = []
        self.disable = False
        self.type = "ARC" # "LINE", "ARC"
        self.arcNodes = []

    def set_pos(self, mouse_pos):
        self.pos = mouse_pos

player = UserPointer()

def pos_to_snap(pos):
    new_pos = (pos[0]-PX_PER_IN/2, pos[1]-PX_PER_IN/2)
    new_pos = (round(new_pos[0] / PX_PER_IN) * PX_PER_IN, round(new_pos[1] / PX_PER_IN) * PX_PER_IN)
    new_pos = (new_pos[0]+PX_PER_IN/2, new_pos[1]+PX_PER_IN/2)
    return new_pos

def transform(point1, point2, transformed):
    p1v = pygame.math.Vector2(point1)
    p2v = pygame.math.Vector2(point2)
    tv = pygame.math.Vector2(transformed)
    p1v = p1v - pygame.math.Vector2(point1) 
    p2v = p2v - pygame.math.Vector2(point1) 
    tv = tv - pygame.math.Vector2(point1) 
    line_angle = (p2v-p1v).angle_to(pygame.math.Vector2(1,0))
    rotated = (tv.rotate(line_angle))
    return (rotated[0], rotated[1])

def transform_back(point1, point2, transformed):
    p1v = pygame.math.Vector2(point1)
    p2v = pygame.math.Vector2(point2)
    tv = pygame.math.Vector2(transformed)
    p1v = p1v - pygame.math.Vector2(point1) 
    p2v = p2v - pygame.math.Vector2(point1) 
    line_angle = (p2v-p1v).angle_to(pygame.math.Vector2(1,0))
    rotated = (tv.rotate(-line_angle))
    rotated = rotated + pygame.math.Vector2(point1) 
    return (rotated[0], rotated[1])

def genArcPoints(point1, point2, top):
    new_point1 = transform(point1, point2, point1)
    new_point2 = transform(point1, point2, point2)
    new_top = transform(point1, point2, top)
    new_top = ((new_point2[0]/2), new_top[1])
    newNodes = []
    divisions = 10
    rounding = 1.5
    for i in range(1,divisions):
        newNodes.append((
            i * (new_point2[0]/2)/divisions,
            new_top[1] * (((rounding ** i) - 1) / (rounding ** i))
        ))
    newNodes.append((
        (new_point2[0]/2),
        new_top[1] * (((rounding ** divisions) - 1) / (rounding ** divisions))
    ))
    for i in range(1,divisions):
        newNodes.append((
            (i * (new_point2[0]/2)/divisions) + (new_point2[0]/2),
            new_top[1] * (((rounding ** (divisions-i)) - 1) / (rounding ** (divisions-i)))
        ))
    allNodes = [new_point1] + newNodes + [new_point2]
    allNodes = [transform_back(point1, point2, i) for i in allNodes]
    return allNodes

while running:
    # process input
    events = pygame.event.get()
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN and not player.disable:
            player.clicking = True
            # LINE will be the only one to connect between different clicks for now maybe.
            # Others will use different data structures besides the currentNodes.
            # Or might also just have it so that it still just saves to lines but parses
            # the entire curve as lines in the current nodes list itself.
            if player.type == "ARC":
                if len(player.arcNodes) == 0:
                    player.arcNodes.append(player.pos)
                elif len(player.arcNodes) == 1:
                    player.arcNodes.append(player.pos)
                elif len(player.arcNodes) > 1:
                    # parse the arc into lines and add to current nodes
                    # add to shape if double click at same position
                    # clear arc nodes also
                    shapes_list.append(player.arcNodes)
                    player.arcNodes = []

            elif player.type == "LINE":
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
    player.disable = False
    for rect in disable_grid:
        if rect.collidepoint(pygame.mouse.get_pos()):
            player.disable = True

    if len(player.arcNodes) >= 2:
        player.arcNodes = genArcPoints(player.arcNodes[0], player.arcNodes[len(player.arcNodes)-1], player.pos)
        # player.arcNodes = [player.arcNodes[0], pygame.mouse.get_pos(), player.arcNodes[len(player.arcNodes)-1]]

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
    if len(player.currentNodes) >= 2:
        pygame.draw.lines(screen, (255, 255, 255), False, player.currentNodes, 10)
    if len(player.arcNodes) == 1:
        pygame.draw.line(screen, (255, 255, 255), player.arcNodes[len(player.arcNodes)-1], player.pos, 10)
    if len(player.arcNodes) > 1:
        pygame.draw.lines(screen, (255, 255, 0), False, player.arcNodes, 10)
    for shape in shapes_list:
        if len(shape) < 2:
            continue
        pygame.draw.lines(screen, (255, 255, 0), False, shape, 10)
    if len(player.currentNodes) > 0 and not player.disable:
        pygame.draw.line(screen, (255, 255, 255), player.currentNodes[len(player.currentNodes)-1], player.pos, 10)
    # Aricks Code
    # Git Blame
    super_UI()
    pw.update(events)
    pygame.display.flip()
    


