from ninjag.tk import dictTK


def test():
    d1 = {"a": 1, "b": [1]}
    d2 = {"a": 2, "b": [2]}
    d3 = {"a": 3, "b": [3]}
    answer = dictTK.merge([d1, d2, d3])
    solution = {"a": 3, "b": [1, 2, 3]}
    assert answer == solution
