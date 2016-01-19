from simdesim.coordinator import Coordinator
from simdesim.sim_node import DESNode


# subclass the DESNode
class MessageNode(DESNode):

    def __init__(self, node_id, node_map):

        # initialize super class
        DESNode.__init__(self, node_id)

        # GIve every node a copy of the node map
        self.node_map = node_map


    def process_action(self, cur_action):





def main():
    pass
    # initate a coordinator



    # add a few nodes





if __name__ == "__main__":
    pass

