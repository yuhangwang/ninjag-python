def check_const(defs):
    """check const section
    """
    if not isinstance(defs, list):
        print("Error hint: \"const\" section must be a list")
        print("  Your const section has type:", type(defs))
        exit()
    else:
        pass

    for d in defs:
        if not isinstance(d, dict):
            msg = ""
            msg += "Error hint: each \"const definition\" must be a \"dict\"\n"
            msg += "Error hint: your const definition:\n"
            msg += "\t{}\nhas type: {}".format(d, type(d))
            print(msg)
            exit()
    return True
