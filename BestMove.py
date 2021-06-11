
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
