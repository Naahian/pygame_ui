import pygame


class Text:
    def __init__(self,x,y, text, size=18, color=(0,0,0), family="Ariel"):
        self.x, self.y = x,y
        font = pygame.font.SysFont(family, size)
        self.img = font.render(text, True, color)
        self.width, self.height = self.img.get_width(), self.img.get_height()
        print(self.width, self.height)
        
    def draw(self, surface:pygame.Surface):
        surface.blit(self.img, (self.x,self.y))
    
    def handleEvent(self, event):
        pass