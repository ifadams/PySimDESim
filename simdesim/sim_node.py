from Queue import PriorityQueue
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
        self.process_msg_ct = 0

    def process_timestep(self, timestep):
        """
        Takes a timestep and processes all messages up
        to and including that timestep
        """

        while True:
            cur_msg = self.inbox.get()

            # if we've gone past the time step, put it back and break out
            # of the loop
            if cur_msg[MSG_TIMESTEP] > timestep:
                self.inbox.put(cur_msg)
                break

            # otherwise we process the msg
            self.process_action(cur_msg)

    def process_action(self, cur_action):

        self.process_msg_ct += 1
        print cur_action[MSG_PAYLOAD]