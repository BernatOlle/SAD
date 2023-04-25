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



class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, p):
    win.fill((128,128,128))
    
    image_peon_B = pygame.image.load("peon_blanco.png")
    image_peon1=  pygame.transform.scale(image_peon_B, (80, 80))
    image_peon_N = pygame.image.load("peon_negro.png")
    image_peon2=  pygame.transform.scale(image_peon_N, (80, 80))
    
    
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
            #pygame.draw.rect(win,red,(pieces_p1[i][0]*100+10,pieces_p1[i][1]*100 +50+ 10,80,80))
            win.blit(image_peon1, (pieces_p1[i][0]*100+10, pieces_p1[i][1]*100+50+10))
            #pygame.draw.rect(win,blue,(pieces_p2[i][0]*100+10,pieces_p2[i][1]*100 +50+ 10,80,80))
            win.blit(image_peon2, (pieces_p2[i][0]*100+10, pieces_p2[i][1]*100+50+10))
        font = pygame.font.SysFont("arial", 40)
        if game.get_turn(p):
            text = font.render("Your turn", 1, (255,255,255), True)
        else:
            text = font.render("Opponent turn", 1, (255,255,255), True)
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