from ninjag.tk import dictTK


def test():
    d1 = {"a": {"a1": 1}, "b": [1]}
    d2 = {"a": {"a1": 2}, "b": [2]}
    answer = dictTK.merge([d1, d2])
    solution = {"a": {"a1": 2}, "b": [1, 2]}
    assert answer == solution
