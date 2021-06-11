import copy

class state:
    def __init__(self,pocketsAndMancalas,currentMove,turn,mode):
        self.pocketsAndMancalas = pocketsAndMancalas
        #0-5 > player1 pockets & 6 player1 mancala
        #7-12 > player2 pockets & 13 player2 mancala
        self.player1Moves = []
        # 0-5 > player1 pockets
        self.player2Moves = []
        # 7-12 > player2 pockets
        self.currentMove = currentMove
        self.turn = turn
        self.newPocketsAndMancalas = copy.deepcopy(pocketsAndMancalas)
        self.nextTurn = ''
        self.mode=mode





    def availableMoves(self):
        for i in range(0, 6):
            if self.pocketsAndMancalas[i] != 0:
                self.player1Moves.append(i)
            if self.pocketsAndMancalas[i+7] != 0:
                self.player2Moves.append(i+7)
        if self.turn=='player1':
            return self.player1Moves
        elif self.turn=='player2':
            return self.player2Moves


    def nextState(self):
        index=self.currentMove
        noOfBalls=self.pocketsAndMancalas[index]
        self.newPocketsAndMancalas[index]=0
        usedMancala=0
        discardedMancala=0
        zerosInplayer1 = 0
        zerosInplayer2 = 0
        usedRange = []

        if self.turn == 'player1':
            discardedMancala = 13
            usedMancala=6
            usedRange = list(range(0, 6))
            self.nextTurn = 'player2'
        elif self.turn == 'player2':
            discardedMancala = 6
            usedMancala=13
            usedRange = list(range(7, 13))
            self.nextTurn = 'player1'

        if self.mode == "Without Stealing":
            while(noOfBalls>0):
                index+=1
                if index==14:
                    index=0
                if index != discardedMancala:
                    self.newPocketsAndMancalas[index]+=1
                    noOfBalls-=1
            if index==6:
                self.nextTurn = 'player1'
            elif index==13:
                self.nextTurn = 'player2'

        elif self.mode == "With Stealing":
            while (noOfBalls > 0):
                index += 1
                if index == 14:
                    index = 0
                if index != discardedMancala:
                    self.newPocketsAndMancalas[index] += 1
                    noOfBalls -= 1
            if index == 6:
                self.nextTurn = 'player1'
            elif index == 13:
                self.nextTurn = 'player2'
            elif (self.newPocketsAndMancalas[index]==1)and(index in usedRange):
                oppositePocket=self.newPocketsAndMancalas[12-index]
                if oppositePocket != 0:
                    self.newPocketsAndMancalas[12 - index]=0
                    self.newPocketsAndMancalas[index]=0
                    self.newPocketsAndMancalas[usedMancala]+=oppositePocket+1


        for i in range(0, 6):
            if self.newPocketsAndMancalas[i] == 0:
                zerosInplayer1 += 1
            if self.newPocketsAndMancalas[i + 7] == 0:
                zerosInplayer2 += 1

        if zerosInplayer1 == 6:
            for i in range(7, 13):

                self.newPocketsAndMancalas[13] += self.newPocketsAndMancalas[i]
                self.newPocketsAndMancalas[i] = 0
            self.nextTurn="finish"
        elif zerosInplayer2 == 6:
            for i in range(0, 6):
                self.newPocketsAndMancalas[6] += self.newPocketsAndMancalas[i]
                self.newPocketsAndMancalas[i] = 0
            self.nextTurn = "finish"


        return self.newPocketsAndMancalas

    def newTurn(self):
        return self.nextTurn





