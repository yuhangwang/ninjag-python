from ninjag.tk import dictTK


def test():
    d1 = {"a": 1, "b": [1]}
    d2 = {"a": 2, "b": [2]}
    answer = dictTK.merge(d1, d2)
    solution = {"a": 2, "b": [1, 2]}
    assert answer == solution
