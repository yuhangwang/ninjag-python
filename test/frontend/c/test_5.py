import ninjag
import os
from read_all import read_all


def test():
    f_inputs = [
        "input/in3.yaml",
        ]
    f_answer = "output/build.ninja"
    f_solution = "solution/sol3.ninja"
    cmd = " ".join(["ninjag", *f_inputs])
    os.system(cmd)
    os.rename('build.ninja', f_answer)
    answer = read_all(f_answer)
    solution = read_all(f_solution)
    assert answer == solution
