def ninja_import(import_type, files):
    """Add include/subninja fields
    Args:
        import_type (str): either "include" or "subninja"
        files (list): a list of file names
    Returns:
        a string
    """
    return "\n\n".join(
            map(
                lambda x: "{}: {}".format(import_type, x),
                files
                )
        )
