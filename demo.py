import pygame
from constants import Colors
from constants import Resolution
from pygame_ui import *

pygame.init()
WIDTH, HEIGHT = Resolution.r800x600
FPS = 60
centerX, centerY = WIDTH//2, HEIGHT//2
pygame.display.set_caption("Pygame UI")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#----------------------- create --------------------------------
def ToggleOpt(x,y, color=Colors.blue):
    togglebarRow = Row(0,0,50, [
            Text(0,0,"Toggle Option", color=Colors.white), 
            ToggleSwitch(0,0, width=40, color=color),
        ])
    return Container(x, y, width=165, color=Colors.grey, borderRadius=20, padding=15, child=togglebarRow)

def Card(x,y, color):    
    cardCol = Column(100,100,10,children=[
        Text(0,0,"Styled Text", size=26, family="Georgia"), 
        Text(0,0,"Some text description of card.", color=(50,50,50)),
        Text(0,0,"Some text description of card.", color=(50,50,50)),
        Text(0,0,"Some text description of card.", color=(50,50,50)),
        BlankSpace(0,0,0,10),
        Button(0,0,"Read More", width=100, height=40, fontSize=18, borderRadius=20, onClick=lambda:print("Card Button clicked!")),
    ])
    return Container(x, y, color=color, borderRadius=10, padding=15, child=cardCol)

card1 = Card(220,180, Colors.yellow)
card2 = Card(422,180, Colors.orange)
title = Text(10,180,"Colored Text", size=28, color=Colors.white)
toggle1 = ToggleOpt(10, 220)
toggle2 = ToggleOpt(10, 280, Colors.green)
toggle3 = ToggleOpt(10, 340)
buttons = Column(630, 180, 15, [
    Button(0,0,"Start", fill=Colors.green),
    Button(0,0,"Stop", fill=Colors.red),
    Button(0,0,"Reset"),
])

#-----------------------------------------------------------------

def draw():
    screen.fill((30, 32, 30))

    card1.draw(screen)
    card2.draw(screen)
    title.draw(screen)
    toggle1.draw(screen)
    toggle2.draw(screen)
    toggle3.draw(screen)
    buttons.draw(screen)
  
    pygame.display.flip()

def update(event:pygame.event ):
    card1.handleEvent(event)
    card2.handleEvent(event)
    toggle1.handleEvent(event)
    toggle2.handleEvent(event)
    toggle3.handleEvent(event)
    buttons.handleEvent(event)


while running:
    draw()
    for event in pygame.event.get():
        update(event)
        
        if(event.type == pygame.QUIT):
            running = False
    clock.tick(FPS)




    

