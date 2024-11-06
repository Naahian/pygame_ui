import pygame


class Text:
    def __init__(self,x,y, text, size=18, color=(0,0,0), family="Ariel"):
        self.x, self.y = x,y
        font = pygame.font.SysFont(family, size)
        self.img = font.render(text, True, color)
    
    def draw(self, surface:pygame.Surface):
        surface.blit(self.img, (self.x,self.y))
    