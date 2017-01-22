import ninjag
from ninjag.tk.ioTK import read_all


def test():
    f_input = "input/in4.yaml"
    f_answer = "output/out4.ninja"
    f_solution = "solution/sol4.ninja"
    ninjag.main(f_answer, [f_input])
    answer = read_all(f_answer)
    solution = read_all(f_solution)
    assert answer == solution
