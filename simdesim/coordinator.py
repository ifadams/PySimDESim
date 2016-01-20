
class Coordinator:

    def __init__(self):
        self.timestep = 0
        self.node_map = {}

    def next_timestep(self):

        # iterate over each node, processing its inbox messages
        for node_id in self.node_map:
            node = self.node_map[id]
            node.process_timestep(self.timestep)

        # now process the outboxes of each node
        #TODO

        self.timestep += 1

    def add_node(self, node_id, node):
        self.node_map[node_id] = node

    def add_action(self, node_id, msg):

        # get the node out
        node = self.node_map[node_id]

        # put the message on the right nodes queue
        node.inbox.put(msg)



