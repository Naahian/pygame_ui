import pygame


class ToggleSwitch:
    def __init__(
            self,
            x, y,
            width=60,
            color=(2, 136, 209), #blue
            onActive = lambda:None,
        ):
        self.x, self.y = x, y
        self.width = width
        self.height = width*.5
        self.color = color
        self.isOn = False
        self.onActive = onActive
        self.border = pygame.Rect(x,y, width, self.height)
        self.surface = pygame.surface.Surface((width, self.height))
        self.surface.set_colorkey((0,0,0))

         
    def draw(self, surface:pygame.Surface):
        self.border.x, self.border.y = self.x, self.y
        pygame.draw.rect(self.surface, (60,60,60), (0,0,self.width, self.height), 2, self.width)
        
        if(self.isOn):
            circle_x = self.width - self.width*.25
            pygame.draw.rect(self.surface, self.color, (0,0,self.width, self.height), 0, self.width)
            pygame.draw.circle(self.surface, (255,255,255), (circle_x, self.width*.25),self.width*.21)
        else:
            circle_x = self.width*.25
            pygame.draw.rect(self.surface, (120,120,120), (0,0,self.width, self.height), 0, self.width)
            pygame.draw.circle(self.surface, (255,255,255), (circle_x, self.width*.25),self.width*.21)
        
                
        surface.blit(self.surface, (self.x, self.y))

    
    def handleEvent(self, event:pygame.event):
        pos = pygame.mouse.get_pos()
        
        if self.border.collidepoint(pos):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.isOn = not self.isOn
                if(self.isOn): self.onActive()
                


        