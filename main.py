import pygame
from button import Button
from column import Column
from constants import Colors, Resolution
from row import Row

pygame.init()
WIDTH, HEIGHT = Resolution.r800x600
FPS = 60
centerX, centerY = WIDTH//2, HEIGHT//2
pygame.display.set_caption("Pygame UI")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
#################################################

def create():
    
    btnRow1 = Row(0,0,20, [
        Button(
            x=0, y=0,
            centered= True,   
            text= "Item 1",
            onClick=lambda:print("Item 1"),
            fill=Colors.green,
        ),
        Button(
            x=0, y=0,
            centered= True,   
            text= "Item 2",
            onClick=lambda:print("Item 2")
        ),
        Button(
            x=0, y=0,
            centered= True,   
            text= "Item 3",
            borderRadius=0,
            image="assets/btn2.png",
            onClick=lambda:print("Item 3")
        ),
    ])

    btnRow2 = Row(0,0,20, [
        Button(
            x=0, y=0,
            centered= True,   
            text= "Item 4",
             image="assets/btn1.png",
            onClick=lambda:print("Item 4")
        ),
        Button(
            x=0, y=0,
            height= 220,
            # width= 50,
            centered= True,   
            text= "Item 5",
            onClick=lambda:print("Item 5"),  
        ),
    ])

    btnRow3 = Row(0,0,20, [
        Button(
            fill=Colors.red,
            x=0, y=0,
            centered= True,   
            text= "Item 4",
            onClick=lambda:print("Item 4")
        ),
        Button(
            x=0, y=0,
            width= 350,       
            centered= True,   
            text= "Item 5",
            image= "assets/btn3.jpg",
            onClick=lambda:print("Item 5"),
        ),
    ])


    btnCol = Column(0, 0, 20,[ btnRow1, btnRow2, btnRow3])
    btnCol.x = centerX - btnCol.width//2
    btnCol.y = centerY - btnCol.height//1.5

    uiObjects.append(btnCol)
   

def draw():
    background = pygame.image.load("assets/bg.jpg").convert() 
    background.set_alpha(2)
    screen.blit(background, (0,0))
    for obj in uiObjects:
        obj.draw(screen)
    
    pygame.display.flip()


def update():
    pass


#################################################
uiObjects = []
create()

while running:
    update()
    draw()
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            #handle key press event
            if(event.key == pygame.K_ESCAPE):
                running = False

        #handle other events
        for obj in uiObjects:
            obj.handleEvent(event)

    clock.tick(FPS)
    

