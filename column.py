import pygame


class Column:
    def __init__(self, x, y, marginBottom, children:list):
        self.children = children
        self.marginBottom = marginBottom
        self.x = x
        self.y = y
        self.width = self.getMaxWidth()
        self.height = self.getHeight()
        self.type = "list"

    def draw(self, surface:pygame.Surface):
        y_pos = self.y
        for i in range(len(self.children)):
            self.children[i].y = y_pos
            self.children[i].x = self.x
            self.children[i].draw(surface)
            y_pos += (self.children[i].height) + self.marginBottom
    
    def handleEvent(self, event:pygame.event):
        for item in self.children:
            item.handleEvent(event)
    
    def getMaxWidth(self):
        max = 0
        for item in self.children:
            if(item.width > max): max = item.width
        return max

    def getHeight(self):
        height = 0
        for item in self.children:
            height += (item.height + self.marginBottom)
        return height