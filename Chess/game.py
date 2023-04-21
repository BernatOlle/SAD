 # from movements import Movements as m

class Game:
    # te tota la info de la partida
    def __init__(self, id):
        self.turn = [True,False]
        self.move = [False, False]
        self.ready = False
        self.moveCorrect = False
        self.id = id
        self.pieces1 = []
        self.pieces2 = []
        self.all_pieces = self.put_pieces()
        self.wins = [0, 0]
        self.piece_sel = -1
        
    def put_pieces(self):
        k=0
        for y in range(2):
            for x in range(8):
                self.pieces1.append((x,y))
                self.pieces2.append((x,y+7-(y%2)*2))
                
        return [self.pieces1,self.pieces2]

    def get_player_pieces(self, p):
        return self.all_pieces[p]
    
    def get_piece(self,p,move):
        '''
        move = [x, y]
        x = [x
        y =  y]        
        '''
        x,y = move.split(",")
        move = [int(x[1]),int(y[1])]
        print(move)
        try:
            print(self.all_pieces[p])
            pos = self.all_pieces[p].index((int(x[1]),int(y[1])))
        except:
            pos = -1
        return pos

    def play(self, player, move):
        print(self.turn)
        if self.turn[player]== True:
            pos = self.get_piece(player,move)
            print(pos)
            if pos != -1:
                self.move[player] = True
                self.piece_sel = pos
                print("Selecionada figura pos:",pos)
            elif self.move[player] == True:
                x,y = move.split(",")
                x_vella= self.all_pieces[player][self.piece_sel][0]
                y_vella=self.all_pieces[player][self.piece_sel][1]
                
                print("LA POSICIO ES = ", pos)
                if(self.piece_sel==0 or self.piece_sel==7):
                    print("TORRE SELECCIONADA")
                    self.moveCorrect=self.verificarTorre(x_vella,y_vella,int(x[1]),int(y[1]))
                    
                elif(self.piece_sel==2 or self.piece_sel==6):
                    self.moveCorrect=self.verificarCaball(x_vella,y_vella,x[1],y[1])
                elif(self.piece_sel==8 or self.piece_sel==9 or self.piece_sel==10 or self.piece_sel==11 or self.piece_sel==12 or self.piece_sel==13 or self.piece_sel==14 or self.piece_sel ==15 ):
                    self.moveCorrect=self.verificarPeo(x_vella,y_vella,int(x[1]),int(y[1]),player)
                if self.moveCorrect:
                    self.all_pieces[player][self.piece_sel] = (int(x[1]),int(y[1]))
                    self.move[player] = False
                    self.turn[player] = False
                if player == 1:
                    self.turn[0] = True
                else:
                    self.turn[1] = True
                
    def verificarPeo(self, x_vella,y_vella,x_nova,y_nova,player):
        peo = False
        if player == 0:
            if x_nova==x_vella and y_nova==y_vella+1:
                peo=True
        if player == 1:
            if x_nova==x_vella and y_nova==y_vella-1:
                peo=True
        return peo
    
    def verificarTorre(self,x_vella,y_vella,x_nova,y_nova):
        Torre=False
        if (x_vella!=x_nova and y_vella==y_nova) or (x_nova==x_vella and y_nova!=y_vella):
            Torre=True
        return Torre 
     
    def verificarCaball(self,x_vella,y_vella,x_nova,y_nova):
        
        return True
    

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
