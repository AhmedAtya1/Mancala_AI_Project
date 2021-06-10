0from State import state


class node:
    def __init__(self,pocketsAndMancalas,turn,mode):
        self.turn=turn
        self.mode=mode
        self.pockets=pocketsAndMancalas
        self.state=state(pocketsAndMancalas,1,turn,mode)
        d7k=self.state.nextState()
        self.finish=self.state.newTurn()
        self.moves=self.state.availableMoves()
        self.children=[]
        self.value=""
        self.depth_limit=15

    def get_finish(self):
        return self.finish
    def get_depth(self):
        return self.depth_limit
    def get_turn(self):
        return self.turn
    def get_mode(self):
        return self.mode
    def get_children(self):
        return self.children
    def set_depth(self,val):
        self.depth_limit=val
    def get_moves(self):
        return self.moves
    def get_pockets(self):
        return self.pockets
    def get_move_index(self,index):
        return self.moves[index-1]

    def get_number_of_children(self):
        return len(self.children)

    def get_value(self):
        return self.value
    def cal_score(self,variable1_wieght,variable2_wieght,variable4_wieght,variable5_wirght,parent_list,turnn):

        variable1  =0
        variable2 = 0

        variable4=0
        variable5=0


        if self.pockets[13]>24:
            return 100000

        #for i in self.pockets[0:7]:
            #variable1-=i
        #for i in self.pockets[7:]:
            #variable1 +=i
        variable1=self.pockets[13]-self.pockets[6]

        variable1*= variable1_wieght

        if (parent_list[13]==self.pockets[13]-1) and (parent_list[0]==self.pockets[0]):
            variable2+=1
        if(self.turn==turnn):

            for i in self.moves:

                temp = state(self.pockets, i, turnn, self.mode)
                ttt=temp.nextState()
                if temp.newTurn()==turnn:
                    variable5 += 1
                    variable5 *= variable5_wirght

        variable2*=variable2_wieght


        if (self.mode=="Without Stealing"):
            return variable1

        else:
            for i in self.pockets[0:7]:
                if i ==0:
                    variable4 -= self.pockets[12-i]
            variable4*=variable4_wieght
            return  variable1


    def set_value(self,value):
        self.value=value





