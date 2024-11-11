import pygame


class BlankSpace:
    def __init__(self, x,y,width=0, height=0) :
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def draw(self, surface:pygame.Surface):
        surface.blit(self.surface, (self.x, self.y))

    def handleEvent(self, event): 
        pass