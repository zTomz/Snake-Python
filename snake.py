import pygame, random
from position import Pos

class Snake:
    def __init__(self, surface):
        self.size = 25
        self.surface = surface
        self.body = [Pos(10, 10), Pos(9, 10), Pos(8, 10)]
        self.direction = "RIGHT" # UP, DOWN, LEFT, RIGHT

        self.applePos = Pos(random.randint(0, 19), random.randint(0, 19))

    def update(self):
        index = len(self.body) - 1

        while index > 0:
            lastPart = self.body[index - 1]
            self.body[index].x = lastPart.x
            self.body[index].y = lastPart.y

            index -= 1

        if self.direction == "UP":
            self.body[0].y -= 1
            if self.body[0].y < 0:
                self.body[0].y = 19
        if self.direction == "DOWN":
            self.body[0].y += 1
            if self.body[0].y > 19:
                self.body[0].y = 0
        if self.direction == "LEFT":
            self.body[0].x -= 1
            if self.body[0].x < 0:
                self.body[0].x = 19
        if self.direction == "RIGHT":
            self.body[0].x += 1
            if self.body[0].x > 19:
                self.body[0].x = 0

        head = self.body[0]

        snakeList = self.body.copy()
        snakeList.pop(0)
        for item in snakeList:
            if head.x == item.x and head.y == item.y:
                print("Loose Game")
                self.body = [Pos(10, 10), Pos(9, 10), Pos(8, 10)]

            index -= 1
        
        del snakeList

        if head.x == self.applePos.x and head.y == self.applePos.y:
            self.body.append(Pos(self.body[-1].x, self.body[-1].y))
            self.applePos = Pos(random.randint(0, 19), random.randint(0, 19))
    
    def draw(self):
        for item in self.body:
            pygame.draw.rect(
                self.surface,
                color="#EDD83D",
                border_radius=10,
                rect=pygame.Rect(item.x * self.size, item.y * self.size, self.size - 1, self.size - 1)
            )

        pygame.draw.rect(
            self.surface,
            color="#DE6B48",
            border_radius=5,
            rect=pygame.Rect(self.applePos.x * self.size, self.applePos.y * self.size, self.size - 1, self.size - 1)
        )
        