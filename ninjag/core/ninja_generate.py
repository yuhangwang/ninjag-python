from .ninja_def import ninja_def
from .ninja_rule import ninja_rule
from .ninja_build import ninja_build
from .ninja_import import ninja_import


def ninja_generate(argd):
    """Return the transformed Ninja build file content

    Args:
        argd (dict): user configuration dictionary
    Returns:
        a string (content of the Ninja build file)
    """
    return "\n\n\n".join(
        filter(
                lambda x: x != "",
                [
                    ninja_def(argd['def']),
                    ninja_rule(argd['rule']),
                    ninja_build(argd['task']),
                    ninja_import("include", argd['include']),
                    ninja_import("subninja", argd['subninja'])
                ]
            )
        )
