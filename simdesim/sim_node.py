from Queue import PriorityQueue, Empty
from simdesim.action import *

class DESNode:

    def __init__(self, node_id):
        """
        Initialize the node class.

        :param node_id: unique identifier for the node
        """

        self.node_id = node_id
        self.inbox = PriorityQueue()
        self.outbox = []
        self.process_act_ct = 0
        self.outbox_act_ct = 0

    def process_timestep(self, timestep):
        """
        Takes a timestep and processes all messages up
        to and including that timestep
        """

        while True:
            # if theres nothin' in the queue move along
            try:
                cur_msg = self.inbox.get(block=False)
            except Empty:
                break

            # if we've gone past the time step, put it back and break out
            # of the loop
            if cur_msg[ACT_TIMESTEP] > timestep:
                self.inbox.put(cur_msg)
                break

            # otherwise we process the msg
            self.process_action(cur_msg)

    def process_outbox(self):
        """
        Process outgoing actions, meant to be overridden
        """

        self.outbox_act_ct += 1
        for action in self.outbox:
            print action

    def process_action(self, cur_action):
        """
        process incoming actions, meant to be overridden
        """

        self.process_act_ct += 1
        print cur_action