import pygame


class Container:
    def __init__(self, x, y,
                child,
                width=None,
                height=None,
                color=None,
                BackgroundImage:str = None,  
                borderColor=None,
                centered = False,
                padding = 0,
                borderRadius = 0,
                border = 0,
                opacity = 1,
            ):
        self.width, self.height = (width or child.width) + 2*padding, (height or child.height) + 2*padding
        self.x, self.y = x, y
        self.rect = pygame.Rect(x,y,self.width, self.height)
        self.color = color       
        self.padding = padding 
        self.borderRadius = borderRadius
        self.child = child
    
    def draw(self, surface:pygame.Surface):
        pygame.draw.rect(surface, self.color or -1, self.rect, 0, self.borderRadius)
        if(self.padding):
            self.child.x, self.child.y = self.x + self.padding, self.y + self.padding
        else:
            self.child.x, self.child.y = self.x, self.y
        self.child.draw(surface)
    

    def handleEvent(self, event:pygame.event):
        
        self.child.handleEvent(event)

   