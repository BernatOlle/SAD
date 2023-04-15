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
    win.fill((255, 255, 255))
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
