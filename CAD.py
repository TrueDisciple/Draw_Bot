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
SIDE_BAR = 120
TOP_BAR = 70
PX_PER_IN = 15

shapes_list = []
disable_grid = [pygame.Rect(0, 0, 1000, 70), pygame.Rect(0, 0, 140, 600)] # first entry from super_UI
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

lineTool = pygame.image.load('.\\Draw_Bot\\images\\line.png')
boxbox = pygame.image.load('.\\Draw_Bot\\images\\square.png')
circlebox = pygame.image.load('.\\Draw_Bot\\images\\circle.png')
arcbox = pygame.image.load('.\\Draw_Bot\\images\\arc.png')
starbox = pygame.image.load('.\\Draw_Bot\\images\\star.png')

def super_UI():
    #Side bar brushes with shapes 
    sideBord = pygame.Rect(0,0, SIDE_BAR + 8, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (20,20,20), sideBord)

    sideBar = pygame.Rect(0,0, SIDE_BAR, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (60,60,70), sideBar)

    #Top Bar UI With buttons
    topBord = pygame.Rect(0, 0, SCREEN_WIDTH, TOP_BAR + 8)
    pygame.draw.rect(screen, (20,20,20), topBord)

    topBar = pygame.Rect(0, 0, SCREEN_WIDTH, TOP_BAR)
    pygame.draw.rect(screen, (60,60,70), topBar)

    # imgpy = pygame.image.load('.\\Draw_Bot\\images\\bar.png').convert()
    # imgpy = pygame.transform.scale(imgpy, (SCREEN_WIDTH, 70))
    # screen.blit(imgpy, (0,0))

    wantedFont = pygame.font.SysFont('verdana', 20)
    wantedFont.set_bold(True)
    wantedFont.set_underline(True)
    title = wantedFont.render("DRAW MACHINE IMAGE", True, (200,200,200))

    title_box = title.get_rect()
    title_box.center = (SCREEN_WIDTH // 2, 15)

    screen.blit(title, title_box)

def clearLines(players):
    players.currentNodes = []
    shapes_list.clear()

def doubPop(players):
    if len(player.currentNodes) > 0:
        players.currentNodes.pop()
        

    #Actual buttons 
new_screen_but = Button(
        #Following documentation
        screen,  # Surface to place button on
        5,  # X-coordinate of top left corner
        30,  # Y-coordinate of top left corner
        (SCREEN_WIDTH / 3) -10,  # Width
        30,  # Height

        # Optional Parameters
        text='Reset',  # Text to display
        fontSize=20,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(190,170,190),  # Colour of button when not being interacted with
        hoverColour=(100, 150, 150),  # Colour of button when being hovered over
        pressedColour=(100, 200, 200),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: clearLines(player) # Function to call when clicked on
    )
    
export_screen_but = Button(
        screen,  # Surface to place button on
        (SCREEN_WIDTH / 3) + 5,  # X-coordinate of top left corner
        30,  # Y-coordinate of top left corner
        (SCREEN_WIDTH / 3) - 10,  # Width
        30,  # Height

        # Optional Parameters
        text='Export',  # Text to display
        fontSize=20,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(190,170,190),  # Colour of button when not being interacted with
        hoverColour=(100, 150, 150),  # Colour of button when being hovered over
        pressedColour=(100, 200, 200),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: GenCommands.reciever(shapes_list)  # Function to call when clicked on
    )

undo_screen_but = Button(
        screen,  # Surface to place button on
        2*(SCREEN_WIDTH / 3) + 5,  # X-coordinate of top left corner
        30,  # Y-coordinate of top left corner
        (SCREEN_WIDTH/ 3) - 10,  # Width
        30,  # Height

        # Optional Parameters
        text='Undo',  # Text to display
        fontSize=20,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(190,170,190),  # Colour of button when not being interacted with
        hoverColour=(100, 150, 150),  # Colour of button when being hovered over
        pressedColour=(100, 200, 200),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: doubPop(player) # Function to call when clicked on
    )

line_tool = Button(
    screen,
    30, 
    SCREEN_HEIGHT / 6,
    60,
    60,

    image=lineTool,
    radius=15,
    inactiveColour=(190,170,190),  # Colour of button when not being interacted with
    hoverColour=(100, 150, 150),  # Colour of button when being hovered over
    pressedColour=(100, 200, 200),  # Colour of button when being clicked
    onClick=lambda: player.set_tool('line')  # Function to call when clicked on
)

box_tool = Button(
    screen,
    30, 
    (SCREEN_HEIGHT / 6)*2,
    60,
    60,

    image=boxbox,
    radius=15,
    inactiveColour=(190,170,190),  # Colour of button when not being interacted with
    hoverColour=(100, 150, 150),  # Colour of button when being hovered over
    pressedColour=(100, 200, 200),  # Colour of button when being clicked
    onClick=lambda: player.set_tool('box')  # Function to call when clicked on
)

circle_tool = Button(
    screen,
    30, 
    (SCREEN_HEIGHT / 6)*3,
    60,
    60,

    image=circlebox,
    radius=15,
    inactiveColour=(190,170,190),  # Colour of button when not being interacted with
    hoverColour=(100, 150, 150),  # Colour of button when being hovered over
    pressedColour=(100, 200, 200),  # Colour of button when being clicked
    onClick=lambda: player.set_tool('circle')  # Function to call when clicked on
)

arc_tool = Button(
    screen,
    30, 
    (SCREEN_HEIGHT / 6)*4,
    60,
    60,

    image=arcbox,
    radius=15,
    inactiveColour=(190,170,190),  # Colour of button when not being interacted with
    hoverColour=(100, 150, 150),  # Colour of button when being hovered over
    pressedColour=(100, 200, 200),  # Colour of button when being clicked
    onClick=lambda: player.set_tool('arc')  # Function to call when clicked on
)

star_tool = Button(
    screen,
    30, 
    (SCREEN_HEIGHT / 6)*5,
    60,
    60,

    image=starbox,
    radius=15,
    inactiveColour=(190,170,190),  # Colour of button when not being interacted with
    hoverColour=(100, 150, 150),  # Colour of button when being hovered over
    pressedColour=(100, 200, 200),  # Colour of button when being clicked
    onClick=lambda: player.set_tool('star')   # Function to call when clicked on
)


class UserPointer():
    def __init__(self):
        self.pos = pygame.mouse.get_pos()
        self.clicking = False
        self.currentNodes = []
        self.disable = False
        self.type = "ARC" # "LINE", "ARC"
        self.arcNodes = []
        self.activeTool = 'line'

    def set_pos(self, mouse_pos):
        self.pos = mouse_pos

    def set_tool(self, tool):
        self.activeTool = tool

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
            if player.pos[0] < SIDE_BAR or player.pos[1] < TOP_BAR:
                pass

            elif player.type == "ARC":
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

    if player.activeTool == "arc":
        player.type = "ARC"
    if player.activeTool == "line":
        player.type = "LINE"

    # render
    screen.fill((255, 253, 238))
    i, j = SIDE_BAR, TOP_BAR
    while i < SCREEN_WIDTH:
        i += PX_PER_IN
        j = TOP_BAR
        while j < SCREEN_HEIGHT:
            j += PX_PER_IN
            pygame.draw.circle(screen, (10, 10, 10), (i-PX_PER_IN/2, j-PX_PER_IN/2), 2)

    pygame.draw.circle(
        screen,
        (255, 0, 0) if player.clicking else (10, 10, 10),
        player.pos,
        7
    )
    if len(player.currentNodes) >= 2:
        pygame.draw.lines(screen, (10, 10, 10), False, player.currentNodes, 10)
    if len(player.arcNodes) == 1:
        pygame.draw.line(screen, (10, 10, 10), player.arcNodes[len(player.arcNodes)-1], player.pos, 10)
    if len(player.arcNodes) > 1:
        pygame.draw.lines(screen, (10, 10, 10), False, player.arcNodes, 10)
    for shape in shapes_list:
        if len(shape) < 2:
            continue
        pygame.draw.lines(screen, (120, 120, 90), False, shape, 10)
    if len(player.currentNodes) > 0 and not player.disable:
        pygame.draw.line(screen, (10, 10, 10), player.currentNodes[len(player.currentNodes)-1], player.pos, 10)
    # Aricks Code
    # Git Blame
    super_UI()
    pw.update(events)
    pygame.display.flip()
    


