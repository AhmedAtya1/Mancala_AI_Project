from State import state
stateList=[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

A=state(stateList,0,'player1','without stealing')
print(A.nextState())
print(A.newTurn())
print(A.availableMoves())
