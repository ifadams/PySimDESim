# "Constants" for indexing into the payload tuple
MSG_TIMESTEP = 0
MSG_PAYLOAD = 1


def create_act_tuple(timestep, target_id, payload):
    """
    :param timestep: time that the message should be delivered to its target to
    :param target_id: id of the target node the message should be delivered to
    :param payload: payload of the message, can be whatever you so desire
    """
    ret_tup = (timestep, target_id, payload)
    return ret_tup
