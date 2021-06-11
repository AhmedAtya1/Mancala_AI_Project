from State import state
stateList=[0, 0, 0, 0, 0, 1, 13, 0, 7, 0, 0, 3, 0, 24]
A=state(stateList,5,'player1',"Without Stealing")
print(A.availableMoves())
print(A.nextState())
print(A.newTurn())

