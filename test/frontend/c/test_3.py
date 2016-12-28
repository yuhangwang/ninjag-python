import ninjag
import os
from read_all import read_all


def test():
    f_inputs = [
        "input/in1.yaml",
        "input/in2.yaml",
        ]
    f_answer = "output/out2.ninja"
    f_solution = "solution/sol2.ninja"
    cmd = " ".join(["ninjag", f_answer, *f_inputs])
    os.system(cmd)
    answer = read_all(f_answer)
    solution = read_all(f_solution)
    assert answer == solution
