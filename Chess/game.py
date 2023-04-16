class Game:
    # te tota la info de la partida
    def __init__(self, id):
        self.turn = [True,False]
        self.move = [False, False]
        self.ready = False
        self.id = id
        self.pieces1 = []
        self.pieces2 = []
        self.all_pieces = self.put_pieces()
        self.wins = [0, 0]
        self.piece_sel = -1
        #hola anna
    
    def put_pieces(self):
        k=0
        for y in range(2):
            for x in range(8):
                self.pieces1.append((x,y))
                self.pieces2.append((x,y+6))
                
        return [self.pieces1,self.pieces2]

    def get_player_pieces(self, p):
        return self.all_pieces[p]
    
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
                self.all_pieces[player][self.piece_sel] = (int(x[1]),int(y[1]))
                self.move[player] = False
                self.turn[player] = False
                if player == 1:
                    self.turn[0] = True
                else:
                    self.turn[1] = True
                
                

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
