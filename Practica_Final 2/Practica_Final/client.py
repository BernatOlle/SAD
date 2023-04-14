import pygame
from network import Network
from player import Player

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joc Ajedrez")
white=(255,255,255)
black=(0,0,0)
square_size = width/8
tablero = [[1,3,5,7,8,6,4,2],
           [9,10,11,12,13,14,15,16],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [25,26,27,28,29,30,31,32],
           [17,19,21,23,24,22,20,18],
           ] 

def redrawWindow(player,player2, win):
    for row in range(8):
        for col in range (8):
            x= col * square_size
            y=row * square_size
            if(col+row)%2 ==0 :
                pygame.draw.rect(screen, black,(x,y,square_size,square_size))
            else:
                pygame.draw.rect(screen, white, (x,y,square_size,square_size))             
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

#def actualitzarTablero(player1, player2): 
     # has de agafar el vector pieces dels players i actualitzar la matriu tablero
   

def main():
    run = True
    n = Network()
    p = n.getP()
    detection=False
    while run:
        p2 = n.send(p)
        check=True
       # actualitzarTablero(p,p2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not detection:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                pos_x = mouse_x//100
                pos_y = mouse_y//100
                print("POS X: ",pos_x)
                print("POS Y: ",pos_y)
                if (tablero[pos_y][pos_x]!=0):
                    detection=True
                    print("TOCA FITXA")
                    check=False
                
            if event.type == pygame.MOUSEBUTTONDOWN and detection and check:
                detection=False
                print("ENTRA")
                new_x , new_y = pygame.mouse.get_pos()
                pos_x = new_x//100
                pos_y = new_y//100
                print("NEW X: ",pos_x)
                print("NEW Y: ",pos_y)
                p.move(pos_x , pos_y , tablero[pos_x][pos_y])
        
        redrawWindow(p,p2, screen)

main()
