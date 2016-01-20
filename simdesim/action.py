# "Constants" for indexing into the payload tuple
ACT_TIMESTEP = 0
ACT_TARGET = 1
ACT_PAYLOAD = 2


def create_act_tuple(timestep, target_id, payload):
    """
    :param timestep: time that the message should be delivered to its target to
    :param target_id: id of the target node the message should be delivered to
    :param payload: payload of the message, can be whatever you so desire
    """
    ret_tup = (timestep, target_id, payload)
    return ret_tup
