import pygame


class Row:
    def __init__(self, x, y, marginRight, children:list):
        self.children = children
        self.marginRight = marginRight
        self.x = x
        self.y = y
        self.width = self.getWidth()
        self.height = self.getMaxHeight()
        self.type = "list"

    def draw(self, surface:pygame.Surface):
        x_pos = self.x
        for i in range(len(self.children)):
            x_pos = (self.children[i-1].width)*i + self.marginRight*i + self.x
            self.children[i].y = self.y
            self.children[i].x = x_pos
            self.children[i].draw(surface)

    
    def handleEvent(self, event:pygame.event):
        for item in self.children:
            item.handleEvent(event)
    
    def getMaxHeight(self):
        max = 0
        for item in self.children:
            if(item.height > max): max = item.height
        return max

    def getWidth(self):
        width = 0
        for item in self.children:
            width += (item.width + self.marginRight)
        return width
    