
from State import state
from Node import  node

def create_children(root):

    if (len(root.get_moves())) > 0:
        for i in root.get_moves():

            temp = state(root.get_pockets(), i, root.get_turn(), root.get_mode())
            next_state_array = temp.nextState()
            new_root=node(next_state_array, temp.newTurn(), root.get_mode())
            new_root.set_depth(root.get_depth())
            root.get_children().append(new_root)


def GET_Best_Value(root_node,depth,isMaximizingPlayer, alpha, beta,parent):

    if root_node.get_number_of_children()==0 and depth != root_node.get_depth() and (not (root_node.get_finish()=="finish")) :

        create_children(root_node)

    if (depth==root_node.get_depth()) or (root_node.get_finish()=="finish"):
        return root_node.cal_score(1,15,10,10,parent,"player2")

    if isMaximizingPlayer :
        bestval = - 5000000
        for i in root_node.get_children():
            turn=i.get_turn()
            if turn=='player2':
                maxmizing=True
            else:
                maxmizing=False

            value = GET_Best_Value(i,depth+1,maxmizing, alpha, beta,root_node.get_pockets())
            bestval = max(bestval, value)
            i.set_value(bestval)
            alpha = max(alpha, bestval)
            if beta <= alpha:
                break

        return bestval

    else:
        bestval =  5000000
        for i in root_node.get_children():
            turn = i.get_turn()
            if turn == 'player2':
                maxmizing = False
            else:
                maxmizing = True
            value = GET_Best_Value(i, depth + 1, maxmizing, alpha, beta,root_node.get_pockets())
            bestval = min(bestval, value)
            i.set_value(bestval)
            beta = min(beta, bestval)
            if beta <= alpha:
                break
        return bestval


def GET_AI_MOVE(root_node,depth,isMaximizingPlayer, alpha, beta):
    value=GET_Best_Value(root_node,depth,isMaximizingPlayer, alpha, beta,root_node.get_pockets())
    index=0
    for i in root_node.get_children():
        index+=1
        if i.get_value()==value:
            return root_node.get_move_index(index)