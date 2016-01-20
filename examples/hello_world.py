from simdesim.coordinator import Coordinator
from simdesim.sim_node import DESNode
from simdesim.action import *

#A simple message passing example with a node "primed" and exchanging a ping
#with its neighbor

# Note:
# PING payloads contain the source node and message type
# same with ACK payloads
PING = 0
ACK = 1

# Helpers for indexing into the payload tuple
MSG_TYPE = 0
SOURCE_NODE = 1


# subclass the DESNode
class MessageNode(DESNode):

    def __init__(self, node_id, node_map):

        # initialize super class
        DESNode.__init__(self, node_id)

        # Give every node a copy of the node map
        self.node_map = node_map


    def process_action(self, cur_action):
        self.process_msg_ct += 1


        print "Processing action for Node %s at Timestep %s" % (self.node_id, cur_action[ACT_TIMESTEP])

        if cur_action[ACT_PAYLOAD][MSG_TYPE] == PING:
            print "Received a PING from Node :%s" % cur_action[ACT_PAYLOAD][SOURCE_NODE]
            print "Going to send a message back to be delivered at the next time step."

            # create the response payload, consisting a timestep to deliver the message
            # the destination node, and the action payload, in this case a simple acknowledgement
            time_to_deliver = cur_action[ACT_TIMESTEP] + 1
            destination_node_id = cur_action[ACT_PAYLOAD][SOURCE_NODE]
            payload = (ACK, self.node_id)
            action = create_act_tuple(time_to_deliver, destination_node_id, payload)

            # add the message to the outbox for process/delivery
            self.outbox.append(action)
        elif cur_action[ACT_PAYLOAD][MSG_TYPE] == ACK:
            print "Received ACK from: %s" % cur_action[ACT_PAYLOAD][SOURCE_NODE]

    def process_outbox(self):

        for action in self.outbox:
            # get the target id, and put the
            dest_node_id = action[ACT_TARGET]

            # get the node from the node map and add the action to the inbox
            self.node_map[dest_node_id].inbox.put(action)




def main():

    # initate a coordinator
    my_coord = Coordinator()


    # add a few nodes
    node_1 = ()

    # set an initial message in the outbox


    # Manually step through a few timesteps



if __name__ == "__main__":
    pass

