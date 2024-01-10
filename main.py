import pygame
import random
import time

pygame.init()

width,height = 400,400
game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The Snake Game")

x,y=200,200
delta_x,delta_y=0,0
clock =pygame.time.Clock()
def Snake():
    global x,y 
    x=(x+delta_x)%width
    y=(y+delta_y)%height


    game_screen.fill((0,0,0))


    pygame.draw.rect(game_screen,(255,255,255),[x,y,10,10])
    pygame.display.update()
while True:
    events=pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                delta_x = -10
                delta_y= 0
            elif(event.key==pygame.K_RIGHT):
                delta_x = 10
                delta_y= 0
            elif(event.key==pygame.K_UP):
                delta_x = 0
                delta_y= -10
            elif(event.key==pygame.K_DOWN):
                delta_x = 0
                delta_y= 10
            else:
                continue
            Snake()
        
    if(not events):
        Snake()
    clock.tick(10)
        



