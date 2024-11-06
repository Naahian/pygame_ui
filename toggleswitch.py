import pygame


class ToggleSwitch:
    def __init__(
            self,
            x, y,
            size=100,
            color=(123,125,250),
            onActive = lambda:None,
        ):
        self.x, self.y = x, y
        self.size = size
        self.color = color
        self.value = False
        self.onActive = onActive
        self.border = pygame.Rect(x,y, size, size*.46)
        self.surface = pygame.surface.Surface((size, size))
        self.surface.set_colorkey((0,0,0))

         
    def draw(self, surface:pygame.Surface):
        self.border.x, self.border.y = self.x, self.y
        pygame.draw.rect(self.surface, (60,60,60), (0,0,self.size, self.size*.46), 2, self.size)
        
        if(self.value):
            circle_x = self.size - self.size*.23
            pygame.draw.rect(self.surface, self.color, (0,0,self.size, self.size*.46), 0, self.size)
            pygame.draw.circle(self.surface, (255,255,255), (circle_x, self.size*.23),self.size*.19)
        else:
            circle_x = self.size*.23
            pygame.draw.rect(self.surface, (150,150,150), (0,0,self.size, self.size*.46), 0, self.size)
            pygame.draw.circle(self.surface, (255,255,255), (circle_x, self.size*.23),self.size*.19)
        
                
        surface.blit(self.surface, (self.x, self.y))

    
    def handleEvent(self, event:pygame.event):
        pos = pygame.mouse.get_pos()
        
        if self.border.collidepoint(pos):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.value = not self.value
                if(self.value): self.onActive()
                


        