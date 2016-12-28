import yaml
import sys
import os
from .core import ninja_generate
from .check_input import check_input
from . import tk


def main(f_out, args):
    if len(args) == 0:
        here = os.path.dirname(os.path.realpath(__file__))
        f_usage = os.path.join(here, 'usage.txt')
        print(tk.io.read_all(f_usage))
        print("Error hint: need at least two command line arguments")
        exit()

    tk.io.save_text(
            f_out,
            ninja_generate(
                    check_input(
                        yaml.load(tk.io.read_all(*args))
                        )
                )
        )
