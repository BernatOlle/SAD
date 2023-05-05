import pygame
from network import Network
import pickle
pygame.font.init()
#funcioa
width = 800
height = 850
white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)
square_size = width/8
win = pygame.display.set_mode((width, height))


def redrawWindow(win, game, p):
    if p == 0:
        fitxes = "Blanques"
    else:
        fitxes = "Negres"
    win.fill((128,128,128))
    
    image_peon_N=  pygame.transform.scale(pygame.image.load("images/peon_negre.png"), (80, 80))
    image_alfil_N = pygame.transform.scale(pygame.image.load("images/alfil_negre.png"), (80, 80))
    image_caball_N = pygame.transform.scale(pygame.image.load("images/caball_negre.png"), (80, 80))
    image_rei_N = pygame.transform.scale(pygame.image.load("images/rei_negre.png"), (80, 80))
    image_reina_N = pygame.transform.scale(pygame.image.load("images/reina_negre.png"), (80, 80))
    image_torre_N = pygame.transform.scale(pygame.image.load("images/torre_negre.png"), (80, 80))
    
    image_peon_B=  pygame.transform.scale(pygame.image.load("images/peon_blanc.png"), (80, 80))
    image_alfil_B = pygame.transform.scale(pygame.image.load("images/alfil_blanc.png"), (80, 80))
    image_caball_B = pygame.transform.scale(pygame.image.load("images/caball_blanc.png"), (80, 80))
    image_rei_B = pygame.transform.scale(pygame.image.load("images/rei_blanc.png"), (80, 80))
    image_reina_B = pygame.transform.scale(pygame.image.load("images/reina_blanc.png"), (80, 80))
    image_torre_B = pygame.transform.scale(pygame.image.load("images/torre_blanc.png"), (80, 80))
    
    images_fitxes = [image_torre_B, image_caball_B ,image_alfil_B, image_rei_B , image_reina_B,image_alfil_B ,image_caball_B, image_torre_B,
                     image_peon_B,image_peon_B,image_peon_B,image_peon_B,image_peon_B,image_peon_B,image_peon_B,image_peon_B , 
                     image_torre_N, image_caball_N ,image_alfil_N, image_rei_N , image_reina_N,image_alfil_N ,image_caball_N, image_torre_N,
                     image_peon_N,image_peon_N,image_peon_N,image_peon_N,image_peon_N,image_peon_N,image_peon_N,image_peon_N]
    
    if not (game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        for row in range(8):
            for col in range(8):
                x = col * square_size
                y = row * square_size
                if (col+row) % 2 == 0:
                    pygame.draw.rect(win, black, (x, y+50, square_size, square_size))
                else:
                    pygame.draw.rect(win, white, (x, y+50, square_size, square_size))
        
        pieces_p1 = game.get_player_pieces(0)
        pieces_p2 = game.get_player_pieces(1)
        
        for i in range(len(pieces_p1)):  
            win.blit(images_fitxes[i], (pieces_p1[i][0]*100+10, pieces_p1[i][1]*100+50+10))
            win.blit(images_fitxes[i+16], (pieces_p2[i][0]*100+10, pieces_p2[i][1]*100+50+10))
        
        if game.get_partida()==False:
            font = pygame.font.SysFont("arial", 40)
            text = font.render("Partida acabada ", 1, (255,255,255), True)
            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            if (game.get_turn(p)):
                text= font.render("Has perdido", 1, (255,0,0), True)
                win.blit(text, (width/2 - text.get_width()/2, height/2  + text.get_height()))
            else:
                text= font.render("Has ganado", 1, (255,0,0), True)
                win.blit(text, (width/2 - text.get_width()/2, height/2  + text.get_height()))
        else:
            font = pygame.font.SysFont("calibri", 30)
            if game.get_turn(p):
                text = font.render("Your turn "+fitxes, 1, (255,255,255), True)
            else:
                text = font.render("Opponent turn "+fitxes, 1, (255,255,255), True)
            win.blit(text, (width/2 - text.get_width()/2, 15 - text.get_height()/2))
                    
    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    print(str(player))
    pygame.display.set_caption("Client"+ str(player))
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                pos = [x//100,(y-50)//100]
                n.send(str(pos))

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()