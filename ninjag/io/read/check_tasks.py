from .check_const import check_const


def check_tasks(tasks):
    """Check tasks section"""
    if not isinstance(tasks, list):
        print("Error hint: \"tasks\" section must be a list")
        exit()
    for d in tasks:
        if "const" in d:
            check_const(d['const'])
    return True
