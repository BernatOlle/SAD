import pygame
from network import Network
from player import Player

width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joc ajedrez")
white=(255,255,255)
black=(0,0,0)
square_size = width/8



def redrawWindow(player,player2, win):
    for row in range(8):
        for col in range (8):
            x= col * square_size
            y=row * square_size
            if(col+row)%2 ==0 :
                pygame.draw.rect(win, black,(x,y,square_size,square_size))
            else:
                pygame.draw.rect(win, white, (x,y,square_size,square_size))             
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    
    while run:
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(p,p2, win)

main()
