def check_isList(obj, name):
    """check whether an object is a list
    Args:
        obj (object): an unknown object
        name (str): name of the object
    """
    if not isinstance(obj, list):
        msg = "Error hint: field {} must be a list".format(name)
        msg += "The received type is {}".format(type(obj))
        print(msg)
        exit()
    return True
