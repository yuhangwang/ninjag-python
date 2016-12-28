import yaml
import sys
import os
from .core import ninja_generate
from .check_input import check_input
from .tk import ioTK


def main(f_out, args):
    if len(args) == 0:
        here = os.path.dirname(os.path.realpath(__file__))
        f_usage = os.path.join(here, 'usage.txt')
        print(ioTK.read_all(f_usage))
        print("Error hint: need at least two command line arguments")
        exit()

    ioTK.save_text(
            f_out,
            ninja_generate(
                    check_input(
                        yaml.load(ioTK.read_all(*args))
                        )
                )
        )
