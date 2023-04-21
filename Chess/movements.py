
class Movements : 
    def verificarPeo(x_vella,y_vella,x_nova,y_nova,player):
        peo = False
        if player == 0:
            if x_nova==x_vella and y_nova==y_vella+1:
                peo=True
        if player == 1:
            if x_nova==x_vella and y_nova==y_vella-1:
                peo=True
        return peo