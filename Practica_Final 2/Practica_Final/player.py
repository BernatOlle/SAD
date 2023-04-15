import pygame
from Practica_Final1.p import  Piece 


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.draw_piece = []
        self.put_pieces(x ,y ,width, height)
        self.vel = 1
        
    # Creas un rectangle que es mostri a la pantalla win 
    # amb els colors i el tamany adecuat
    def draw(self, win):
        for i in range(16):
            pygame.draw.rect(win, self.color, self.piece[i])

    def move(self,x,y,pesa):
        # haura de mirar quina peça es i compara si el moviment que es vol fer es viable i moure-ho al pieces
        if(pesa == Piece.peo1_A):
            self.update(self.x,self.y, x,y)
      #actualitza els canvis  
        
    def update(self, vella_x, vella_y,x, y):
        #pos = self.get_piece(vella_x, vella_y)
        pos=14
        self.piece[pos] = (x*100, y*100, self.width, self.height)
        
    def checkpiece(self, mouse_x, mouse_y):
        piece1=False
        if (self.x<mouse_x<(self.x+self.width)) and (self.y <mouse_y <self.y+ self.height):
            self.color = (0,255,0)
            piece1=True 
        return piece1
    
    def put_pieces(self,x ,y,width,height):
        k=0
        for i in range(2):
            for i in range(8):
                self.piece.append((x + 100 * i, y + 100*k, width, height))
            k=1