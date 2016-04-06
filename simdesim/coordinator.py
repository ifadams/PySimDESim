
class Coordinator:

    def __init__(self):
        self.timestep = 0
        self.node_map = {}

    def next_timestep(self):
        """
        Process all the actions for the current timestep, then increment one
        """

        # iterate over each node, processing its inbox messages
        for node_id in self.node_map:
            node = self.node_map[node_id]
            node.process_timestep(self.timestep)

        # now process the outboxes of each node
        for node_id in self.node_map:
            node = self.node_map[node_id]
            node.process_outbox()

        self.timestep += 1

    def add_node(self, node_id, node):
        """
        Add a node to the coordinators node map
        """
        self.node_map[node_id] = node

    def add_action(self, node_id, msg):
        """
        Add an 'out of band' action to a node
        """

        # get the node out
        node = self.node_map[node_id]

        # put the message on the right nodes queue
        node.inbox.put(msg)



