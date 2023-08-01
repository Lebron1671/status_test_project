import pytest


@pytest.mark.parametrize("id, expected_result",
                             [(4, [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]),
                              (5,[])])
def test_get_children_positive(ts, id, expected_result):
    assert ts.getChildren(id) == expected_result

def test_get_children_negative(ts):
    with pytest.raises(ValueError):
        ts.getAllParents(100)