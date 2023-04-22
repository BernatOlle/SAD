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
    
    def get_turn(self,p):
        return self.turn[p]
    
    def get_piece(self,p,move):
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
                    self.moveCorrect=self.verificarTorre(x_vella,y_vella,int(x[1]),int(y[1]))
                elif(self.piece_sel==1 or self.piece_sel==6):
                    self.moveCorrect=self.verificarCaball(x_vella,y_vella,int(x[1]),int(y[1]))
                elif(self.piece_sel==8 or self.piece_sel==9 or self.piece_sel==10 or self.piece_sel==11 or self.piece_sel==12 or self.piece_sel==13 or self.piece_sel==14 or self.piece_sel ==15 ):
                    self.moveCorrect=self.verificarPeo(x_vella,y_vella,int(x[1]),int(y[1]),player)
                    #self.kill_piece(player,int(x[1]),int(y[1]))
                elif(self.piece_sel==2 or self.piece_sel==5):
                    self.moveCorrect=self.verificarAlfil(x_vella,y_vella,int(x[1]),int(y[1]))
                elif self.piece_sel==3:
                    self.moveCorrect=self.verificarReina(x_vella,y_vella,int(x[1]),int(y[1]))
                elif self.piece_sel==4:
                    print("Verifica REI ")
                    self.moveCorrect=self.verificarRei(x_vella,y_vella,int(x[1]),int(y[1]))
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
        p = 0 if player == 1 else 1
        coordenada = (x_nova,y_nova)
        if coordenada in self.all_pieces[p]:
            pos=1
        else:
            pos=-1
        if player == 0:
            if x_nova==x_vella and y_nova==y_vella+1:
                peo=True
            elif x_nova==x_vella and y_nova==y_vella+2 and y_vella==1:
                peo=True
            elif pos!=-1 and x_nova==x_vella+1 and y_nova==y_vella+1:
               peo=True
               self.kill_piece(p,x_nova,y_nova)
            elif pos!=-1 and x_nova==x_vella-1 and y_nova==y_vella+1:
                peo=True
                self.kill_piece(p,x_nova,y_nova)
        if player == 1:
            if x_nova==x_vella and y_nova==y_vella-1:
                peo=True
            elif x_nova==x_vella and y_nova==y_vella-2 and y_vella==6:
                peo=True 
            elif pos!=-1 and x_nova==x_vella-1 and y_nova==y_vella-1:
                peo=True
                self.kill_piece(p,x_nova,y_nova)
            elif pos!=-1 and x_nova==x_vella+1 and y_nova==y_vella-1:
                peo=True
                self.kill_piece(p,x_nova,y_nova)
        return peo
    
    def kill_piece(self,player,x_nova,y_nova):
        #NO SE PQ NO FUNCIONA SI HO CRIDO DESDE PEO SI QUE FUNCIONA PERO SI HO CRIDO DESDE
        #EL PLAY ES BUGUEJA EL JOC I ES TANCA 
        coordenada = (x_nova,y_nova)
        #p = 0 if player == 1 else 1
        pos = self.all_pieces[player].index(coordenada)
        self.all_pieces[player][pos]=(0,0)
        print("HAS MATAT!")
        
    def verificarTorre(self,x_vella,y_vella,x_nova,y_nova):
        Torre=False
        if (x_vella!=x_nova and y_vella==y_nova) or (x_nova==x_vella and y_nova!=y_vella):
            Torre=True
            
        return Torre 
     
    def verificarCaball(self,x_vella,y_vella,x_nova,y_nova):
        Caball=False
        diff_x = x_vella-x_nova
        diff_y= y_vella-y_nova
        if ((diff_x==1) and (diff_y==2)) or ((diff_x==-1) and (diff_y==2)) :
            Caball=True
        elif ((diff_x==1) and (diff_y==-2)) or ((diff_x==-1) and (diff_y==-2)):
            Caball=True
        elif ((diff_x==2) and (diff_y==1)) or ((diff_x==2) and (diff_y==-1)) :
            Caball=True
        elif ((diff_x==-2) and (diff_y==1)) or ((diff_x==-2) and (diff_y==-1)):
            Caball=True
        return Caball
    
    def verificarAlfil(self,x_vella,y_vella,x_nova,y_nova):
        Alfil=False
        if (x_nova-x_vella==y_nova-y_vella) or (x_nova-x_vella==-(y_nova-y_vella)) :
            Alfil=True
        return Alfil 
    
    def verificarRei(self,x_vella,y_vella,x_nova,y_nova):
        Rei = False
        print("Verificació ....")
        
        if (x_vella-x_nova==1 and y_nova==y_vella) or (x_vella-x_nova==-1 and y_nova==y_vella):
            print("CORRECTE")
            Rei = True
        elif (y_vella-y_nova==1 and x_nova==x_vella) or (y_vella-y_nova==-1 and x_nova==x_vella):
            Rei = True
            print("CORRECTE")
        elif (y_vella==y_nova+1 and x_vella==x_nova+1) or (y_vella==y_nova-1 and x_vella==x_nova-1) or (y_vella==y_nova+1 and x_vella==x_nova-1) or (y_vella==y_nova-1 and x_vella==x_nova+1):
            Rei=True
            print("CORRECTE")
        return Rei
    
    def verificarReina (self,x_vella,y_vella,x_nova,y_nova):
        Reina = False
        movHoritz=False
        mov_diag=False
        movHoritz= self.verificarTorre(x_vella,y_vella,x_nova,y_nova)
        mov_diag= self.verificarAlfil(x_vella,y_vella,x_nova,y_nova)
        if(movHoritz or mov_diag):
            Reina=True
        return Reina

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
