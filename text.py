import pygame

class Text:
    #TODO:set width, height, bold
    def __init__(self,x,y, text, size=14, color=(0,0,0), family="Calibri"):
        self.x, self.y = x,y
        font = pygame.font.SysFont(family, size)
        self.img = font.render(text, True, color)
        self.img.set_clip(pygame.Rect(x,y,100,400))
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        
    def draw(self, surface:pygame.Surface):
        surface.blit(self.img, (self.x,self.y))
    
    def handleEvent(self, event):
        pass